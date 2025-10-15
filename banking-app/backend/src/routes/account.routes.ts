import { Router } from 'express';
import { PrismaClient } from '@prisma/client';
import { authenticateToken, AuthRequest } from '../middleware/auth';
import plaidService from '../services/plaid.service';

const router = Router();
const prisma = new PrismaClient();

// Create Plaid link token
router.post('/link/token', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const linkToken = await plaidService.createLinkToken(req.user!.uid);
    res.json({ linkToken });
  } catch (error) {
    console.error('Link token error:', error);
    res.status(500).json({ error: 'Failed to create link token' });
  }
});

// Exchange public token and sync accounts
router.post('/link/exchange', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const { publicToken } = req.body;
    const { accessToken, itemId } = await plaidService.exchangePublicToken(publicToken);

    // Get accounts from Plaid
    const plaidAccounts = await plaidService.getAccounts(accessToken);

    // Get user from database
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Save accounts to database
    const accounts = await Promise.all(
      plaidAccounts.map((account: any) =>
        prisma.account.create({
          data: {
            userId: user.id,
            plaidAccountId: account.account_id,
            plaidItemId: itemId,
            name: account.name,
            officialName: account.official_name,
            type: account.type,
            subtype: account.subtype,
            mask: account.mask,
            currentBalance: account.balances.current,
            availableBalance: account.balances.available,
            currency: account.balances.iso_currency_code || 'USD',
          },
        })
      )
    );

    // Sync transactions
    const endDate = new Date().toISOString().split('T')[0];
    const startDate = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0];
    await syncTransactions(user.id, accessToken, startDate, endDate);

    res.json({ accounts });
  } catch (error) {
    console.error('Exchange token error:', error);
    res.status(500).json({ error: 'Failed to link account' });
  }
});

// Get all accounts
router.get('/', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const accounts = await prisma.account.findMany({
      where: { userId: user.id, isActive: true },
      include: {
        transactions: {
          take: 10,
          orderBy: { date: 'desc' },
        },
      },
    });

    res.json({ accounts });
  } catch (error) {
    console.error('Get accounts error:', error);
    res.status(500).json({ error: 'Failed to get accounts' });
  }
});

// Get account by ID
router.get('/:id', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const account = await prisma.account.findFirst({
      where: {
        id: req.params.id,
        userId: user.id,
      },
      include: {
        transactions: {
          orderBy: { date: 'desc' },
          take: 50,
        },
      },
    });

    if (!account) {
      return res.status(404).json({ error: 'Account not found' });
    }

    res.json({ account });
  } catch (error) {
    console.error('Get account error:', error);
    res.status(500).json({ error: 'Failed to get account' });
  }
});

// Helper function to sync transactions
async function syncTransactions(userId: string, accessToken: string, startDate: string, endDate: string) {
  const transactions = await plaidService.getTransactions(accessToken, startDate, endDate);
  const aiService = require('../services/ai.service').default;

  for (const txn of transactions) {
    const existing = await prisma.transaction.findUnique({
      where: { plaidTransactionId: txn.transaction_id },
    });

    if (!existing) {
      const account = await prisma.account.findUnique({
        where: { plaidAccountId: txn.account_id },
      });

      if (account) {
        // AI categorization
        const { category, subcategory } = await aiService.categorizeTransaction(
          txn.name,
          txn.amount,
          txn.category
        );

        await prisma.transaction.create({
          data: {
            accountId: account.id,
            plaidTransactionId: txn.transaction_id,
            amount: txn.amount,
            date: new Date(txn.date),
            name: txn.name,
            merchantName: txn.merchant_name,
            category: txn.category,
            aiCategory: category,
            aiSubcategory: subcategory,
            pending: txn.pending,
            paymentChannel: txn.payment_channel,
            location: txn.location || {},
          },
        });
      }
    }
  }
}

export default router;


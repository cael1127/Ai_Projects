import { Router } from 'express';
import { PrismaClient } from '@prisma/client';
import { authenticateToken, AuthRequest } from '../middleware/auth';

const router = Router();
const prisma = new PrismaClient();

// Get all transactions
router.get('/', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const { limit = '50', offset = '0', accountId, category, startDate, endDate } = req.query;

    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
      include: { accounts: true },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const accountIds = user.accounts.map(a => a.id);

    const where: any = {
      accountId: { in: accountIds },
    };

    if (accountId) where.accountId = accountId as string;
    if (category) where.aiCategory = category as string;
    if (startDate || endDate) {
      where.date = {};
      if (startDate) where.date.gte = new Date(startDate as string);
      if (endDate) where.date.lte = new Date(endDate as string);
    }

    const transactions = await prisma.transaction.findMany({
      where,
      orderBy: { date: 'desc' },
      take: parseInt(limit as string),
      skip: parseInt(offset as string),
      include: { account: true },
    });

    const total = await prisma.transaction.count({ where });

    res.json({ transactions, total });
  } catch (error) {
    console.error('Get transactions error:', error);
    res.status(500).json({ error: 'Failed to get transactions' });
  }
});

// Get transaction by ID
router.get('/:id', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
      include: { accounts: true },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const accountIds = user.accounts.map(a => a.id);

    const transaction = await prisma.transaction.findFirst({
      where: {
        id: req.params.id,
        accountId: { in: accountIds },
      },
      include: { account: true },
    });

    if (!transaction) {
      return res.status(404).json({ error: 'Transaction not found' });
    }

    res.json({ transaction });
  } catch (error) {
    console.error('Get transaction error:', error);
    res.status(500).json({ error: 'Failed to get transaction' });
  }
});

// Get spending by category
router.get('/analytics/by-category', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const { startDate, endDate } = req.query;

    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
      include: { accounts: true },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const accountIds = user.accounts.map(a => a.id);

    const where: any = {
      accountId: { in: accountIds },
      amount: { gt: 0 }, // Only expenses
    };

    if (startDate || endDate) {
      where.date = {};
      if (startDate) where.date.gte = new Date(startDate as string);
      if (endDate) where.date.lte = new Date(endDate as string);
    }

    const transactions = await prisma.transaction.findMany({ where });

    // Group by category
    const categorySpending: Record<string, number> = {};
    transactions.forEach(txn => {
      const category = txn.aiCategory || 'Other';
      categorySpending[category] = (categorySpending[category] || 0) + txn.amount;
    });

    const result = Object.entries(categorySpending).map(([category, amount]) => ({
      category,
      amount,
    })).sort((a, b) => b.amount - a.amount);

    res.json({ spending: result });
  } catch (error) {
    console.error('Get category spending error:', error);
    res.status(500).json({ error: 'Failed to get spending by category' });
  }
});

export default router;


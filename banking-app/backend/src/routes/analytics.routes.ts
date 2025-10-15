import { Router } from 'express';
import { PrismaClient } from '@prisma/client';
import { authenticateToken, AuthRequest } from '../middleware/auth';
import aiService from '../services/ai.service';

const router = Router();
const prisma = new PrismaClient();

// Get dashboard summary
router.get('/dashboard', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
      include: {
        accounts: true,
        budgets: true,
        goals: true,
      },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Calculate total balance
    const totalBalance = user.accounts.reduce((sum, acc) => sum + acc.currentBalance, 0);

    // Get recent transactions
    const accountIds = user.accounts.map(a => a.id);
    const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

    const recentTransactions = await prisma.transaction.findMany({
      where: {
        accountId: { in: accountIds },
        date: { gte: thirtyDaysAgo },
      },
    });

    // Calculate spending
    const totalSpent = recentTransactions
      .filter(t => t.amount > 0)
      .reduce((sum, t) => sum + t.amount, 0);

    // Calculate income
    const totalIncome = recentTransactions
      .filter(t => t.amount < 0)
      .reduce((sum, t) => sum + Math.abs(t.amount), 0);

    // Get top categories
    const categorySpending: Record<string, number> = {};
    recentTransactions
      .filter(t => t.amount > 0)
      .forEach(t => {
        const category = t.aiCategory || 'Other';
        categorySpending[category] = (categorySpending[category] || 0) + t.amount;
      });

    const topCategories = Object.entries(categorySpending)
      .map(([category, amount]) => ({ category, amount }))
      .sort((a, b) => b.amount - a.amount)
      .slice(0, 5);

    res.json({
      totalBalance,
      totalSpent,
      totalIncome,
      netSavings: totalIncome - totalSpent,
      topCategories,
      accountCount: user.accounts.length,
      activeBudgets: user.budgets.filter(b => b.isActive).length,
      savingGoals: user.goals.length,
    });
  } catch (error) {
    console.error('Dashboard error:', error);
    res.status(500).json({ error: 'Failed to get dashboard data' });
  }
});

// Generate AI insights
router.get('/insights', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
      include: {
        accounts: true,
        budgets: true,
      },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const accountIds = user.accounts.map(a => a.id);
    const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

    const transactions = await prisma.transaction.findMany({
      where: {
        accountId: { in: accountIds },
        date: { gte: thirtyDaysAgo },
      },
    });

    const insights = await aiService.generateFinancialInsights(transactions, user.budgets);

    res.json({ insights });
  } catch (error) {
    console.error('Insights error:', error);
    res.status(500).json({ error: 'Failed to generate insights' });
  }
});

// Get spending predictions
router.get('/predictions', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
      include: { accounts: true },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const accountIds = user.accounts.map(a => a.id);
    const ninetyDaysAgo = new Date(Date.now() - 90 * 24 * 60 * 60 * 1000);

    const transactions = await prisma.transaction.findMany({
      where: {
        accountId: { in: accountIds },
        date: { gte: ninetyDaysAgo },
        amount: { gt: 0 }, // Only expenses
      },
    });

    const predictions = await aiService.predictFutureExpenses(transactions);

    res.json({ predictions });
  } catch (error) {
    console.error('Predictions error:', error);
    res.status(500).json({ error: 'Failed to generate predictions' });
  }
});

// Get saving suggestions
router.get('/savings-suggestions', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
      include: {
        accounts: true,
        goals: true,
      },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const accountIds = user.accounts.map(a => a.id);
    const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

    const transactions = await prisma.transaction.findMany({
      where: {
        accountId: { in: accountIds },
        date: { gte: thirtyDaysAgo },
      },
    });

    const income = transactions
      .filter(t => t.amount < 0)
      .reduce((sum, t) => sum + Math.abs(t.amount), 0);

    const expenses = transactions
      .filter(t => t.amount > 0)
      .reduce((sum, t) => sum + t.amount, 0);

    const suggestions = await aiService.generateSavingSuggestions(income, expenses, user.goals);

    res.json({ suggestions });
  } catch (error) {
    console.error('Savings suggestions error:', error);
    res.status(500).json({ error: 'Failed to generate saving suggestions' });
  }
});

export default router;


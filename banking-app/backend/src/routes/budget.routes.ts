import { Router } from 'express';
import { PrismaClient } from '@prisma/client';
import { authenticateToken, AuthRequest } from '../middleware/auth';

const router = Router();
const prisma = new PrismaClient();

// Get all budgets
router.get('/', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const budgets = await prisma.budget.findMany({
      where: { userId: user.id, isActive: true },
      orderBy: { createdAt: 'desc' },
    });

    res.json({ budgets });
  } catch (error) {
    console.error('Get budgets error:', error);
    res.status(500).json({ error: 'Failed to get budgets' });
  }
});

// Create budget
router.post('/', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const { category, amount, period, startDate, endDate } = req.body;

    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const budget = await prisma.budget.create({
      data: {
        userId: user.id,
        category,
        amount,
        period,
        startDate: new Date(startDate),
        endDate: endDate ? new Date(endDate) : undefined,
      },
    });

    res.json({ budget });
  } catch (error) {
    console.error('Create budget error:', error);
    res.status(500).json({ error: 'Failed to create budget' });
  }
});

// Update budget
router.put('/:id', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const { category, amount, period, isActive } = req.body;

    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const budget = await prisma.budget.updateMany({
      where: {
        id: req.params.id,
        userId: user.id,
      },
      data: {
        ...(category && { category }),
        ...(amount && { amount }),
        ...(period && { period }),
        ...(isActive !== undefined && { isActive }),
      },
    });

    res.json({ budget });
  } catch (error) {
    console.error('Update budget error:', error);
    res.status(500).json({ error: 'Failed to update budget' });
  }
});

// Delete budget
router.delete('/:id', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    await prisma.budget.deleteMany({
      where: {
        id: req.params.id,
        userId: user.id,
      },
    });

    res.json({ message: 'Budget deleted' });
  } catch (error) {
    console.error('Delete budget error:', error);
    res.status(500).json({ error: 'Failed to delete budget' });
  }
});

export default router;


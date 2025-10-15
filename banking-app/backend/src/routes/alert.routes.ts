import { Router } from 'express';
import { PrismaClient } from '@prisma/client';
import { authenticateToken, AuthRequest } from '../middleware/auth';

const router = Router();
const prisma = new PrismaClient();

// Get all alerts
router.get('/', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const { unreadOnly } = req.query;

    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const where: any = { userId: user.id };
    if (unreadOnly === 'true') {
      where.isRead = false;
    }

    const alerts = await prisma.alert.findMany({
      where,
      orderBy: { createdAt: 'desc' },
      take: 50,
    });

    res.json({ alerts });
  } catch (error) {
    console.error('Get alerts error:', error);
    res.status(500).json({ error: 'Failed to get alerts' });
  }
});

// Mark alert as read
router.put('/:id/read', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    const alert = await prisma.alert.updateMany({
      where: {
        id: req.params.id,
        userId: user.id,
      },
      data: { isRead: true },
    });

    res.json({ alert });
  } catch (error) {
    console.error('Mark read error:', error);
    res.status(500).json({ error: 'Failed to mark alert as read' });
  }
});

// Mark all alerts as read
router.put('/read-all', authenticateToken, async (req: AuthRequest, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: { firebaseUid: req.user!.uid },
    });

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    await prisma.alert.updateMany({
      where: {
        userId: user.id,
        isRead: false,
      },
      data: { isRead: true },
    });

    res.json({ message: 'All alerts marked as read' });
  } catch (error) {
    console.error('Mark all read error:', error);
    res.status(500).json({ error: 'Failed to mark all alerts as read' });
  }
});

export default router;


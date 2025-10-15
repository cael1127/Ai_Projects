'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { interviews, analytics } from '@/lib/api'
import { Calendar, TrendingUp, Clock, CheckCircle, Plus, RefreshCw } from 'lucide-react'
import { format } from 'date-fns'

export default function DashboardPage() {
  const router = useRouter()
  const [stats, setStats] = useState<any>(null)
  const [upcomingInterviews, setUpcomingInterviews] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [syncing, setSyncing] = useState(false)

  useEffect(() => {
    loadDashboardData()
  }, [])

  const loadDashboardData = async () => {
    try {
      const [statsData, interviewsData] = await Promise.all([
        analytics.getDashboard(),
        interviews.getAll(),
      ])
      setStats(statsData)
      // Filter upcoming interviews
      const upcoming = interviewsData.filter((i: any) => 
        i.status === 'upcoming' && new Date(i.scheduled_date) > new Date()
      ).slice(0, 5)
      setUpcomingInterviews(upcoming)
    } catch (error) {
      console.error('Failed to load dashboard:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSyncGmail = async () => {
    setSyncing(true)
    try {
      await interviews.syncFromGmail()
      await loadDashboardData()
      alert('Successfully synced interviews from Gmail!')
    } catch (error) {
      alert('Failed to sync from Gmail')
    } finally {
      setSyncing(false)
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-lg">Loading...</div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b">
        <div className="container mx-auto px-4 py-4">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold">Interview Prep Dashboard</h1>
            <div className="flex gap-2">
              <Button variant="outline" onClick={handleSyncGmail} disabled={syncing}>
                <RefreshCw className={`h-4 w-4 mr-2 ${syncing ? 'animate-spin' : ''}`} />
                Sync Gmail
              </Button>
              <Button onClick={() => router.push('/interviews/new')}>
                <Plus className="h-4 w-4 mr-2" />
                Add Interview
              </Button>
            </div>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <StatCard
            title="Total Interviews"
            value={stats?.total_interviews || 0}
            icon={<Calendar className="h-6 w-6" />}
            color="blue"
          />
          <StatCard
            title="Upcoming"
            value={stats?.upcoming_interviews || 0}
            icon={<Clock className="h-6 w-6" />}
            color="yellow"
          />
          <StatCard
            title="Completed"
            value={stats?.completed_interviews || 0}
            icon={<CheckCircle className="h-6 w-6" />}
            color="green"
          />
          <StatCard
            title="Success Rate"
            value={stats?.success_rate ? `${stats.success_rate.toFixed(0)}%` : 'N/A'}
            icon={<TrendingUp className="h-6 w-6" />}
            color="purple"
          />
        </div>

        {/* Upcoming Interviews */}
        <Card>
          <CardHeader>
            <CardTitle>Upcoming Interviews</CardTitle>
            <CardDescription>Your scheduled interviews</CardDescription>
          </CardHeader>
          <CardContent>
            {upcomingInterviews.length === 0 ? (
              <div className="text-center py-8 text-muted-foreground">
                No upcoming interviews. Sync from Gmail or add one manually.
              </div>
            ) : (
              <div className="space-y-4">
                {upcomingInterviews.map((interview) => (
                  <div
                    key={interview.id}
                    className="flex items-center justify-between p-4 border rounded-lg hover:bg-gray-50 cursor-pointer"
                    onClick={() => router.push(`/interviews/${interview.id}`)}
                  >
                    <div className="flex-1">
                      <h3 className="font-semibold">{interview.company}</h3>
                      <p className="text-sm text-muted-foreground">{interview.position}</p>
                      <p className="text-sm text-muted-foreground mt-1">
                        {format(new Date(interview.scheduled_date), 'PPP p')}
                      </p>
                    </div>
                    <div className="text-right">
                      <span className="inline-block px-3 py-1 text-xs rounded-full bg-blue-100 text-blue-800">
                        {interview.interview_type}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>
      </main>
    </div>
  )
}

function StatCard({ title, value, icon, color }: any) {
  const colorClasses = {
    blue: 'bg-blue-500',
    yellow: 'bg-yellow-500',
    green: 'bg-green-500',
    purple: 'bg-purple-500',
  }

  return (
    <Card>
      <CardContent className="pt-6">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm font-medium text-muted-foreground">{title}</p>
            <p className="text-3xl font-bold mt-2">{value}</p>
          </div>
          <div className={`p-3 rounded-full ${colorClasses[color as keyof typeof colorClasses]} text-white`}>
            {icon}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}


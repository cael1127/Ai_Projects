'use client'

import { useRouter } from 'next/navigation'
import { useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Calendar, Brain, TrendingUp, Mail } from 'lucide-react'

export default function Home() {
  const router = useRouter()

  useEffect(() => {
    // Check if user is logged in
    const token = localStorage.getItem('token')
    if (token) {
      router.push('/dashboard')
    }
  }, [router])

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Header */}
      <header className="container mx-auto px-4 py-6 flex justify-between items-center">
        <div className="flex items-center space-x-2">
          <Brain className="h-8 w-8 text-blue-600" />
          <span className="text-2xl font-bold text-gray-900">Interview Prep</span>
        </div>
        <div className="space-x-4">
          <Button variant="ghost" onClick={() => router.push('/auth/login')}>
            Login
          </Button>
          <Button onClick={() => router.push('/auth/register')}>
            Get Started
          </Button>
        </div>
      </header>

      {/* Hero Section */}
      <main className="container mx-auto px-4 py-20">
        <div className="text-center max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            Ace Your Next Interview with{' '}
            <span className="text-blue-600">AI-Powered Prep</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Automatically detect interviews from Gmail, generate tailored questions,
            and schedule prep sessions in your calendar. All powered by AI.
          </p>
          <div className="flex justify-center space-x-4">
            <Button size="lg" onClick={() => router.push('/auth/register')}>
              Start Preparing Free
            </Button>
            <Button size="lg" variant="outline" onClick={() => router.push('/auth/login')}>
              Sign In with Google
            </Button>
          </div>
        </div>

        {/* Features */}
        <div className="mt-24 grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <FeatureCard
            icon={<Mail className="h-10 w-10 text-blue-600" />}
            title="Gmail Integration"
            description="Automatically detect interview invitations from your email"
          />
          <FeatureCard
            icon={<Brain className="h-10 w-10 text-blue-600" />}
            title="AI Questions"
            description="Generate tailored interview questions based on role and company"
          />
          <FeatureCard
            icon={<Calendar className="h-10 w-10 text-blue-600" />}
            title="Auto-Schedule"
            description="Automatically schedule prep sessions in Google Calendar"
          />
          <FeatureCard
            icon={<TrendingUp className="h-10 w-10 text-blue-600" />}
            title="Track Progress"
            description="Monitor your preparation and interview performance"
          />
        </div>

        {/* How It Works */}
        <div className="mt-32">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
            How It Works
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <StepCard
              number="1"
              title="Connect Your Gmail"
              description="Securely connect your Gmail account to automatically detect interview invitations"
            />
            <StepCard
              number="2"
              title="Get AI Questions"
              description="Our AI generates customized interview questions based on the role and company"
            />
            <StepCard
              number="3"
              title="Prep & Succeed"
              description="Follow your automated prep schedule and track your progress"
            />
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t mt-32 py-8">
        <div className="container mx-auto px-4 text-center text-gray-600">
          <p>&copy; 2024 Interview Prep Tool. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

function FeatureCard({ icon, title, description }: { icon: React.ReactNode; title: string; description: string }) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
      <div className="mb-4">{icon}</div>
      <h3 className="text-lg font-semibold text-gray-900 mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  )
}

function StepCard({ number, title, description }: { number: string; title: string; description: string }) {
  return (
    <div className="text-center">
      <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-blue-600 text-white text-2xl font-bold mb-4">
        {number}
      </div>
      <h3 className="text-xl font-semibold text-gray-900 mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  )
}


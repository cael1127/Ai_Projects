import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Handle 401 errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/auth/login'
    }
    return Promise.reject(error)
  }
)

export const auth = {
  register: async (email: string, password: string, fullName?: string) => {
    const response = await api.post('/api/auth/register', {
      email,
      password,
      full_name: fullName,
    })
    return response.data
  },

  login: async (email: string, password: string) => {
    const formData = new FormData()
    formData.append('username', email)
    formData.append('password', password)

    const response = await api.post('/api/auth/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })
    return response.data
  },

  getGoogleAuthUrl: async () => {
    const response = await api.get('/api/auth/google/login')
    return response.data
  },

  googleCallback: async (code: string) => {
    const response = await api.post('/api/auth/google/callback', { code })
    return response.data
  },

  getCurrentUser: async () => {
    const response = await api.get('/api/auth/me')
    return response.data
  },
}

export const interviews = {
  getAll: async () => {
    const response = await api.get('/api/interviews')
    return response.data
  },

  getById: async (id: number) => {
    const response = await api.get(`/api/interviews/${id}`)
    return response.data
  },

  create: async (data: any) => {
    const response = await api.post('/api/interviews', data)
    return response.data
  },

  update: async (id: number, data: any) => {
    const response = await api.put(`/api/interviews/${id}`, data)
    return response.data
  },

  delete: async (id: number) => {
    const response = await api.delete(`/api/interviews/${id}`)
    return response.data
  },

  generateQuestions: async (id: number, numQuestions: number = 10) => {
    const response = await api.post(`/api/interviews/${id}/questions`, null, {
      params: { num_questions: numQuestions },
    })
    return response.data
  },

  syncFromGmail: async () => {
    const response = await api.post('/api/interviews/sync-from-gmail')
    return response.data
  },

  schedulePrepSessions: async (id: number, daysBefore: number = 3) => {
    const response = await api.post(`/api/interviews/${id}/schedule-prep`, null, {
      params: { days_before: daysBefore },
    })
    return response.data
  },
}

export const prepSessions = {
  getAll: async () => {
    const response = await api.get('/api/prep-sessions')
    return response.data
  },

  getById: async (id: number) => {
    const response = await api.get(`/api/prep-sessions/${id}`)
    return response.data
  },

  create: async (data: any) => {
    const response = await api.post('/api/prep-sessions', data)
    return response.data
  },

  update: async (id: number, data: any) => {
    const response = await api.put(`/api/prep-sessions/${id}`, data)
    return response.data
  },

  start: async (id: number) => {
    const response = await api.post(`/api/prep-sessions/${id}/start`)
    return response.data
  },

  complete: async (id: number) => {
    const response = await api.post(`/api/prep-sessions/${id}/complete`)
    return response.data
  },
}

export const analytics = {
  getDashboard: async () => {
    const response = await api.get('/api/analytics/dashboard')
    return response.data
  },

  getPerformance: async (interviewId: number) => {
    const response = await api.get(`/api/analytics/performance/${interviewId}`)
    return response.data
  },

  createPerformance: async (data: any) => {
    const response = await api.post('/api/analytics/performance', data)
    return response.data
  },

  updatePerformance: async (interviewId: number, data: any) => {
    const response = await api.put(`/api/analytics/performance/${interviewId}`, data)
    return response.data
  },
}


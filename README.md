# Three AI-Powered Full-Stack Projects

This repository contains three production-ready, full-stack AI applications designed to showcase modern web development practices and AI integration.

## Projects

### 1. 🎯 Smart Interview Prep Tool
**Location**: `interview-prep/`

AI-powered interview preparation with Gmail and Google Calendar integration.

**Features**:
- Auto-detect interviews from Gmail
- AI-generated question sets tailored to interview type
- Auto-schedule prep sessions in Google Calendar
- Performance tracking and analytics
- Gmail and Calendar OAuth integration

**Tech Stack**:
- **Backend**: Python, FastAPI, PostgreSQL, OpenAI API, Gmail API, Google Calendar API
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS, shadcn/ui

**Quick Start**:
```bash
cd interview-prep/backend
pip install -r requirements.txt
uvicorn app.main:app --reload

cd ../frontend
npm install
npm run dev
```

---

### 2. 💰 AI-Powered Banking App
**Location**: `banking-app/`

Comprehensive banking application with AI spending insights and Plaid integration.

**Features**:
- Bank account connection via Plaid (mock mode available)
- AI transaction categorization
- Spending predictions and insights
- Budget tracking and alerts
- Real-time dashboards
- Web + Mobile apps (React Native/Expo)

**Tech Stack**:
- **Backend**: Node.js, Express, TypeScript, PostgreSQL (Supabase), Plaid API, OpenAI API
- **Web**: Next.js 14, TypeScript, Tailwind CSS, Firebase Auth
- **Mobile**: React Native (Expo), TypeScript, React Native Paper

**Quick Start**:
```bash
cd banking-app/backend
npm install
npm run dev

cd ../web
npm install
npm run dev

cd ../mobile
npm install
npm start
```

---

### 3. 🤖 AI Job Applier
**Location**: `job-applier/`

Automated job application tool with AI resume/cover letter generation and browser automation.

**Features**:
- Auto-fill job applications with Playwright
- AI-generated resumes tailored per job
- AI-generated cover letters per company
- Track applications and recruiter responses
- Gmail integration for response tracking
- Analytics: conversion rates, interview pipeline

**Tech Stack**:
- **Backend**: Python, FastAPI, PostgreSQL, Playwright, OpenAI API, Gmail API
- **Frontend**: React, TypeScript, Tailwind CSS

**Quick Start**:
```bash
cd job-applier/backend
pip install -r requirements.txt
playwright install
uvicorn app.main:app --reload --port 8001

cd ../frontend
npm install
npm run dev
```

---

## Project Structure

```
AiProjects/
├── interview-prep/
│   ├── backend/          # FastAPI backend
│   └── frontend/         # Next.js frontend
├── banking-app/
│   ├── backend/          # Node.js/Express backend
│   ├── web/              # Next.js web app
│   └── mobile/           # React Native mobile app
├── job-applier/
│   ├── backend/          # FastAPI backend
│   └── frontend/         # React frontend
└── README.md
```

## Common Features Across All Projects

- ✅ **Production-ready**: Comprehensive error handling, logging, security
- ✅ **Modern UI**: Beautiful, responsive interfaces with Tailwind CSS
- ✅ **AI Integration**: Leveraging OpenAI GPT-4 for intelligent features
- ✅ **Authentication**: Secure OAuth 2.0 and JWT implementations
- ✅ **Database**: PostgreSQL with proper models and relationships
- ✅ **API Documentation**: OpenAPI/Swagger docs for all endpoints
- ✅ **Mock Modes**: Test without real API keys where applicable
- ✅ **Docker Support**: Easy containerized deployment
- ✅ **Comprehensive READMEs**: Detailed setup and usage instructions

## Prerequisites

### All Projects
- Git
- Code editor (VS Code recommended)

### Interview Prep & Job Applier (Python)
- Python 3.11+
- PostgreSQL 15+
- pip

### Banking App (Node.js)
- Node.js 18+
- PostgreSQL 15+ or Supabase account
- npm or yarn

### Mobile Development
- Expo CLI
- iOS Simulator (Mac) or Android Emulator

## API Keys Required

### Required for Full Functionality
- **OpenAI API Key**: All projects use GPT-4
  - Get at: https://platform.openai.com/

### Optional (Mock Modes Available)
- **Google Cloud** (Interview Prep):
  - Gmail API
  - Google Calendar API
  - Get at: https://console.cloud.google.com/

- **Firebase** (Banking App):
  - Authentication
  - Get at: https://console.firebase.google.com/

- **Plaid** (Banking App):
  - Sandbox credentials available
  - Get at: https://plaid.com/

## Environment Setup

Each project has a `.env.example` file. Copy it to `.env` and fill in your credentials:

```bash
# Example for Interview Prep
cd interview-prep/backend
cp .env.example .env
# Edit .env with your API keys
```

## Database Setup

Each project needs PostgreSQL:

```bash
# Create databases
createdb interview_prep
createdb banking_app
createdb job_applier
```

Update `DATABASE_URL` in each project's `.env` file.

## Running All Projects

**Terminal 1 - Interview Prep Backend**:
```bash
cd interview-prep/backend
uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Interview Prep Frontend**:
```bash
cd interview-prep/frontend
npm run dev  # Port 3000
```

**Terminal 3 - Banking Backend**:
```bash
cd banking-app/backend
npm run dev  # Port 3001
```

**Terminal 4 - Banking Web**:
```bash
cd banking-app/web
npm run dev  # Port 3002
```

**Terminal 5 - Job Applier Backend**:
```bash
cd job-applier/backend
uvicorn app.main:app --reload --port 8001
```

**Terminal 6 - Job Applier Frontend**:
```bash
cd job-applier/frontend
npm run dev  # Port 3003
```

## Ports

- Interview Prep Backend: `8000`
- Interview Prep Frontend: `3000`
- Banking Backend: `3001`
- Banking Web: `3002`
- Job Applier Backend: `8001`
- Job Applier Frontend: `3003`

## Testing with Mock Data

All projects include mock modes for testing without real API integrations:

- **Interview Prep**: Set `MOCK_MODE=True` for mock Gmail/Calendar
- **Banking App**: Set `MOCK_PLAID=true` for mock bank data
- **Job Applier**: Set `MOCK_AUTOMATION=true` for mock browser automation

## Documentation

Each project has its own detailed README:
- [Interview Prep Backend](interview-prep/backend/README.md)
- [Interview Prep Frontend](interview-prep/frontend/README.md)
- [Banking Backend](banking-app/backend/README.md)
- [Banking Web](banking-app/web/README.md)
- [Banking Mobile](banking-app/mobile/README.md)
- [Job Applier Backend](job-applier/backend/README.md)
- [Job Applier Frontend](job-applier/frontend/README.md)

## Deployment

Each project includes:
- Dockerfile
- docker-compose.yml
- Production configuration examples
- Deployment guides in individual READMEs

## Features Comparison

| Feature | Interview Prep | Banking App | Job Applier |
|---------|---------------|-------------|-------------|
| AI Integration | ✅ Question Gen | ✅ Spending Analysis | ✅ Resume/Cover Letter |
| External APIs | Gmail, Calendar | Plaid, Firebase | Gmail, Playwright |
| Real-time Features | Calendar Sync | Transaction Updates | Application Status |
| Mobile App | ❌ | ✅ | ❌ |
| Browser Automation | ❌ | ❌ | ✅ |
| Analytics Dashboard | ✅ | ✅ | ✅ |

## Architecture Highlights

### Interview Prep
- **Pattern**: Microservices with dedicated AI, Gmail, Calendar services
- **Auth**: Google OAuth 2.0 with JWT
- **Real-time**: Calendar event synchronization

### Banking App
- **Pattern**: RESTful API with real-time updates
- **Auth**: Firebase Authentication
- **Database**: Supabase (PostgreSQL + real-time)
- **Cross-platform**: Shared TypeScript types between web and mobile

### Job Applier
- **Pattern**: Queue-based automation with Celery
- **Auth**: JWT with optional OAuth
- **Automation**: Playwright for cross-platform browser control
- **AI**: Multi-stage AI pipeline for resume/cover letter generation

## Contributing

These are portfolio/demonstration projects. Feel free to fork and customize for your needs.

## License

MIT License - See individual project READMEs for details.

## Support

For questions or issues:
1. Check individual project READMEs
2. Review API documentation at `/docs` endpoint for each backend
3. Check `.env.example` files for configuration options

---

**Built with ❤️ using modern web technologies and AI**


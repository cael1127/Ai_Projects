# Banking App - Backend

AI-powered banking application backend with Plaid integration (mock mode available).

## Features

- **Plaid Integration**: Connect to bank accounts (sandbox/mock mode)
- **AI Categorization**: Automatic transaction categorization using OpenAI
- **Real-time Analytics**: Spending insights and predictions
- **Budget Tracking**: Set and monitor budgets
- **Smart Alerts**: Unusual activity detection
- **Firebase Auth**: Secure authentication
- **Supabase**: PostgreSQL database with real-time features

## Tech Stack

- Node.js + Express + TypeScript
- Prisma ORM
- PostgreSQL (Supabase)
- Firebase Admin SDK
- Plaid API (mock mode available)
- OpenAI API

## Setup

### Prerequisites

- Node.js 18+
- PostgreSQL database (Supabase recommended)
- Firebase project
- OpenAI API key

### Installation

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Set up environment variables**:
   Copy `.env.example` to `.env` and fill in your credentials.

3. **Set up Prisma**:
   ```bash
   npx prisma generate
   npx prisma db push
   ```

4. **Run development server**:
   ```bash
   npm run dev
   ```

   Server runs on http://localhost:3001

## API Endpoints

### Authentication
- `POST /api/auth/sync` - Sync Firebase user to database
- `GET /api/auth/me` - Get current user

### Accounts
- `POST /api/accounts/link/token` - Create Plaid link token
- `POST /api/accounts/link/exchange` - Exchange public token
- `GET /api/accounts` - Get all accounts
- `GET /api/accounts/:id` - Get account details

### Transactions
- `GET /api/transactions` - Get transactions (with filters)
- `GET /api/transactions/:id` - Get transaction details
- `GET /api/transactions/analytics/by-category` - Spending by category

### Budgets
- `GET /api/budgets` - Get all budgets
- `POST /api/budgets` - Create budget
- `PUT /api/budgets/:id` - Update budget
- `DELETE /api/budgets/:id` - Delete budget

### Analytics
- `GET /api/analytics/dashboard` - Dashboard summary
- `GET /api/analytics/insights` - AI-generated insights
- `GET /api/analytics/predictions` - Spending predictions
- `GET /api/analytics/savings-suggestions` - Saving suggestions

### Alerts
- `GET /api/alerts` - Get alerts
- `PUT /api/alerts/:id/read` - Mark alert as read
- `PUT /api/alerts/read-all` - Mark all alerts as read

## Mock Mode

Set `MOCK_PLAID=true` in `.env` to use mock Plaid data without real API keys.
Mock mode provides:
- Simulated bank accounts
- Generated transactions
- Realistic data for testing

## License

MIT


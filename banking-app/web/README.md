# Banking App - Web Frontend

Modern web interface for the AI-Powered Banking App.

## Features

- **Firebase Authentication**: Secure user authentication
- **Plaid Integration**: Connect bank accounts
- **Real-time Dashboard**: View accounts and transactions
- **AI Insights**: Smart spending analysis and recommendations
- **Budget Tracking**: Create and monitor budgets
- **Responsive Design**: Beautiful UI with Tailwind CSS
- **Data Visualization**: Charts and graphs using Recharts

## Tech Stack

- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Firebase Auth
- Recharts
- Axios

## Setup

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Configure Firebase**:
   Create `src/lib/firebase.ts` with your Firebase config

3. **Set environment variables**:
   Create `.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:3001
   NEXT_PUBLIC_FIREBASE_API_KEY=your_api_key
   NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your_auth_domain
   NEXT_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
   ```

4. **Run development server**:
   ```bash
   npm run dev
   ```

   App runs on http://localhost:3002

## Pages

- `/` - Landing page
- `/dashboard` - Main dashboard with accounts and transactions
- `/transactions` - Transaction history and filtering
- `/budgets` - Budget management
- `/analytics` - Insights and predictions
- `/settings` - Account settings

## License

MIT


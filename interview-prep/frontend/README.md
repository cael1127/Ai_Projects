# Interview Prep Tool - Frontend

Modern Next.js frontend for the AI-powered interview preparation tool.

## Features

- **Modern UI**: Built with Next.js 14, TypeScript, and Tailwind CSS
- **Component Library**: Using shadcn/ui for beautiful, accessible components
- **Google OAuth**: Seamless authentication with Google
- **Interview Management**: Create, view, and manage interviews
- **AI Questions**: Generate and practice with AI-powered questions
- **Calendar Integration**: View and manage prep sessions
- **Analytics Dashboard**: Track your preparation progress

## Tech Stack

- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui components
- Axios for API calls
- date-fns for date formatting
- Recharts for data visualization

## Setup

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Set up environment variables**:
   Create a `.env.local` file:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

3. **Run development server**:
   ```bash
   npm run dev
   ```

   The app will be available at http://localhost:3000

## Project Structure

```
src/
├── app/                    # Next.js app router pages
│   ├── auth/              # Authentication pages
│   ├── dashboard/         # Dashboard page
│   ├── interviews/        # Interview management pages
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Landing page
├── components/            # React components
│   └── ui/               # shadcn/ui components
├── lib/                  # Utilities
│   ├── api.ts           # API client
│   └── utils.ts         # Helper functions
└── styles/              # Global styles
```

## Key Pages

- `/` - Landing page
- `/auth/login` - Login page
- `/auth/register` - Registration page
- `/dashboard` - Main dashboard
- `/interviews` - Interview list
- `/interviews/[id]` - Interview details with questions
- `/analytics` - Performance analytics

## API Integration

The frontend communicates with the FastAPI backend through the API client in `src/lib/api.ts`. All endpoints are typed and include:

- Authentication (login, register, OAuth)
- Interview management (CRUD operations)
- Question generation
- Prep session management
- Analytics and performance tracking

## Authentication

The app supports two authentication methods:

1. **Email/Password**: Traditional authentication
2. **Google OAuth**: One-click sign in with Gmail integration

Tokens are stored in localStorage and automatically attached to API requests.

## Development

### Adding New Components

```bash
# Components use shadcn/ui
npx shadcn-ui@latest add [component-name]
```

### Code Style

- Use TypeScript for type safety
- Follow Next.js app router conventions
- Use Tailwind CSS for styling
- Keep components small and focused

## Building for Production

```bash
npm run build
npm start
```

## Environment Variables

- `NEXT_PUBLIC_API_URL`: Backend API URL (default: http://localhost:8000)

## License

MIT


# AI Job Applier - Frontend

Modern React interface for automated job applications.

## Features

- **Profile Builder**: Create comprehensive profile with skills, experience, education
- **Job Import**: Import jobs from URLs or add manually
- **Application Queue**: Manage jobs to apply to
- **Auto-Apply**: One-click batch application
- **Resume Generator**: AI-generated tailored resumes
- **Cover Letter Generator**: AI-generated personalized cover letters
- **Application Tracker**: Monitor status of all applications
- **Response Tracking**: View recruiter responses from Gmail
- **Analytics Dashboard**: Track conversion rates, response rates, interview pipeline
- **Application History**: Complete history with timeline

## Tech Stack

- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Axios
- Recharts (analytics)
- React Markdown

## Setup

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Configure environment**:
   Create `.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8001
   ```

3. **Run development server**:
   ```bash
   npm run dev
   ```

   App runs on http://localhost:3003

## Pages

- `/` - Landing page
- `/auth/login` - Login
- `/auth/register` - Register
- `/dashboard` - Main dashboard
- `/profile` - Edit profile
- `/jobs` - Browse and import jobs
- `/applications` - Application tracker
- `/resumes` - Resume management
- `/analytics` - Statistics and insights

## Key Features

### Profile Management
Complete profile with:
- Personal information
- Work experience
- Education
- Skills
- Certifications
- Links (LinkedIn, GitHub, Portfolio)

### Job Import
Import jobs from:
- URL (auto-scrape)
- Manual entry
- Batch import from spreadsheet

### Auto-Application
- Select jobs to apply to
- Review generated resumes/cover letters
- Apply with one click
- Monitor progress in real-time

### Analytics
Track:
- Total applications
- Response rate
- Interview conversion rate
- Average response time
- Application timeline

## License

MIT


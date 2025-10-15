# AI Job Applier - Backend

Automate job applications with AI-generated resumes and cover letters, plus browser automation.

## Features

- **Browser Automation**: Uses Playwright to auto-fill job applications
- **AI Resume Generation**: Tailored resumes for each job using OpenAI
- **AI Cover Letters**: Personalized cover letters per application
- **Gmail Integration**: Track recruiter responses automatically
- **Application Tracking**: Monitor all applications and their status
- **Job Board Support**: LinkedIn, Indeed, Greenhouse, and custom sites
- **Analytics**: Track conversion rates, response rates, interview pipeline
- **Mock Mode**: Test without real browser automation

## Tech Stack

- FastAPI
- PostgreSQL with SQLAlchemy ORM
- Playwright (browser automation)
- OpenAI GPT-4 (resume/cover letter generation)
- Gmail API (response tracking)
- Celery (background tasks)

## Setup

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis (for Celery)

### Installation

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

4. **Set up environment variables**:
   Copy `.env.example` to `.env` and configure

5. **Create database**:
   ```bash
   createdb job_applier
   ```

6. **Run migrations**:
   ```bash
   alembic upgrade head
   ```

### Running

**Development**:
```bash
uvicorn app.main:app --reload --port 8001
```

**Production**:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001 --workers 4
```

**Background Worker** (for automated applications):
```bash
celery -A app.tasks worker --loglevel=info
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Get current user

### User Profile
- `GET /api/profile` - Get user profile
- `PUT /api/profile` - Update profile
- `POST /api/profile/education` - Add education
- `POST /api/profile/experience` - Add work experience

### Jobs
- `GET /api/jobs` - List jobs
- `POST /api/jobs` - Add new job
- `GET /api/jobs/{id}` - Get job details
- `POST /api/jobs/import` - Import job from URL
- `DELETE /api/jobs/{id}` - Delete job

### Applications
- `GET /api/applications` - List all applications
- `GET /api/applications/{id}` - Get application details
- `POST /api/applications` - Create application
- `POST /api/applications/{id}/apply` - Apply to job (automation)
- `PUT /api/applications/{id}/status` - Update status

### Resumes
- `GET /api/resumes` - List resumes
- `POST /api/resumes/generate` - Generate AI resume for job
- `GET /api/resumes/{id}` - Get resume content
- `PUT /api/resumes/{id}` - Update resume

### Cover Letters
- `POST /api/cover-letters/generate` - Generate AI cover letter
- `GET /api/cover-letters/{id}` - Get cover letter

### Analytics
- `GET /api/analytics/dashboard` - Dashboard stats
- `GET /api/analytics/conversion` - Conversion rates
- `GET /api/analytics/responses` - Response statistics
- `GET /api/analytics/timeline` - Application timeline

### Gmail Sync
- `POST /api/gmail/sync` - Sync recruiter responses
- `GET /api/responses` - Get all responses

## Browser Automation

### Supported Platforms
- LinkedIn Easy Apply
- Indeed Quick Apply
- Greenhouse ATS
- Generic job boards

### Mock Mode
Set `MOCK_AUTOMATION=True` in `.env` to simulate applications without real browser automation. Useful for:
- Testing
- Development
- Demos
- Rate limiting compliance

### Customization
To add support for new job boards, extend `AutomationService` in `app/services/automation_service.py`.

## AI Features

### Resume Generation
- Analyzes job description
- Highlights relevant skills and experience
- Uses ATS-friendly formatting
- Includes keywords from job posting

### Cover Letter Generation
- Personalized for each company
- Addresses specific requirements
- Professional tone
- Compelling narrative

### Job Fit Analysis
- Match score (0-100)
- Identifies strengths
- Highlights gaps
- Application recommendation

## Database Models

- **User**: User accounts
- **UserProfile**: Detailed profile with skills, experience, education
- **Job**: Job postings
- **Application**: Application records with status
- **Resume**: Generated and template resumes
- **CoverLetter**: Generated cover letters
- **RecruiterResponse**: Tracked responses from Gmail
- **ApplicationLog**: Audit log of application actions

## Environment Variables

Key variables:
- `DATABASE_URL`: PostgreSQL connection
- `OPENAI_API_KEY`: OpenAI API key
- `GMAIL_CLIENT_ID`: Gmail OAuth client ID
- `GMAIL_CLIENT_SECRET`: Gmail OAuth secret
- `SECRET_KEY`: JWT secret
- `HEADLESS_BROWSER`: Run browser in headless mode
- `MOCK_AUTOMATION`: Enable mock automation mode

## Best Practices

1. **Rate Limiting**: Avoid applying to too many jobs simultaneously
2. **Quality Over Quantity**: Review and customize each application
3. **Track Responses**: Regularly sync Gmail to track replies
4. **Update Profile**: Keep skills and experience current
5. **Mock Mode**: Test new job boards in mock mode first

## Deployment

1. Set production environment variables
2. Use production database
3. Set `DEBUG=False`
4. Enable HTTPS
5. Use proper WSGI server (Gunicorn)
6. Set up Redis for Celery
7. Configure proper logging
8. Set up monitoring

## License

MIT


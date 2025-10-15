# Interview Prep Tool - Backend

AI-powered interview preparation tool with Gmail and Google Calendar integration.

## Features

- **OAuth 2.0 Authentication**: Secure Google OAuth integration for Gmail and Calendar access
- **Email Parsing**: Automatically detect interview invitations from Gmail
- **AI Question Generation**: Generate tailored interview questions using OpenAI
- **Calendar Integration**: Auto-schedule prep sessions in Google Calendar
- **Performance Tracking**: Track preparation progress and interview outcomes
- **Analytics Dashboard**: View statistics and success rates

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT + Google OAuth 2.0
- **AI**: OpenAI GPT-4
- **APIs**: Gmail API, Google Calendar API
- **Task Queue**: Celery with Redis

## Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Redis (optional, for Celery)

### Installation

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Configure Google OAuth**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable Gmail API and Google Calendar API
   - Create OAuth 2.0 credentials
   - Add authorized redirect URIs: `http://localhost:3000/auth/callback`
   - Copy Client ID and Client Secret to `.env`

5. **Set up OpenAI API**:
   - Get API key from [OpenAI Platform](https://platform.openai.com/)
   - Add to `.env` file

6. **Create database**:
   ```bash
   createdb interview_prep
   ```

7. **Run migrations** (if using Alembic):
   ```bash
   alembic upgrade head
   ```

### Using Docker

```bash
docker-compose up -d
```

This will start:
- PostgreSQL database on port 5432
- Redis on port 6379
- API server on port 8000

## Running the Application

### Development Mode

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login with email/password
- `GET /api/auth/google/login` - Initiate Google OAuth
- `POST /api/auth/google/callback` - Handle OAuth callback
- `GET /api/auth/me` - Get current user

### Interviews

- `GET /api/interviews` - List all interviews
- `GET /api/interviews/{id}` - Get interview details with questions
- `POST /api/interviews` - Create new interview
- `PUT /api/interviews/{id}` - Update interview
- `DELETE /api/interviews/{id}` - Delete interview
- `POST /api/interviews/{id}/questions` - Generate AI questions
- `POST /api/interviews/sync-from-gmail` - Sync from Gmail
- `POST /api/interviews/{id}/schedule-prep` - Schedule prep sessions

### Prep Sessions

- `GET /api/prep-sessions` - List prep sessions
- `GET /api/prep-sessions/{id}` - Get session details
- `POST /api/prep-sessions` - Create prep session
- `PUT /api/prep-sessions/{id}` - Update prep session
- `POST /api/prep-sessions/{id}/start` - Start session
- `POST /api/prep-sessions/{id}/complete` - Complete session

### Analytics

- `GET /api/analytics/dashboard` - Dashboard statistics
- `GET /api/analytics/performance/{interview_id}` - Interview performance
- `POST /api/analytics/performance` - Create performance record
- `PUT /api/analytics/performance/{interview_id}` - Update performance

## Mock Mode

The application includes a mock mode for development without real API keys:

Set `MOCK_MODE=True` in `.env` to use:
- Mock Gmail email parsing
- Mock Calendar event creation
- Still requires OpenAI key for question generation

## Database Models

- **User**: User accounts with OAuth credentials
- **Interview**: Interview details and scheduling
- **Question**: AI-generated interview questions
- **PrepSession**: Scheduled preparation sessions
- **Performance**: Interview outcomes and metrics

## Environment Variables

See `.env.example` for all configuration options.

Key variables:
- `DATABASE_URL`: PostgreSQL connection string
- `OPENAI_API_KEY`: OpenAI API key
- `GOOGLE_CLIENT_ID`: Google OAuth Client ID
- `GOOGLE_CLIENT_SECRET`: Google OAuth Client Secret
- `SECRET_KEY`: JWT secret key
- `MOCK_MODE`: Enable/disable mock APIs

## Security

- Passwords hashed with bcrypt
- JWT tokens for session management
- OAuth 2.0 for Google integration
- CORS configuration for frontend
- SQL injection prevention via SQLAlchemy
- Input validation with Pydantic

## Development

### Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "description"
```

Apply migrations:
```bash
alembic upgrade head
```

### Testing

```bash
pytest
```

## Deployment

1. Set production environment variables
2. Set `DEBUG=False`
3. Use a production-grade WSGI server (e.g., Gunicorn)
4. Enable HTTPS
5. Set up proper database backups
6. Configure monitoring and logging

## License

MIT


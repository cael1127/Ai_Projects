# Quick Setup Guide for All Three Projects

This guide will help you get all three projects running quickly.

## Prerequisites Checklist

### Required for All Projects
- [ ] Node.js 18+ installed
- [ ] Python 3.11+ installed
- [ ] PostgreSQL 15+ installed
- [ ] Git installed
- [ ] Code editor (VS Code recommended)

### API Keys Required
- [ ] OpenRouter API Key (required for all projects - using Chimera)
  - Your key: `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`
  - Dashboard: https://openrouter.ai/
  - This gives you access to GPT-4o, Claude, and other models!

### Optional API Keys (Projects work in MOCK mode without these)
- [ ] Google Cloud credentials (for Interview Prep)
- [ ] Firebase credentials (for Banking App)
- [ ] Plaid credentials (for Banking App - sandbox available)

## Database Setup

Create three PostgreSQL databases:

```bash
# Using psql or your preferred method
createdb interview_prep
createdb banking_app
createdb job_applier
```

Or with SQL:
```sql
CREATE DATABASE interview_prep;
CREATE DATABASE banking_app;
CREATE DATABASE job_applier;
```

## Project 1: Interview Prep Tool

### Backend Setup

```bash
cd interview-prep/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (copy from .env.example and fill in values)
# At minimum, set:
# - DATABASE_URL=postgresql://postgres:password@localhost:5432/interview_prep
# - OPENAI_API_KEY=your_key_here
# - SECRET_KEY=some_random_string
# - MOCK_MODE=True (to test without Gmail/Calendar)

# Run the server
uvicorn app.main:app --reload
```

**Backend will run on**: http://localhost:8000

### Frontend Setup

Open a new terminal:

```bash
cd interview-prep/frontend

# Install dependencies
npm install

# Create .env.local file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Run the development server
npm run dev
```

**Frontend will run on**: http://localhost:3000

### Test Interview Prep

1. Open http://localhost:3000
2. Register a new account
3. With MOCK_MODE=True, you can test all features without real API keys
4. The app will show mock interview data

---

## Project 2: AI-Powered Banking App

### Backend Setup

```bash
cd banking-app/backend

# Install dependencies
npm install

# Create .env file with at minimum:
# - DATABASE_URL=postgresql://postgres:password@localhost:5432/banking_app
# - OPENAI_API_KEY=your_key_here
# - JWT_SECRET=some_random_string
# - MOCK_PLAID=true
# - FIREBASE_PROJECT_ID=demo-project (can be dummy in mock mode)
# - FIREBASE_PRIVATE_KEY=dummy (can be dummy in mock mode)
# - FIREBASE_CLIENT_EMAIL=dummy@example.com (can be dummy in mock mode)

# Generate Prisma client
npx prisma generate

# Push database schema
npx prisma db push

# Run the server
npm run dev
```

**Backend will run on**: http://localhost:3001

### Web Frontend Setup

Open a new terminal:

```bash
cd banking-app/web

# Install dependencies
npm install

# Create .env.local file
# Add Firebase config (can use demo values for testing)

# Run the development server
npm run dev
```

**Web will run on**: http://localhost:3002

### Mobile App Setup (Optional)

```bash
cd banking-app/mobile

# Install dependencies
npm install

# Start Expo
npm start

# Then:
# - Press 'i' for iOS simulator
# - Press 'a' for Android emulator
# - Scan QR code with Expo Go app on your phone
```

### Test Banking App

1. Open http://localhost:3002
2. With MOCK_PLAID=true, you'll see mock bank accounts and transactions
3. All AI features will work with real OpenAI API

---

## Project 3: AI Job Applier

### Backend Setup

```bash
cd job-applier/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Create .env file with at minimum:
# - DATABASE_URL=postgresql://postgres:password@localhost:5432/job_applier
# - OPENAI_API_KEY=your_key_here
# - SECRET_KEY=some_random_string
# - MOCK_AUTOMATION=True (to test without real browser automation)

# Run the server
uvicorn app.main:app --reload --port 8001
```

**Backend will run on**: http://localhost:8001

### Frontend Setup

Open a new terminal:

```bash
cd job-applier/frontend

# Install dependencies
npm install

# Create .env.local file
echo "NEXT_PUBLIC_API_URL=http://localhost:8001" > .env.local

# Run the development server
npm run dev
```

**Frontend will run on**: http://localhost:3003

### Test Job Applier

1. Open http://localhost:8003
2. With MOCK_AUTOMATION=True, applications will be simulated
3. AI resume/cover letter generation will work with real OpenAI API

---

## Running All Projects Simultaneously

You'll need **6 terminals** (or use tmux/screen):

**Terminal 1**: Interview Prep Backend
```bash
cd interview-prep/backend
venv\Scripts\activate  # or source venv/bin/activate
uvicorn app.main:app --reload
```

**Terminal 2**: Interview Prep Frontend
```bash
cd interview-prep/frontend
npm run dev
```

**Terminal 3**: Banking Backend
```bash
cd banking-app/backend
npm run dev
```

**Terminal 4**: Banking Web
```bash
cd banking-app/web
npm run dev
```

**Terminal 5**: Job Applier Backend
```bash
cd job-applier/backend
venv\Scripts\activate  # or source venv/bin/activate
uvicorn app.main:app --reload --port 8001
```

**Terminal 6**: Job Applier Frontend
```bash
cd job-applier/frontend
npm run dev
```

### Access Points

- Interview Prep: http://localhost:3000 (frontend) + http://localhost:8000 (API)
- Banking App: http://localhost:3002 (web) + http://localhost:3001 (API)
- Job Applier: http://localhost:3003 (frontend) + http://localhost:8001 (API)

---

## Common Issues & Solutions

### Database Connection Issues

**Error**: "connection refused" or "password authentication failed"

**Solution**: Check your DATABASE_URL in .env files matches your PostgreSQL setup.

### Port Already in Use

**Error**: "Address already in use"

**Solution**: 
- Change the port in the command
- Or kill the process using that port

### Missing Dependencies

**Error**: Module not found

**Solution**: 
- Make sure you ran `npm install` or `pip install -r requirements.txt`
- Try deleting node_modules and running `npm install` again

### OpenAI API Errors

**Error**: "Invalid API key"

**Solution**: 
- Verify your OPENAI_API_KEY in .env files
- Make sure you have credits in your OpenAI account

### Playwright Installation Issues

**Error**: "Executable doesn't exist"

**Solution**: 
```bash
playwright install
```

---

## Mock Mode Testing

All projects support mock modes for testing without external APIs:

- **Interview Prep**: Set `MOCK_MODE=True` - generates mock interviews and emails
- **Banking App**: Set `MOCK_PLAID=true` - generates mock bank accounts and transactions  
- **Job Applier**: Set `MOCK_AUTOMATION=True` - simulates job applications without browser

This allows you to test the full application flow with just an OpenAI API key!

---

## Next Steps

1. **Explore the APIs**: Visit `/docs` on each backend for interactive API documentation
   - http://localhost:8000/docs (Interview Prep)
   - http://localhost:8001/docs (Job Applier)

2. **Check the READMEs**: Each project has detailed documentation
   - `interview-prep/backend/README.md`
   - `interview-prep/frontend/README.md`
   - `banking-app/backend/README.md`
   - etc.

3. **Configure Real APIs**: When ready, get real API credentials and set mock modes to False

4. **Deploy**: Check individual project READMEs for deployment guides

---

## Quick Test Checklist

- [ ] All databases created
- [ ] All backends running without errors
- [ ] All frontends loading in browser
- [ ] Can register/login on Interview Prep
- [ ] Can see mock data in Banking App
- [ ] Job Applier API responding at /health endpoint
- [ ] OpenAI integration working (test AI features)

---

## Support

If you encounter issues:
1. Check the error messages carefully
2. Review the project-specific README files
3. Ensure all environment variables are set
4. Verify all dependencies are installed
5. Check that databases are running and accessible

**API Documentation**:
- FastAPI projects: Visit `http://localhost:PORT/docs`
- All endpoints and their parameters are documented there

---

**Happy coding! 🚀**


# 🚀 Quick Start - Get All Three Projects Running

## 📋 Prerequisites (5 minutes)

1. ✅ PostgreSQL installed and running
2. ✅ Python 3.11+ installed
3. ✅ Node.js 18+ installed
4. ✅ Your OpenRouter API key ready

---

## 🔑 Step 1: Create .env Files (2 minutes)

### Interview Prep Backend
Create `interview-prep/backend/.env`:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/interview_prep
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=change-me-in-production
MOCK_MODE=True
```

### Banking App Backend
Create `banking-app/backend/.env`:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/banking_app
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
JWT_SECRET=change-me-in-production
MOCK_PLAID=true
FIREBASE_PROJECT_ID=demo-project
FIREBASE_PRIVATE_KEY=dummy
FIREBASE_CLIENT_EMAIL=demo@example.com
```

### Job Applier Backend
Create `job-applier/backend/.env`:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/job_applier
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=change-me-in-production
MOCK_AUTOMATION=True
```

### Frontend .env Files
Create `interview-prep/frontend/.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Create `banking-app/web/.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:3001
```

Create `job-applier/frontend/.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8001
```

---

## 💾 Step 2: Create Databases (1 minute)

```bash
createdb interview_prep
createdb banking_app
createdb job_applier
```

---

## 🎯 Step 3: Run Project 1 - Interview Prep

### Terminal 1: Backend
```bash
cd interview-prep/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
✅ Running on http://localhost:8000

### Terminal 2: Frontend
```bash
cd interview-prep/frontend
npm install
npm run dev
```
✅ Running on http://localhost:3000

**Test**: Open http://localhost:3000

---

## 💰 Step 4: Run Project 2 - Banking App

### Terminal 3: Backend
```bash
cd banking-app/backend
npm install
npx prisma generate
npx prisma db push
npm run dev
```
✅ Running on http://localhost:3001

### Terminal 4: Frontend
```bash
cd banking-app/web
npm install
npm run dev
```
✅ Running on http://localhost:3002

**Test**: Open http://localhost:3002

---

## 🤖 Step 5: Run Project 3 - Job Applier

### Terminal 5: Backend
```bash
cd job-applier/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
uvicorn app.main:app --reload --port 8001
```
✅ Running on http://localhost:8001

### Terminal 6: Frontend
```bash
cd job-applier/frontend
npm install
npm run dev
```
✅ Running on http://localhost:3003

**Test**: Open http://localhost:3003

---

## ✅ Verification Checklist

- [ ] Interview Prep backend: http://localhost:8000/health returns `{"status":"healthy"}`
- [ ] Interview Prep frontend: http://localhost:3000 loads
- [ ] Banking backend: http://localhost:3001/health returns `{"status":"healthy"}`
- [ ] Banking frontend: http://localhost:3002 loads
- [ ] Job Applier backend: http://localhost:8001/health returns `{"status":"healthy"}`
- [ ] Job Applier frontend: http://localhost:3003 loads

---

## 🎨 What You Can Do Now

### Interview Prep (Port 3000)
1. Register an account
2. View mock interviews
3. Generate AI questions (uses OpenRouter!)
4. See mock calendar events

### Banking App (Port 3002)
1. View mock bank accounts
2. See 50+ mock transactions
3. Watch AI categorize spending (uses OpenRouter!)
4. View financial insights

### Job Applier (Port 3003)
1. Build your profile
2. Add jobs
3. Generate AI resumes (uses OpenRouter!)
4. Generate AI cover letters (uses OpenRouter!)
5. Simulate applications

---

## 🔍 API Documentation

- Interview Prep: http://localhost:8000/docs
- Job Applier: http://localhost:8001/docs

---

## 🆘 Common Issues

### "Connection refused" error
→ Make sure PostgreSQL is running

### "Module not found" error
→ Run `npm install` or `pip install -r requirements.txt`

### "Port already in use"
→ Kill the process or change the port

### OpenAI API errors
→ Check your `OPENAI_API_KEY` in .env files

---

## 📊 Your API Key

Using OpenRouter (Chimera):
```
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
```

This key gives you access to:
- ✅ GPT-4o
- ✅ GPT-4 Turbo
- ✅ Claude 3
- ✅ And more models!

Track usage at: https://openrouter.ai/

---

## 🎉 That's It!

All three AI projects are now running with OpenRouter integration!

**Next**: Start exploring the features and test the AI functionality!


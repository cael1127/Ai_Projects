# 🚀 START HERE - Simple Manual Setup

## ✅ What You Have So Far

- ✅ Python 3.14.0 installed (use `py` command)
- ✅ Node.js v22.17.0 installed
- ✅ PostgreSQL 15.14 installed  
- ✅ Git v2.50.0 installed
- ✅ Interview Prep backend dependencies INSTALLED
- ✅ Interview Prep backend .env file CREATED
- ✅ Interview Prep backend RUNNING in background

---

## 📝 Step 1: Create the Three Databases

Open a **NEW PowerShell window** and run these commands one at a time:

```powershell
# You'll be prompted for PostgreSQL password (the one you set during installation)

& "C:\Program Files\PostgreSQL\15\bin\createdb.exe" -U postgres interview_prep

& "C:\Program Files\PostgreSQL\15\bin\createdb.exe" -U postgres banking_app

& "C:\Program Files\PostgreSQL\15\bin\createdb.exe" -U postgres job_applier
```

**Or use pgAdmin (GUI):**
1. Open pgAdmin
2. Connect to PostgreSQL server
3. Right-click "Databases" → "Create" → "Database"
4. Create: `interview_prep`, `banking_app`, `job_applier`

---

## 📝 Step 2: Create Remaining .env Files

Run this in PowerShell (in C:\Users\caelf\AiProjects):

```powershell
# Get your PostgreSQL password
$pgPass = Read-Host "Enter your PostgreSQL password" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pgPass)
$pgPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
$dbUrl = "postgresql://postgres:${pgPassword}@localhost:5432"

# Interview Prep Frontend
"NEXT_PUBLIC_API_URL=http://localhost:8000" | Out-File -FilePath "interview-prep\frontend\.env.local" -Encoding UTF8

# Banking Backend
@"
PORT=3001
NODE_ENV=development
DATABASE_URL=${dbUrl}/banking_app
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
JWT_SECRET=banking-secret
MOCK_PLAID=true
FIREBASE_PROJECT_ID=demo
FIREBASE_PRIVATE_KEY=dummy
FIREBASE_CLIENT_EMAIL=demo@demo.com
"@ | Out-File -FilePath "banking-app\backend\.env" -Encoding UTF8

# Banking Web
"NEXT_PUBLIC_API_URL=http://localhost:3001" | Out-File -FilePath "banking-app\web\.env.local" -Encoding UTF8

# Job Applier Backend
@"
DATABASE_URL=${dbUrl}/job_applier
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=job-applier-secret
MOCK_AUTOMATION=True
"@ | Out-File -FilePath "job-applier\backend\.env" -Encoding UTF8

# Job Applier Frontend
"NEXT_PUBLIC_API_URL=http://localhost:8001" | Out-File -FilePath "job-applier\frontend\.env.local" -Encoding UTF8

Write-Host "[OK] All .env files created!" -ForegroundColor Green
```

---

## 📝 Step 3: Check Interview Prep Backend

The backend should be running. Test it:

```powershell
# Open in browser:
start http://localhost:8000/docs
```

You should see the API documentation!

---

## 📝 Step 4: Start Interview Prep Frontend

Open a **NEW terminal** and run:

```powershell
cd C:\Users\caelf\AiProjects\interview-prep\frontend
npm install
npm run dev
```

Then visit: http://localhost:3000

---

## 📝 Step 5: Start Banking App (Optional)

### Backend (Terminal 3):
```powershell
cd C:\Users\caelf\AiProjects\banking-app\backend
npm install
npx prisma generate
npx prisma db push
npm run dev
```

### Frontend (Terminal 4):
```powershell
cd C:\Users\caelf\AiProjects\banking-app\web
npm install
npm run dev
```

Visit: http://localhost:3002

---

## 📝 Step 6: Start Job Applier (Optional)

### Backend (Terminal 5):
```powershell
cd C:\Users\caelf\AiProjects\job-applier\backend
py -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy alembic python-dotenv openai==1.3.0 httpx python-multipart pydantic-settings psycopg2-binary python-jose[cryptography] passlib[bcrypt]
pip install playwright
playwright install
uvicorn app.main:app --reload --port 8001
```

### Frontend (Terminal 6):
```powershell
cd C:\Users\caelf\AiProjects\job-applier\frontend
npm install
npm run dev
```

Visit: http://localhost:8003

---

## ✅ Quick Checklist

- [ ] Three databases created (interview_prep, banking_app, job_applier)
- [ ] All .env files created
- [ ] Interview Prep backend running on port 8000
- [ ] Interview Prep frontend running on port 3000
- [ ] Can access http://localhost:3000

---

## 🎉 Your First Test

1. Visit: http://localhost:3000
2. Click "Register" or "Sign up"
3. Create an account
4. You should see the dashboard with mock interviews!

---

## 🆘 If Something Doesn't Work

### Backend won't start
- Check the .env file exists: `ls interview-prep\backend\.env`
- Check PostgreSQL is running: `& "C:\Program Files\PostgreSQL\15\bin\pg_isready.exe"`
- Look at the error messages in the terminal

### Frontend won't start
- Make sure Node.js is working: `node --version`
- Try deleting node_modules and reinstalling: `rm -r node_modules; npm install`

### Can't connect to database
- Update your DATABASE_URL in .env with your actual PostgreSQL password
- Test connection: `& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -d interview_prep -c "SELECT 1;"`

---

## 🎯 Summary

**You're on Step 1!** Create the databases, then follow the rest of the steps above.

The Interview Prep backend is already running - you're almost there! 🚀


# 🔐 Creating Your .env Files - Safe Environment Variables

## ✅ Security Features Already Implemented

- ✅ All projects use `.env` files (never committed to git)
- ✅ No API keys are hardcoded in any code
- ✅ All sensitive data loaded from environment variables
- ✅ `.gitignore` files protect your secrets

---

## 📝 Step-by-Step: Create Your .env Files

### Quick Setup (Windows PowerShell)

Run these commands from the `AiProjects` directory:

```powershell
# 1. Interview Prep Backend
@"
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/interview_prep
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=interview-prep-secret-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=Interview Prep Tool
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3000
MOCK_MODE=True
REDIS_URL=redis://localhost:6379/0
"@ | Out-File -FilePath "interview-prep\backend\.env" -Encoding UTF8

# 2. Interview Prep Frontend
@"
NEXT_PUBLIC_API_URL=http://localhost:8000
"@ | Out-File -FilePath "interview-prep\frontend\.env.local" -Encoding UTF8

# 3. Banking App Backend
@"
PORT=3001
NODE_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/banking_app
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
JWT_SECRET=banking-app-secret-change-in-production
MOCK_PLAID=true
FIREBASE_PROJECT_ID=demo-project
FIREBASE_PRIVATE_KEY=dummy
FIREBASE_CLIENT_EMAIL=demo@example.com
PLAID_CLIENT_ID=dummy
PLAID_SECRET=dummy
PLAID_ENV=sandbox
"@ | Out-File -FilePath "banking-app\backend\.env" -Encoding UTF8

# 4. Banking Web Frontend
@"
NEXT_PUBLIC_API_URL=http://localhost:3001
NEXT_PUBLIC_FIREBASE_API_KEY=demo-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=demo.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=demo-project
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=demo.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456:web:abc123
"@ | Out-File -FilePath "banking-app\web\.env.local" -Encoding UTF8

# 5. Job Applier Backend
@"
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/job_applier
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=job-applier-secret-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=AI Job Applier
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3003
HEADLESS_BROWSER=True
MOCK_AUTOMATION=True
REDIS_URL=redis://localhost:6379/0
"@ | Out-File -FilePath "job-applier\backend\.env" -Encoding UTF8

# 6. Job Applier Frontend
@"
NEXT_PUBLIC_API_URL=http://localhost:8001
"@ | Out-File -FilePath "job-applier\frontend\.env.local" -Encoding UTF8

Write-Host "✅ All .env files created successfully!" -ForegroundColor Green
Write-Host "Your API keys are now safely stored in git-ignored .env files" -ForegroundColor Green
```

---

## 🖥️ Manual Creation (Any Platform)

If you prefer to create them manually, here are the exact contents:

### 1️⃣ `interview-prep/backend/.env`

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/interview_prep
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=interview-prep-secret-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=Interview Prep Tool
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3000
MOCK_MODE=True
REDIS_URL=redis://localhost:6379/0
```

### 2️⃣ `interview-prep/frontend/.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3️⃣ `banking-app/backend/.env`

```env
PORT=3001
NODE_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/banking_app
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
JWT_SECRET=banking-app-secret-change-in-production
MOCK_PLAID=true
FIREBASE_PROJECT_ID=demo-project
FIREBASE_PRIVATE_KEY=dummy
FIREBASE_CLIENT_EMAIL=demo@example.com
PLAID_CLIENT_ID=dummy
PLAID_SECRET=dummy
PLAID_ENV=sandbox
```

### 4️⃣ `banking-app/web/.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:3001
NEXT_PUBLIC_FIREBASE_API_KEY=demo-key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=demo.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=demo-project
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=demo.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456:web:abc123
```

### 5️⃣ `job-applier/backend/.env`

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/job_applier
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=job-applier-secret-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=AI Job Applier
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3003
HEADLESS_BROWSER=True
MOCK_AUTOMATION=True
REDIS_URL=redis://localhost:6379/0
```

### 6️⃣ `job-applier/frontend/.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8001
```

---

## 🔐 Security Verification

### Check that .env files are protected:

```powershell
# These should all be listed (means they're git-ignored)
git check-ignore interview-prep/backend/.env
git check-ignore interview-prep/frontend/.env.local
git check-ignore banking-app/backend/.env
git check-ignore banking-app/web/.env.local
git check-ignore job-applier/backend/.env
git check-ignore job-applier/frontend/.env.local
```

If they're all ignored, you're secure! ✅

---

## 📍 What Each Variable Does

### Database URLs
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/database_name
```
- Format: `postgresql://username:password@host:port/database`
- Change `postgres:postgres` to your PostgreSQL credentials

### OpenRouter API (Your AI Key)
```env
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
```
- This is your OpenRouter/Chimera key
- All AI features use this
- Can switch models easily

### Secret Keys (JWT)
```env
SECRET_KEY=change-me-in-production
JWT_SECRET=change-me-in-production
```
- Used for authentication tokens
- **Must change for production!**
- Generate with: `openssl rand -hex 32`

### Mock Modes
```env
MOCK_MODE=True
MOCK_PLAID=true
MOCK_AUTOMATION=True
```
- Test without real external APIs
- Great for development
- Set to `False` when you have real credentials

---

## ✅ Verification Checklist

After creating the files:

- [ ] 6 `.env` files created
- [ ] No `.env` files show up in `git status`
- [ ] OpenRouter API key is in all backend .env files
- [ ] Database URLs match your PostgreSQL setup
- [ ] Mock modes set to `True` for testing

---

## 🎯 One-Command Setup (Copy & Paste)

Just copy the entire PowerShell script above and paste it into PowerShell in your `AiProjects` directory. It will create all 6 files automatically! 🚀

---

## 🔄 Updating Values Later

To change any value:
1. Open the `.env` file in any text editor
2. Change the value
3. Restart the backend server
4. Changes take effect immediately

---

## 📝 Example: Changing PostgreSQL Password

If your PostgreSQL password is different:

**Before:**
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/interview_prep
```

**After:**
```env
DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/interview_prep
```

---

## 🎉 That's It!

Your environment variables are now:
- ✅ Safely stored in `.env` files
- ✅ Git-ignored (never committed)
- ✅ Easy to update
- ✅ Ready to use

**Next**: Run the PowerShell script or manually create the files, then follow `QUICK_START.md`! 🚀


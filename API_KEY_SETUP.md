# API Key Setup Guide - Using OpenRouter (Chimera)

## 🔑 Where to Put API Keys

**IMPORTANT**: Never commit API keys to git! Always use `.env` files.

---

## OpenRouter (Chimera) Configuration

We'll use **OpenRouter** instead of direct OpenAI for all projects. This gives you access to multiple models including GPT-4.

### Your OpenRouter API Key
```
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
```

---

## Project 1: Interview Prep Tool

### Backend: `interview-prep/backend/.env`

Create this file (it's git-ignored):

```env
# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/interview_prep

# OpenRouter API (Chimera)
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o

# Google OAuth (Optional - use mock mode)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:3000/auth/callback

# JWT
SECRET_KEY=interview-prep-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App Settings
APP_NAME=Interview Prep Tool
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3000

# Mock Mode (set to True to test without Gmail/Calendar)
MOCK_MODE=True

# Redis
REDIS_URL=redis://localhost:6379/0
```

### Frontend: `interview-prep/frontend/.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Project 2: Banking App

### Backend: `banking-app/backend/.env`

```env
# Server
PORT=3001
NODE_ENV=development

# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/banking_app

# Supabase (Optional)
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_KEY=your_supabase_service_key

# Firebase (Can use dummy values in mock mode)
FIREBASE_PROJECT_ID=demo-project
FIREBASE_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC\n-----END PRIVATE KEY-----\n
FIREBASE_CLIENT_EMAIL=firebase-adminsdk@demo-project.iam.gserviceaccount.com

# Plaid (Sandbox)
PLAID_CLIENT_ID=your_plaid_client_id
PLAID_SECRET=your_plaid_secret_sandbox
PLAID_ENV=sandbox

# OpenRouter API (Chimera)
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o

# JWT
JWT_SECRET=banking-app-secret-key-change-in-production

# Mock Mode
MOCK_PLAID=true
```

### Web Frontend: `banking-app/web/.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:3001

# Firebase (Can use demo config for testing)
NEXT_PUBLIC_FIREBASE_API_KEY=AIzaSyDemo123456789
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=demo-project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=demo-project
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=demo-project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456789
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456789:web:abc123
```

---

## Project 3: Job Applier

### Backend: `job-applier/backend/.env`

```env
# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/job_applier

# OpenRouter API (Chimera)
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o

# Gmail (Optional - for response tracking)
GMAIL_CLIENT_ID=your_gmail_client_id
GMAIL_CLIENT_SECRET=your_gmail_client_secret
GMAIL_REDIRECT_URI=http://localhost:3003/auth/callback

# JWT
SECRET_KEY=job-applier-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App Settings
APP_NAME=AI Job Applier
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3003

# Automation Settings
HEADLESS_BROWSER=True
MOCK_AUTOMATION=True

# Redis
REDIS_URL=redis://localhost:6379/0
```

### Frontend: `job-applier/frontend/.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8001
```

---

## 🔐 Security Notes

1. **Never commit `.env` files to git**
   - They're already in `.gitignore`
   - Only commit `.env.example` files (without real keys)

2. **Keep API keys secret**
   - Don't share them in public repos
   - Don't paste them in public forums
   - Rotate them if exposed

3. **Use different keys for production**
   - Development: Test keys
   - Production: Separate production keys

---

## ✅ Quick Setup Checklist

For each project, create the `.env` file:

```bash
# Interview Prep Backend
cd interview-prep/backend
# Create .env file with the content above

# Interview Prep Frontend
cd interview-prep/frontend
# Create .env.local file

# Banking Backend
cd banking-app/backend
# Create .env file

# Banking Web
cd banking-app/web
# Create .env.local file

# Job Applier Backend
cd job-applier/backend
# Create .env file

# Job Applier Frontend
cd job-applier/frontend
# Create .env.local file
```

---

## 🧪 Testing OpenRouter Connection

Run this test to verify your OpenRouter key works:

```bash
# Test from any project directory
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
    "model": "openai/gpt-4o",
    "messages": [
      {"role": "user", "content": "Say hello"}
    ]
  }'
```

If you get a response, your key is working! ✅

---

## 🚀 After Creating .env Files

1. **Start the backends** - they'll automatically read the .env files
2. **Test the health endpoints** - make sure everything connects
3. **Try an AI feature** - test that OpenRouter integration works

---

## 📝 Example .env File Creation (Windows)

```powershell
# Interview Prep Backend
cd interview-prep\backend
New-Item -Path .env -ItemType File
# Then copy the content above into it

# Or use echo
@"
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/interview_prep
OPENAI_API_KEY=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
OPENAI_BASE_URL=https://openrouter.ai/api/v1
SECRET_KEY=change-me-in-production
MOCK_MODE=True
"@ | Out-File -FilePath .env -Encoding UTF8
```

---

## 🎯 Summary

- **3 Backend .env files** with OpenRouter config
- **3 Frontend .env.local files** with API URLs  
- **All use the same OpenRouter API key**
- **Base URL**: `https://openrouter.ai/api/v1`
- **Model**: `openai/gpt-4o`

Your API key is ready to use! 🎉


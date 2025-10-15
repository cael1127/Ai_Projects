# 🧪 Test One Project - Interview Prep

## ✅ Prerequisites (You Have These)
- ✅ Python 3.14 (py command)
- ✅ Node.js v22.17
- ✅ PostgreSQL 15.14
- ✅ Dependencies installed in interview-prep/backend
- ✅ .env file created

---

## 🎯 Simple 3-Step Process

### **Step 1: Create Database in pgAdmin** (1 minute)

1. Press **Windows Key**
2. Type **"pgAdmin"**
3. Open it (enter your PostgreSQL password)
4. In the left panel: Right-click **"Databases"**
5. Click **"Create"** → **"Database..."**
6. Name: **`interview_prep`**
7. Click **"Save"**

✅ Database created!

---

### **Step 2: Start Backend** (Terminal 1)

Open PowerShell and run this script:

```powershell
cd C:\Users\caelf\AiProjects
.\RUN_INTERVIEW_PREP_BACKEND.ps1
```

**Wait for**: "Application startup complete" message

**Test it works**: Open http://localhost:8080/docs in your browser
- You should see interactive API documentation
- Try the `/health` endpoint - click "Try it out" → "Execute"
- Should return `{"status": "healthy"}`

✅ Backend working!

---

### **Step 3: Start Frontend** (Terminal 2)

Open a **NEW PowerShell window** and run:

```powershell
cd C:\Users\caelf\AiProjects
.\RUN_INTERVIEW_PREP_FRONTEND.ps1
```

**First time**: npm will install dependencies (2-3 minutes)
**Wait for**: "Ready in X seconds" message

**Test it works**: Open http://localhost:3000 in your browser
- You should see a beautiful landing page
- "Interview Prep" title with features
- "Get Started" and "Sign In" buttons

✅ Frontend working!

---

## 🎉 Test the Complete Flow

1. **Visit**: http://localhost:3000
2. **Click**: "Get Started" or "Sign up"
3. **Register** with:
   - Email: test@example.com
   - Password: password123
   - Name: Test User
4. **Click**: "Create account"
5. **You should see**: Dashboard with mock interview data!

---

## 🔍 What You Should See

### Backend Terminal:
```
INFO:     Will watch for changes in these directories: ['C:\\Users\\caelf\\AiProjects\\interview-prep\\backend']
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [XXXX] using WatchFiles
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Frontend Terminal:
```
   ▲ Next.js 14.1.0
   - Local:        http://localhost:3000

 ✓ Ready in 2.1s
```

### In Browser:
- Beautiful landing page at http://localhost:3000
- Can register and login
- Dashboard shows mock interviews
- Can generate AI questions

---

## 🆘 Troubleshooting

### Backend won't start - "Database connection failed"

**Fix**: Make sure you created the `interview_prep` database in pgAdmin

**Or** update the password in `.env`:
```powershell
# Edit: interview-prep\backend\.env
# Line 1: Change postgres:postgres to postgres:YOUR_ACTUAL_PASSWORD
```

### Frontend - "npm install" fails

**Fix**: Try:
```powershell
cd interview-prep\frontend
Remove-Item node_modules -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item package-lock.json -ErrorAction SilentlyContinue
npm install
```

### "Cannot connect to backend" error in browser

**Fix**: Make sure backend is running and showing "Application startup complete"

---

## ✅ Success Checklist

- [ ] pgAdmin opened and database created
- [ ] Backend script running (Terminal 1)
- [ ] Seeing "Application startup complete"
- [ ] http://localhost:8080/docs shows API documentation
- [ ] Frontend script running (Terminal 2)
- [ ] http://localhost:3000 shows landing page
- [ ] Can register an account
- [ ] Dashboard loads with mock data
- [ ] Can click "Sync Gmail" (shows mock interviews)
- [ ] Can generate AI questions for an interview

---

## 🎯 Your Two Commands

**Terminal 1:**
```powershell
cd C:\Users\caelf\AiProjects
.\RUN_INTERVIEW_PREP_BACKEND.ps1
```

**Terminal 2:**
```powershell
cd C:\Users\caelf\AiProjects
.\RUN_INTERVIEW_PREP_FRONTEND.ps1
```

**That's it!** 🚀

Once this works, we know the setup is correct and can proceed to the other two projects!


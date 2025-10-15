# 🚀 Simple Commands - Copy & Paste

## ⚠️ IMPORTANT: You're Currently in C:\WINDOWS\system32

You need to navigate to your project directory first!

---

## 📍 Step 1: Navigate to Project Directory

**Copy and paste this FIRST:**

```powershell
cd C:\Users\caelf\AiProjects
```

---

## 🗄️ Step 2: Create Databases Using pgAdmin

**Easiest way to avoid password issues:**

1. Press **Windows Key**
2. Type **"pgAdmin"**
3. Open pgAdmin
4. Connect to PostgreSQL (enter your password when prompted)
5. Right-click **"Databases"** → **"Create"** → **"Database"**
6. Name: `interview_prep` → Click **Save**
7. Repeat for: `banking_app`
8. Repeat for: `job_applier`

✅ Done! Three databases created!

---

## 🚀 Step 3: Start Interview Prep Backend

**Terminal 1** (Backend):

```powershell
cd C:\Users\caelf\AiProjects\interview-prep\backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

**Wait for**: "Application startup complete"
**Test in browser**: http://localhost:8000/docs

---

## 🚀 Step 4: Start Interview Prep Frontend

**Terminal 2** (Frontend - open a NEW PowerShell):

```powershell
cd C:\Users\caelf\AiProjects\interview-prep\frontend
npm install
```

Wait for npm install to finish (2-3 minutes), then:

```powershell
npm run dev
```

**Test in browser**: http://localhost:3000

---

## ✅ If Interview Prep Works, You're Done!

You can then:
1. Register an account
2. See mock interviews
3. Generate AI questions
4. Test all features

---

## 🎯 Quick Troubleshooting

### "Cannot find path"
→ You're in the wrong directory. Run: `cd C:\Users\caelf\AiProjects`

### "Password authentication failed"
→ Use pgAdmin to create databases (Step 2 above)

### "uvicorn: command not found"
→ Make sure virtual environment is activated: `.\venv\Scripts\Activate.ps1`

### "Module not found" in Python
→ Make sure you installed dependencies: `pip install -r requirements.txt`

---

## 📋 Complete Command Sequence

**Just copy this entire block** (after creating databases in pgAdmin):

```powershell
# Navigate to project
cd C:\Users\caelf\AiProjects

# Start backend (Terminal 1)
cd interview-prep\backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

**Then in a NEW terminal:**

```powershell
# Start frontend (Terminal 2)
cd C:\Users\caelf\AiProjects\interview-prep\frontend
npm install
npm run dev
```

**Then open**: http://localhost:3000

---

## 🎉 That's It!

Three simple steps:
1. Create databases in pgAdmin
2. Start backend
3. Start frontend

**You're almost there!** 🚀



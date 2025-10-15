# 🚀 FINAL SIMPLE GUIDE - Test Interview Prep

## ✅ Everything is Ready! Just 3 Steps:

---

## 📋 **Step 1: Create Database (1 minute)**

Use pgAdmin (easiest way):

1. **Open pgAdmin** (search in Start Menu)
2. **Enter your PostgreSQL password** to connect
3. **Right-click** "Databases" in left panel
4. **Click** "Create" → "Database..."
5. **Type**: `interview_prep`
6. **Click** "Save"

✅ Done!

**Alternative** (if you know your PostgreSQL password):
```powershell
$env:PGPASSWORD="YOUR_PASSWORD"
& "C:\Program Files\PostgreSQL\15\bin\createdb.exe" -U postgres interview_prep
Remove-Item Env:\PGPASSWORD
```

---

## 🖥️ **Step 2: Start Backend (Terminal 1)**

Open PowerShell in your project directory and run:

```powershell
cd C:\Users\caelf\AiProjects
.\RUN_INTERVIEW_PREP_BACKEND.ps1
```

**Wait for this message:**
```
INFO:     Application startup complete.
```

**Verify it works:**
- Open: http://localhost:8080/docs
- You should see API documentation!

✅ Backend running!

---

## 🌐 **Step 3: Start Frontend (Terminal 2)**

Open a **NEW PowerShell window** and run:

```powershell
cd C:\Users\caelf\AiProjects
.\RUN_INTERVIEW_PREP_FRONTEND.ps1
```

**First time**: npm installs dependencies (2-3 minutes)

**Wait for this message:**
```
✓ Ready in X.Xs
```

**Verify it works:**
- Open: http://localhost:3000
- You should see a beautiful landing page!

✅ Frontend running!

---

## 🎉 **Test the App**

1. Visit: **http://localhost:3000**
2. Click **"Get Started"**
3. Register with:
   - Email: `test@example.com`
   - Password: `password123`
   - Name: `Test User`
4. Click **"Create account"**
5. **Dashboard loads** with mock interviews!
6. Click **"Sync Gmail"** - see mock interviews appear
7. Click an interview → Click **"Generate Questions"**
8. **AI generates interview questions!** (Using your OpenRouter key)

---

## 🔍 **What You Should See:**

### ✅ Backend Terminal:
```
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8080
```

### ✅ Frontend Terminal:
```
▲ Next.js 14.1.0
- Local: http://localhost:3000
✓ Ready in 2.1s
```

### ✅ In Browser:
- Landing page with "Interview Prep" title
- Registration page
- Dashboard with stats
- Mock interviews shown
- AI question generation works

---

## 🆘 **If Something Doesn't Work:**

### Backend Error: "Database connection failed"
**Fix**: Create the database in pgAdmin (Step 1)

### Backend Error: "Port already in use"
**Fix**: I already cleared the ports, but if needed:
```powershell
Get-Process | Where-Object {$_.Name -like "*python*"} | Stop-Process -Force
```

### Frontend Error: "Cannot connect to API"
**Fix**: Make sure backend is running and shows "Application startup complete"

### Frontend Error: npm install fails
**Fix**: Delete node_modules and try again:
```powershell
cd interview-prep\frontend
Remove-Item node_modules -Recurse -Force
npm install
```

---

## 📊 **Ports Used:**
- **Backend**: 8080 (changed from 8000 to avoid conflicts)
- **Frontend**: 3000

---

## ✅ **Success Criteria:**

When everything works:
- [ ] Backend terminal shows "Application startup complete"
- [ ] http://localhost:8080/docs opens
- [ ] Frontend terminal shows "Ready in"
- [ ] http://localhost:3000 opens
- [ ] Can register an account
- [ ] Dashboard loads
- [ ] Can generate AI questions (tests OpenRouter integration!)

---

## 🎯 **Just Run These Two Scripts:**

**Terminal 1:**
```powershell
.\RUN_INTERVIEW_PREP_BACKEND.ps1
```

**Terminal 2 (NEW window):**
```powershell
.\RUN_INTERVIEW_PREP_FRONTEND.ps1
```

**That's literally it!** 🚀

Once this works, we'll know:
- ✅ Database works
- ✅ Python setup works
- ✅ Node.js setup works
- ✅ OpenRouter API key works
- ✅ All configurations are correct

Then the other two projects will be easy! 🎉


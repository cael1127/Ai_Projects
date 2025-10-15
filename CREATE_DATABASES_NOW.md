# Creating Your Three Databases

## ✅ Your Setup Status

- ✅ **Python 3.14.0** installed (use `py` command)
- ✅ **PostgreSQL 15.14** installed
- ✅ **Node.js v22.17.0** installed
- ✅ **Git v2.50.0** installed

**Now you just need to create the three databases!**

---

## 🗄️ Create Databases (3 Commands)

### **Method 1: Direct Commands** (Recommended)

Run these three commands. You'll be prompted for the PostgreSQL password you set during installation:

```powershell
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "CREATE DATABASE interview_prep;"
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "CREATE DATABASE banking_app;"
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "CREATE DATABASE job_applier;"
```

**Password**: Enter the password you set when installing PostgreSQL

---

### **Method 2: Interactive Mode**

```powershell
# Connect to PostgreSQL
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres

# Once connected, type these commands:
CREATE DATABASE interview_prep;
CREATE DATABASE banking_app;
CREATE DATABASE job_applier;

# Verify they were created:
\l

# Exit:
\q
```

---

### **Method 3: Using pgAdmin (GUI)**

If you prefer a visual tool:

1. Open **pgAdmin** (should be installed with PostgreSQL)
2. Connect to your PostgreSQL server
3. Right-click "Databases" → "Create" → "Database"
4. Create these three databases:
   - `interview_prep`
   - `banking_app`
   - `job_applier`

---

## ✅ Verify Databases Were Created

```powershell
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "\l"
```

You should see your three new databases in the list!

---

## 🔑 Update Your Database URLs

In your `.env` files, update the DATABASE_URL with your actual password:

```env
# If your PostgreSQL password is 'mypassword':
DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/interview_prep
```

**Replace `mypassword` with your actual PostgreSQL password!**

---

## 🚀 After Databases Are Created

1. ✅ Create `.env` files → See below for the script
2. ✅ Follow QUICK_START.md to run the projects

---

## 📝 Database Connection Strings

Use these in your `.env` files (update the password):

```env
# Interview Prep
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/interview_prep

# Banking App
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/banking_app

# Job Applier
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/job_applier
```

**Replace `YOUR_PASSWORD` with your actual PostgreSQL password!**


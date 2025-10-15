# Setting Up Python and PostgreSQL in PATH

## ✅ You've Downloaded Python 3.14.0 and PostgreSQL 15.14!

Now we need to add them to your PATH so you can use them from any terminal.

---

## 🔍 Quick Test - Close and Reopen PowerShell

**First, try this simple fix:**

1. **Close this PowerShell window completely**
2. **Open a NEW PowerShell window** (regular user, not admin)
3. **Try these commands:**
   ```powershell
   python --version
   psql --version
   ```

If they work, skip to "Create Databases" below! ✅

---

## 🛠️ If Commands Still Don't Work

### **Option 1: Find and Add to PATH (Easiest)**

Python and PostgreSQL are likely installed here:

**Python**: `C:\Users\caelf\AppData\Local\Programs\Python\Python314\`
**PostgreSQL**: `C:\Program Files\PostgreSQL\15\bin\`

Let's check:

```powershell
# Check if Python exists
Test-Path "C:\Users\caelf\AppData\Local\Programs\Python\Python314\python.exe"

# Check if PostgreSQL exists
Test-Path "C:\Program Files\PostgreSQL\15\bin\psql.exe"
```

### **Option 2: Add to PATH Manually**

1. **Press Win + X**, select "System"
2. Click **"Advanced system settings"**
3. Click **"Environment Variables"**
4. Under **"User variables"**, select **"Path"**, click **"Edit"**
5. Click **"New"** and add these paths (if they exist):
   - `C:\Users\caelf\AppData\Local\Programs\Python\Python314\`
   - `C:\Users\caelf\AppData\Local\Programs\Python\Python314\Scripts\`
   - `C:\Program Files\PostgreSQL\15\bin\`
6. Click **OK** on all dialogs
7. **Close and reopen PowerShell**

### **Option 3: Use py Command (Python)**

Windows Python installer includes a launcher. Try:

```powershell
py --version
py -m pip --version
```

If this works, you can use `py` instead of `python` everywhere!

---

## 📊 Verify Installations

Once PATH is set up, verify:

```powershell
# Check Python
python --version
# OR
py --version

# Check pip
pip --version
# OR  
py -m pip --version

# Check PostgreSQL
psql --version
```

You should see:
- Python 3.14.0
- PostgreSQL 15.14

---

## 🗄️ Create the Three Databases

Once `psql` command works, create the databases:

### **Method 1: Using psql Command**

```powershell
# You'll be prompted for password (default is usually 'postgres')
psql -U postgres -c "CREATE DATABASE interview_prep;"
psql -U postgres -c "CREATE DATABASE banking_app;"
psql -U postgres -c "CREATE DATABASE job_applier;"
```

### **Method 2: Interactive Mode**

```powershell
# Connect to PostgreSQL
psql -U postgres

# Then type these commands:
CREATE DATABASE interview_prep;
CREATE DATABASE banking_app;
CREATE DATABASE job_applier;

# List databases to verify
\l

# Exit
\q
```

### **Method 3: Using pgAdmin (GUI)**

If you installed pgAdmin with PostgreSQL:
1. Open pgAdmin
2. Connect to PostgreSQL server
3. Right-click "Databases" → "Create" → "Database"
4. Create: `interview_prep`, `banking_app`, `job_applier`

---

## ✅ Verification Checklist

- [ ] Python works: `python --version` or `py --version`
- [ ] PostgreSQL works: `psql --version`
- [ ] Three databases created
- [ ] You know your PostgreSQL password

---

## 🚀 Next Steps After This

1. **Create .env files** → See `CREATE_ENV_FILES.md`
2. **Follow QUICK_START.md** to run the projects

---

## 🔧 Troubleshooting

### "Access denied" when creating databases

**Solution**: Use the postgres superuser:
```powershell
psql -U postgres
# Enter your password (set during PostgreSQL installation)
```

### "Password authentication failed"

**Solution**: Your password might be different from 'postgres'. Try:
- The password you set during installation
- Check pgAdmin → you can reset it there
- Or leave password blank (just press Enter)

### Python works but pip doesn't

**Solution**: Use the Python module:
```powershell
py -m pip --version
py -m pip install --upgrade pip
```

---

## 📝 Quick Commands Summary

```powershell
# Close and reopen PowerShell first!

# Test installations
python --version
psql --version

# Create databases
psql -U postgres -c "CREATE DATABASE interview_prep;"
psql -U postgres -c "CREATE DATABASE banking_app;"
psql -U postgres -c "CREATE DATABASE job_applier;"

# Verify databases exist
psql -U postgres -c "\l"
```

---

**Once you can run `python --version` and `psql --version` successfully, you're ready to move forward!** 🎉


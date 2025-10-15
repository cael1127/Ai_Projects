# Reset PostgreSQL Password - Step by Step

## 🔐 Your PostgreSQL password is NOT 'postgres'

Let's reset it to 'postgres' so all your .env files work without changes.

---

## ✅ Method: Reset Password via Configuration

### **Step 1: Stop PostgreSQL Service**

Run in PowerShell **as Administrator**:

```powershell
Stop-Service postgresql-x64-15
```

### **Step 2: Edit pg_hba.conf**

1. **Open Notepad as Administrator**:
   - Search for "Notepad" in Start Menu
   - Right-click → "Run as administrator"

2. **Open the file**:
   - File → Open
   - Navigate to: `C:\Program Files\PostgreSQL\15\data\pg_hba.conf`
   - Change file filter to "All Files (*.*)"

3. **Find these lines** (near the bottom):

   ```
   # IPv4 local connections:
   host    all             all             127.0.0.1/32            scram-sha-256
   # IPv6 local connections:
   host    all             all             ::1/128                 scram-sha-256
   ```

4. **Change `scram-sha-256` to `trust`**:

   ```
   # IPv4 local connections:
   host    all             all             127.0.0.1/32            trust
   # IPv6 local connections:
   host    all             all             ::1/128                 trust
   ```

5. **Save the file** (Ctrl+S)

### **Step 3: Start PostgreSQL**

```powershell
Start-Service postgresql-x64-15
```

### **Step 4: Connect WITHOUT Password**

```powershell
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres
```

It should connect immediately without asking for password!

### **Step 5: Set New Password**

In the psql prompt, type:

```sql
ALTER USER postgres PASSWORD 'postgres';
```

Then:

```sql
\q
```

### **Step 6: Change pg_hba.conf BACK**

1. Open `C:\Program Files\PostgreSQL\15\data\pg_hba.conf` again as Administrator
2. Change `trust` BACK to `scram-sha-256`:

   ```
   # IPv4 local connections:
   host    all             all             127.0.0.1/32            scram-sha-256
   # IPv6 local connections:
   host    all             all             ::1/128                 scram-sha-256
   ```

3. Save the file

### **Step 7: Restart PostgreSQL**

```powershell
Restart-Service postgresql-x64-15
```

### **Step 8: Test New Password**

```powershell
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres
```

Password: `postgres`

Should work now! ✅

---

## 🗄️ Now Create the Databases

```powershell
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "CREATE DATABASE interview_prep;"
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "CREATE DATABASE banking_app;"
& "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "CREATE DATABASE job_applier;"
```

Password: `postgres`

---

## ✅ Alternative: Use pgAdmin

1. **Open pgAdmin**
2. Connect to PostgreSQL (it might remember the password)
3. Right-click PostgreSQL server → "Properties" → "Connection"
4. Set password to: `postgres`
5. Create the three databases there

---

## 🎯 Summary

By the end of this, you'll have:
- ✅ PostgreSQL password set to `postgres`
- ✅ Three databases created
- ✅ All .env files working without modification

**Try this and let me know if you need help with any step!** 🔐



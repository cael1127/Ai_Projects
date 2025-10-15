# 🚀 Installing All Prerequisites - Automated Setup

This guide will help you install everything you need for all three AI projects on Windows.

---

## 📋 What We'll Install

1. ✅ **Chocolatey** (Package manager for Windows)
2. ✅ **Git** (Version control)
3. ✅ **Python 3.11+** (For Interview Prep & Job Applier)
4. ✅ **Node.js 18+** (For Banking App & frontends)
5. ✅ **PostgreSQL 15+** (Database)
6. ✅ **VS Code** (Code editor)

---

## 🎯 One-Command Installation Script

### **Run as Administrator!**

Open **PowerShell as Administrator** (Right-click → "Run as Administrator") and run:

```powershell
# This script installs everything you need!

Write-Host "🚀 Installing Prerequisites for Three AI Projects..." -ForegroundColor Cyan
Write-Host ""

# 1. Install Chocolatey (Package Manager)
Write-Host "📦 Step 1/6: Installing Chocolatey..." -ForegroundColor Yellow
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "✅ Chocolatey installed!" -ForegroundColor Green
} else {
    Write-Host "✅ Chocolatey already installed!" -ForegroundColor Green
}

# Refresh environment
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 2. Install Git
Write-Host ""
Write-Host "📦 Step 2/6: Installing Git..." -ForegroundColor Yellow
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    choco install git -y
    Write-Host "✅ Git installed!" -ForegroundColor Green
} else {
    Write-Host "✅ Git already installed!" -ForegroundColor Green
}

# 3. Install Python 3.11
Write-Host ""
Write-Host "📦 Step 3/6: Installing Python 3.11..." -ForegroundColor Yellow
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    choco install python311 -y
    Write-Host "✅ Python 3.11 installed!" -ForegroundColor Green
} else {
    $pythonVersion = python --version
    Write-Host "✅ Python already installed: $pythonVersion" -ForegroundColor Green
}

# 4. Install Node.js 18
Write-Host ""
Write-Host "📦 Step 4/6: Installing Node.js 18..." -ForegroundColor Yellow
if (!(Get-Command node -ErrorAction SilentlyContinue)) {
    choco install nodejs-lts -y
    Write-Host "✅ Node.js installed!" -ForegroundColor Green
} else {
    $nodeVersion = node --version
    Write-Host "✅ Node.js already installed: $nodeVersion" -ForegroundColor Green
}

# 5. Install PostgreSQL 15
Write-Host ""
Write-Host "📦 Step 5/6: Installing PostgreSQL 15..." -ForegroundColor Yellow
if (!(Get-Command psql -ErrorAction SilentlyContinue)) {
    choco install postgresql15 --params '/Password:postgres' -y
    Write-Host "✅ PostgreSQL 15 installed!" -ForegroundColor Green
    Write-Host "   Default password: postgres" -ForegroundColor Cyan
} else {
    Write-Host "✅ PostgreSQL already installed!" -ForegroundColor Green
}

# 6. Install VS Code
Write-Host ""
Write-Host "📦 Step 6/6: Installing VS Code..." -ForegroundColor Yellow
if (!(Get-Command code -ErrorAction SilentlyContinue)) {
    choco install vscode -y
    Write-Host "✅ VS Code installed!" -ForegroundColor Green
} else {
    Write-Host "✅ VS Code already installed!" -ForegroundColor Green
}

# Refresh environment variables
Write-Host ""
Write-Host "🔄 Refreshing environment variables..." -ForegroundColor Yellow
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Verify installations
Write-Host ""
Write-Host "✅ Installation Complete! Verifying..." -ForegroundColor Green
Write-Host ""

Write-Host "Installed Versions:" -ForegroundColor Cyan
try { Write-Host "  Git: $(git --version)" } catch { Write-Host "  Git: Not found - please restart PowerShell" -ForegroundColor Red }
try { Write-Host "  Python: $(python --version)" } catch { Write-Host "  Python: Not found - please restart PowerShell" -ForegroundColor Red }
try { Write-Host "  Node: $(node --version)" } catch { Write-Host "  Node: Not found - please restart PowerShell" -ForegroundColor Red }
try { Write-Host "  npm: $(npm --version)" } catch { Write-Host "  npm: Not found - please restart PowerShell" -ForegroundColor Red }
try { $pgVersion = psql --version; Write-Host "  PostgreSQL: $pgVersion" } catch { Write-Host "  PostgreSQL: Not found - please restart PowerShell" -ForegroundColor Red }

Write-Host ""
Write-Host "🎉 All prerequisites installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANT: Please close and reopen PowerShell for all changes to take effect!" -ForegroundColor Yellow
Write-Host ""
Write-Host "📝 Next Steps:" -ForegroundColor Cyan
Write-Host "   1. Close this PowerShell window"
Write-Host "   2. Open a new PowerShell window"
Write-Host "   3. Run: cd AiProjects"
Write-Host "   4. Create databases: see CREATE_DATABASES.md"
Write-Host "   5. Create .env files: see CREATE_ENV_FILES.md"
Write-Host "   6. Follow QUICK_START.md"
Write-Host ""
```

---

## 📝 Manual Installation (If Needed)

If the automated script has issues, install manually:

### 1. **Chocolatey** (Package Manager)

```powershell
# Run in PowerShell as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### 2. **Git**

```powershell
choco install git -y
```

Or download from: https://git-scm.com/download/win

### 3. **Python 3.11**

```powershell
choco install python311 -y
```

Or download from: https://www.python.org/downloads/

### 4. **Node.js 18 LTS**

```powershell
choco install nodejs-lts -y
```

Or download from: https://nodejs.org/

### 5. **PostgreSQL 15**

```powershell
choco install postgresql15 --params '/Password:postgres' -y
```

Or download from: https://www.postgresql.org/download/windows/

**Default credentials:**
- Username: `postgres`
- Password: `postgres`

### 6. **VS Code**

```powershell
choco install vscode -y
```

Or download from: https://code.visualstudio.com/

---

## ✅ Verification Script

After installation, verify everything is working:

```powershell
Write-Host "Checking installations..." -ForegroundColor Cyan
Write-Host ""

# Check Git
if (Get-Command git -ErrorAction SilentlyContinue) {
    Write-Host "✅ Git: $(git --version)" -ForegroundColor Green
} else {
    Write-Host "❌ Git: Not installed" -ForegroundColor Red
}

# Check Python
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pyVersion = python --version
    if ($pyVersion -match "3\.1[1-9]") {
        Write-Host "✅ Python: $pyVersion" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Python: $pyVersion (Need 3.11+)" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Python: Not installed" -ForegroundColor Red
}

# Check Node.js
if (Get-Command node -ErrorAction SilentlyContinue) {
    $nodeVersion = node --version
    if ($nodeVersion -match "v1[8-9]|v[2-9][0-9]") {
        Write-Host "✅ Node.js: $nodeVersion" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Node.js: $nodeVersion (Need v18+)" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Node.js: Not installed" -ForegroundColor Red
}

# Check npm
if (Get-Command npm -ErrorAction SilentlyContinue) {
    Write-Host "✅ npm: $(npm --version)" -ForegroundColor Green
} else {
    Write-Host "❌ npm: Not installed" -ForegroundColor Red
}

# Check PostgreSQL
if (Get-Command psql -ErrorAction SilentlyContinue) {
    Write-Host "✅ PostgreSQL: $(psql --version)" -ForegroundColor Green
} else {
    Write-Host "❌ PostgreSQL: Not installed" -ForegroundColor Red
}

# Check VS Code
if (Get-Command code -ErrorAction SilentlyContinue) {
    Write-Host "✅ VS Code: Installed" -ForegroundColor Green
} else {
    Write-Host "⚠️  VS Code: Not found in PATH (may need restart)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Verification complete!" -ForegroundColor Cyan
```

---

## 🎯 Post-Installation Setup

### 1. **Configure PostgreSQL**

After PostgreSQL is installed:

```powershell
# Add PostgreSQL to PATH (if not automatic)
$env:Path += ";C:\Program Files\PostgreSQL\15\bin"

# Test connection
psql -U postgres -c "SELECT version();"
# Password: postgres
```

### 2. **Install Python Tools**

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install virtualenv
pip install virtualenv
```

### 3. **Verify Node Package Manager**

```powershell
npm --version
npx --version
```

---

## 🗄️ Create Databases

After PostgreSQL is installed:

```powershell
# Connect to PostgreSQL
psql -U postgres

# Then run these commands:
CREATE DATABASE interview_prep;
CREATE DATABASE banking_app;
CREATE DATABASE job_applier;
\q
```

Or one-liner:

```powershell
psql -U postgres -c "CREATE DATABASE interview_prep;"
psql -U postgres -c "CREATE DATABASE banking_app;"
psql -U postgres -c "CREATE DATABASE job_applier;"
```

---

## 🔧 Troubleshooting

### Issue: "Command not found" after installation

**Solution**: Close and reopen PowerShell

### Issue: PostgreSQL password not working

**Solution**: Reset password:

```powershell
# Run as Administrator
psql -U postgres
# If it asks for password and you don't know it:
# 1. Edit pg_hba.conf (usually in C:\Program Files\PostgreSQL\15\data\)
# 2. Change "md5" to "trust" temporarily
# 3. Restart PostgreSQL service
# 4. Set new password with: ALTER USER postgres PASSWORD 'postgres';
# 5. Change "trust" back to "md5"
```

### Issue: Python/Node not in PATH

**Solution**: Add to PATH manually or restart computer

### Issue: Chocolatey installation fails

**Solution**: Ensure you're running PowerShell as Administrator

---

## 🎉 Installation Complete!

After everything is installed:

1. ✅ Close and reopen PowerShell
2. ✅ Verify all installations with the verification script
3. ✅ Create the three databases
4. ✅ Create .env files (see `CREATE_ENV_FILES.md`)
5. ✅ Follow `QUICK_START.md` to run the projects!

---

## 📊 Installation Checklist

- [ ] Chocolatey installed
- [ ] Git installed (`git --version` works)
- [ ] Python 3.11+ installed (`python --version` works)
- [ ] Node.js 18+ installed (`node --version` works)
- [ ] PostgreSQL 15+ installed (`psql --version` works)
- [ ] VS Code installed
- [ ] Three databases created
- [ ] All commands work in new PowerShell window

---

## 🚀 Next Steps

Once all prerequisites are installed:

1. **Create Databases** (see above)
2. **Create .env Files** → Run script in `CREATE_ENV_FILES.md`
3. **Start Projects** → Follow `QUICK_START.md`

You're almost ready to run all three AI projects! 🎉


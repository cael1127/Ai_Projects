# Three AI Projects - Prerequisites Installation Script
# Run this in PowerShell as Administrator

Write-Host "🚀 Installing Prerequisites for Three AI Projects..." -ForegroundColor Cyan
Write-Host ""
Write-Host "⚠️  Make sure you're running PowerShell as Administrator!" -ForegroundColor Yellow
Write-Host ""

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "❌ ERROR: This script must be run as Administrator!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please:" -ForegroundColor Yellow
    Write-Host "  1. Right-click PowerShell" -ForegroundColor Yellow
    Write-Host "  2. Select 'Run as Administrator'" -ForegroundColor Yellow
    Write-Host "  3. Run this script again" -ForegroundColor Yellow
    exit 1
}

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
    Write-Host "   Username: postgres" -ForegroundColor Cyan
    Write-Host "   Password: postgres" -ForegroundColor Cyan
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
try { Write-Host "  ✅ Git: $(git --version)" -ForegroundColor Green } catch { Write-Host "  ⚠️  Git: Not found - restart PowerShell" -ForegroundColor Yellow }
try { Write-Host "  ✅ Python: $(python --version)" -ForegroundColor Green } catch { Write-Host "  ⚠️  Python: Not found - restart PowerShell" -ForegroundColor Yellow }
try { Write-Host "  ✅ Node: $(node --version)" -ForegroundColor Green } catch { Write-Host "  ⚠️  Node: Not found - restart PowerShell" -ForegroundColor Yellow }
try { Write-Host "  ✅ npm: $(npm --version)" -ForegroundColor Green } catch { Write-Host "  ⚠️  npm: Not found - restart PowerShell" -ForegroundColor Yellow }
try { $pgVersion = psql --version; Write-Host "  ✅ PostgreSQL: $pgVersion" -ForegroundColor Green } catch { Write-Host "  ⚠️  PostgreSQL: Not found - restart PowerShell" -ForegroundColor Yellow }
try { Write-Host "  ✅ VS Code: Installed" -ForegroundColor Green } catch { Write-Host "  ⚠️  VS Code: Not found - restart PowerShell" -ForegroundColor Yellow }

Write-Host ""
Write-Host "🎉 All prerequisites installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANT NEXT STEPS:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  1️⃣  Close this PowerShell window" -ForegroundColor Cyan
Write-Host "  2️⃣  Open a NEW PowerShell window (as regular user)" -ForegroundColor Cyan
Write-Host "  3️⃣  Navigate to: cd C:\Users\caelf\AiProjects" -ForegroundColor Cyan
Write-Host "  4️⃣  Create databases - run:" -ForegroundColor Cyan
Write-Host "      psql -U postgres -c 'CREATE DATABASE interview_prep;'" -ForegroundColor White
Write-Host "      psql -U postgres -c 'CREATE DATABASE banking_app;'" -ForegroundColor White
Write-Host "      psql -U postgres -c 'CREATE DATABASE job_applier;'" -ForegroundColor White
Write-Host "      (Password: postgres)" -ForegroundColor Gray
Write-Host ""
Write-Host "  5️⃣  Create .env files - see CREATE_ENV_FILES.md" -ForegroundColor Cyan
Write-Host "  6️⃣  Follow QUICK_START.md to run all projects!" -ForegroundColor Cyan
Write-Host ""

# Pause so user can read
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")


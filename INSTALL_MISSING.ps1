# Install Only What's Missing - Custom Script for Your System
# Run this in PowerShell as Administrator

Write-Host "Installing Missing Prerequisites..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Current Status:" -ForegroundColor Yellow
Write-Host "  [OK] Git: Already installed" -ForegroundColor Green
Write-Host "  [OK] Node.js: Already installed" -ForegroundColor Green
Write-Host "  [OK] npm: Already installed" -ForegroundColor Green
Write-Host "  [--] Python: Need to install" -ForegroundColor Red
Write-Host "  [--] PostgreSQL: Need to install" -ForegroundColor Red
Write-Host ""

# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "[ERROR] This script must be run as Administrator!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please:" -ForegroundColor Yellow
    Write-Host "  1. Right-click PowerShell" -ForegroundColor Yellow
    Write-Host "  2. Select 'Run as Administrator'" -ForegroundColor Yellow
    Write-Host "  3. Navigate to: cd C:\Users\caelf\AiProjects" -ForegroundColor Yellow
    Write-Host "  4. Run: .\INSTALL_MISSING.ps1" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Running as Administrator" -ForegroundColor Green
Write-Host ""

# Install Chocolatey if not present (needed for installations)
Write-Host "Checking Chocolatey..." -ForegroundColor Yellow
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Installing Chocolatey package manager..." -ForegroundColor Yellow
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "[OK] Chocolatey installed!" -ForegroundColor Green
} else {
    Write-Host "[OK] Chocolatey already installed" -ForegroundColor Green
}

# Refresh environment
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Install Python 3.11
Write-Host ""
Write-Host "Step 1/2: Installing Python 3.11..." -ForegroundColor Yellow
Write-Host "   This will take a few minutes..." -ForegroundColor Gray
choco install python311 -y
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Python 3.11 installed successfully!" -ForegroundColor Green
} else {
    Write-Host "[WARNING] Python installation encountered an issue" -ForegroundColor Yellow
}

# Refresh environment
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Install PostgreSQL 15
Write-Host ""
Write-Host "Step 2/2: Installing PostgreSQL 15..." -ForegroundColor Yellow
Write-Host "   This will take a few minutes..." -ForegroundColor Gray
Write-Host "   Default password will be set to: postgres" -ForegroundColor Cyan
choco install postgresql15 --params '/Password:postgres' -y
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] PostgreSQL 15 installed successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "   PostgreSQL Credentials:" -ForegroundColor Cyan
    Write-Host "      Username: postgres" -ForegroundColor White
    Write-Host "      Password: postgres" -ForegroundColor White
} else {
    Write-Host "[WARNING] PostgreSQL installation encountered an issue" -ForegroundColor Yellow
}

# Refresh environment variables
Write-Host ""
Write-Host "Refreshing environment variables..." -ForegroundColor Yellow
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Verify installations
Write-Host ""
Write-Host "[OK] Installation Complete! Verifying..." -ForegroundColor Green
Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Current Installations:" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

try { 
    $gitVer = git --version
    Write-Host "[OK] Git: $gitVer" -ForegroundColor Green 
} catch { 
    Write-Host "[--] Git: Not found" -ForegroundColor Red 
}

try { 
    $pyVer = python --version 2>&1
    Write-Host "[OK] Python: $pyVer" -ForegroundColor Green 
} catch { 
    Write-Host "[WARNING] Python: Not found - restart PowerShell" -ForegroundColor Yellow 
}

try { 
    $nodeVer = node --version
    Write-Host "[OK] Node.js: $nodeVer" -ForegroundColor Green 
} catch { 
    Write-Host "[--] Node.js: Not found" -ForegroundColor Red 
}

try { 
    $npmVer = npm --version
    Write-Host "[OK] npm: $npmVer" -ForegroundColor Green 
} catch { 
    Write-Host "[--] npm: Not found" -ForegroundColor Red 
}

try { 
    $pgVer = psql --version 2>&1
    Write-Host "[OK] PostgreSQL: $pgVer" -ForegroundColor Green 
} catch { 
    Write-Host "[WARNING] PostgreSQL: Not found - restart PowerShell" -ForegroundColor Yellow 
}

Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "SUCCESS! Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "IMPORTANT: Next Steps" -ForegroundColor Yellow
Write-Host ""
Write-Host "Step 1: CLOSE this PowerShell window" -ForegroundColor Cyan
Write-Host ""
Write-Host "Step 2: OPEN a NEW PowerShell window (regular user, not admin)" -ForegroundColor Cyan
Write-Host ""
Write-Host "Step 3: Verify installations work:" -ForegroundColor Cyan
Write-Host "    python --version" -ForegroundColor White
Write-Host "    psql --version" -ForegroundColor White
Write-Host ""
Write-Host "Step 4: Create the three databases:" -ForegroundColor Cyan
Write-Host "    psql -U postgres -c ""CREATE DATABASE interview_prep;""" -ForegroundColor White
Write-Host "    psql -U postgres -c ""CREATE DATABASE banking_app;""" -ForegroundColor White
Write-Host "    psql -U postgres -c ""CREATE DATABASE job_applier;""" -ForegroundColor White
Write-Host "    (Password: postgres)" -ForegroundColor Gray
Write-Host ""
Write-Host "Step 5: Create .env files:" -ForegroundColor Cyan
Write-Host "    See CREATE_ENV_FILES.md for the script" -ForegroundColor White
Write-Host ""
Write-Host "Step 6: Start the projects:" -ForegroundColor Cyan
Write-Host "    Follow QUICK_START.md" -ForegroundColor White
Write-Host ""

Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")


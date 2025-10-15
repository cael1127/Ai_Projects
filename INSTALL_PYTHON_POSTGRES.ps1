# Install Python and PostgreSQL - Simple Version
# Run in PowerShell as Administrator AFTER running FIX_CHOCOLATEY.ps1

Write-Host "Installing Python 3.11 and PostgreSQL 15..." -ForegroundColor Cyan
Write-Host ""

# Check if running as admin
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "[ERROR] Must run as Administrator!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Step 1: Installing Python 3.11..." -ForegroundColor Yellow
Write-Host "This may take 3-5 minutes..." -ForegroundColor Gray
Write-Host ""

choco install python311 -y --force

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[OK] Python installed!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "[WARNING] Python installation had issues" -ForegroundColor Yellow
    Write-Host "You can also download from: https://www.python.org/downloads/" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Step 2: Installing PostgreSQL 15..." -ForegroundColor Yellow
Write-Host "This may take 5-10 minutes..." -ForegroundColor Gray
Write-Host ""

choco install postgresql15 --params '/Password:postgres' -y --force

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[OK] PostgreSQL installed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "PostgreSQL Credentials:" -ForegroundColor Cyan
    Write-Host "  Username: postgres" -ForegroundColor White
    Write-Host "  Password: postgres" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "[WARNING] PostgreSQL installation had issues" -ForegroundColor Yellow
    Write-Host "You can also download from: https://www.postgresql.org/download/windows/" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Installation Complete!" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Close this PowerShell window" -ForegroundColor White
Write-Host "2. Open a NEW PowerShell (regular user)" -ForegroundColor White
Write-Host "3. Test installations:" -ForegroundColor White
Write-Host "   python --version" -ForegroundColor Gray
Write-Host "   psql --version" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Create databases:" -ForegroundColor White
Write-Host "   psql -U postgres -c ""CREATE DATABASE interview_prep;""" -ForegroundColor Gray
Write-Host "   psql -U postgres -c ""CREATE DATABASE banking_app;""" -ForegroundColor Gray
Write-Host "   psql -U postgres -c ""CREATE DATABASE job_applier;""" -ForegroundColor Gray
Write-Host ""

Read-Host "Press Enter to exit"


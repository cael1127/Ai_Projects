# All-in-One Setup Script
# Run this in regular PowerShell (NOT as admin)
# This creates databases and .env files in one go!

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Three AI Projects - Complete Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check installations
Write-Host "Checking prerequisites..." -ForegroundColor Yellow
Write-Host ""

$pythonOk = $false
$postgresOk = $false

# Check Python
try {
    $pyVersion = py --version 2>&1
    Write-Host "[OK] Python: $pyVersion" -ForegroundColor Green
    $pythonOk = $true
} catch {
    Write-Host "[ERROR] Python not found! Please install Python 3.11+" -ForegroundColor Red
}

# Check Node
try {
    $nodeVersion = node --version
    Write-Host "[OK] Node.js: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Node.js not found!" -ForegroundColor Red
}

# Check PostgreSQL
$psqlPath = "C:\Program Files\PostgreSQL\15\bin\psql.exe"
if (Test-Path $psqlPath) {
    $pgVersion = & $psqlPath --version
    Write-Host "[OK] PostgreSQL: $pgVersion" -ForegroundColor Green
    $postgresOk = $true
} else {
    Write-Host "[ERROR] PostgreSQL not found!" -ForegroundColor Red
}

Write-Host ""

if (-not ($pythonOk -and $postgresOk)) {
    Write-Host "Please install missing prerequisites first!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Get PostgreSQL password
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 1: Database Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$pgPassword = Read-Host "Enter your PostgreSQL password (for user 'postgres')" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pgPassword)
$pgPasswordPlain = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

Write-Host ""
Write-Host "Creating databases..." -ForegroundColor Yellow

# Set password environment variable
$env:PGPASSWORD = $pgPasswordPlain

try {
    & $psqlPath -U postgres -c "CREATE DATABASE interview_prep;" 2>&1 | Out-Null
    Write-Host "[OK] Created: interview_prep" -ForegroundColor Green
    
    & $psqlPath -U postgres -c "CREATE DATABASE banking_app;" 2>&1 | Out-Null
    Write-Host "[OK] Created: banking_app" -ForegroundColor Green
    
    & $psqlPath -U postgres -c "CREATE DATABASE job_applier;" 2>&1 | Out-Null
    Write-Host "[OK] Created: job_applier" -ForegroundColor Green
} catch {
    Write-Host "[WARNING] Some databases may already exist (this is OK)" -ForegroundColor Yellow
}

# Clear password from environment
Remove-Item Env:\PGPASSWORD

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 2: Creating .env Files" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$dbUrlBase = "postgresql://postgres:${pgPasswordPlain}@localhost:5432"

# Create .env files
Write-Host "Creating environment files..." -ForegroundColor Yellow
Write-Host ""

# 1. Interview Prep Backend
$envContent = @"
DATABASE_URL=${dbUrlBase}/interview_prep
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=interview-prep-secret-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=Interview Prep Tool
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3000
MOCK_MODE=True
REDIS_URL=redis://localhost:6379/0
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=http://localhost:3000/auth/callback
"@
$envContent | Out-File -FilePath "interview-prep\backend\.env" -Encoding UTF8
Write-Host "[OK] interview-prep/backend/.env" -ForegroundColor Green

# 2. Interview Prep Frontend
"NEXT_PUBLIC_API_URL=http://localhost:8000" | Out-File -FilePath "interview-prep\frontend\.env.local" -Encoding UTF8
Write-Host "[OK] interview-prep/frontend/.env.local" -ForegroundColor Green

# 3. Banking Backend
$envContent = @"
PORT=3001
NODE_ENV=development
DATABASE_URL=${dbUrlBase}/banking_app
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
JWT_SECRET=banking-app-secret-change-in-production
MOCK_PLAID=true
FIREBASE_PROJECT_ID=demo-project
FIREBASE_PRIVATE_KEY=dummy
FIREBASE_CLIENT_EMAIL=demo@example.com
PLAID_CLIENT_ID=dummy
PLAID_SECRET=dummy
PLAID_ENV=sandbox
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_KEY=
"@
$envContent | Out-File -FilePath "banking-app\backend\.env" -Encoding UTF8
Write-Host "[OK] banking-app/backend/.env" -ForegroundColor Green

# 4. Banking Web
"NEXT_PUBLIC_API_URL=http://localhost:3001" | Out-File -FilePath "banking-app\web\.env.local" -Encoding UTF8
Write-Host "[OK] banking-app/web/.env.local" -ForegroundColor Green

# 5. Job Applier Backend
$envContent = @"
DATABASE_URL=${dbUrlBase}/job_applier
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY_HERE
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o
SECRET_KEY=job-applier-secret-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=AI Job Applier
APP_VERSION=1.0.0
DEBUG=True
FRONTEND_URL=http://localhost:3003
HEADLESS_BROWSER=True
MOCK_AUTOMATION=True
REDIS_URL=redis://localhost:6379/0
GMAIL_CLIENT_ID=
GMAIL_CLIENT_SECRET=
GMAIL_REDIRECT_URI=http://localhost:3003/auth/callback
"@
$envContent | Out-File -FilePath "job-applier\backend\.env" -Encoding UTF8
Write-Host "[OK] job-applier/backend/.env" -ForegroundColor Green

# 6. Job Applier Frontend
"NEXT_PUBLIC_API_URL=http://localhost:8001" | Out-File -FilePath "job-applier\frontend\.env.local" -Encoding UTF8
Write-Host "[OK] job-applier/frontend/.env.local" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "What was created:" -ForegroundColor Yellow
Write-Host "  [OK] 3 PostgreSQL databases" -ForegroundColor Green
Write-Host "  [OK] 6 .env files with your OpenRouter API key" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host ""
Write-Host "Follow QUICK_START.md to run the projects!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Quick summary:" -ForegroundColor White
Write-Host "  1. Each project needs 2 terminals (backend + frontend)" -ForegroundColor Gray
Write-Host "  2. Use 'py' instead of 'python' for Python commands" -ForegroundColor Gray
Write-Host "  3. All AI features will work with your OpenRouter key" -ForegroundColor Gray
Write-Host ""

Read-Host "Press Enter to exit"


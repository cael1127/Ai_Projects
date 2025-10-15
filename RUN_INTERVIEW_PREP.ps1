# Simple Script to Start Interview Prep Backend
# Run this from C:\Users\caelf\AiProjects

Write-Host "Starting Interview Prep Backend..." -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
$projectRoot = "C:\Users\caelf\AiProjects"
if (-not (Test-Path $projectRoot)) {
    Write-Host "[ERROR] Project directory not found!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

cd $projectRoot
cd interview-prep\backend

Write-Host "Current directory: $(Get-Location)" -ForegroundColor Gray
Write-Host ""

# Check if venv exists
if (-not (Test-Path "venv")) {
    Write-Host "[ERROR] Virtual environment not found!" -ForegroundColor Red
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    py -m venv venv
}

# Activate and run
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "Starting FastAPI server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Server will start on: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

uvicorn app.main:app --reload --port 8000



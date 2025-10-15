# Run Interview Prep Backend - Complete Script
# Run this from C:\Users\caelf\AiProjects

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Interview Prep Backend" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to backend directory
cd C:\Users\caelf\AiProjects\interview-prep\backend

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Start the server
Write-Host ""
Write-Host "[OK] Starting FastAPI server on port 8080..." -ForegroundColor Green
Write-Host ""
Write-Host "Server URLs:" -ForegroundColor Cyan
Write-Host "  API: http://localhost:8080" -ForegroundColor White
Write-Host "  Docs: http://localhost:8080/docs" -ForegroundColor White
Write-Host "  Health: http://localhost:8080/health" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

uvicorn app.main:app --reload --port 8080


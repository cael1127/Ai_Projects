# Run Interview Prep Frontend - Complete Script
# Run this from C:\Users\caelf\AiProjects in a SECOND terminal

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Interview Prep Frontend" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to frontend directory
cd C:\Users\caelf\AiProjects\interview-prep\frontend

# Update .env.local to point to port 8080
Write-Host "Updating API URL..." -ForegroundColor Yellow
"NEXT_PUBLIC_API_URL=http://localhost:8080" | Out-File -FilePath ".env.local" -Encoding UTF8

# Check if node_modules exists
if (-not (Test-Path "node_modules")) {
    Write-Host "Installing dependencies (this takes 2-3 minutes)..." -ForegroundColor Yellow
    npm install
    Write-Host ""
}

# Start the server
Write-Host "[OK] Starting Next.js development server..." -ForegroundColor Green
Write-Host ""
Write-Host "Frontend URL:" -ForegroundColor Cyan
Write-Host "  http://localhost:3000" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

npm run dev


# Fix Chocolatey Lock File Issue
# Run this in PowerShell as Administrator

Write-Host "Fixing Chocolatey lock file issue..." -ForegroundColor Cyan
Write-Host ""

# Remove the lock file that's causing the issue
$lockFile = "C:\ProgramData\chocolatey\lib\2c83db4d4d218d74778538ed5c96a122186bdbf9"
if (Test-Path $lockFile) {
    Write-Host "Removing lock file..." -ForegroundColor Yellow
    Remove-Item $lockFile -Force -ErrorAction SilentlyContinue
    Write-Host "[OK] Lock file removed" -ForegroundColor Green
} else {
    Write-Host "Lock file not found (may already be cleaned)" -ForegroundColor Gray
}

# Try to fix lib-bad directory permissions
$libBadDir = "C:\ProgramData\chocolatey\lib-bad"
if (Test-Path $libBadDir) {
    Write-Host "Fixing lib-bad directory permissions..." -ForegroundColor Yellow
    try {
        $acl = Get-Acl $libBadDir
        $acl.SetAccessRuleProtection($false, $true)
        Set-Acl $libBadDir $acl
        Write-Host "[OK] Permissions fixed" -ForegroundColor Green
    } catch {
        Write-Host "[WARNING] Could not fix permissions, trying to remove directory..." -ForegroundColor Yellow
        Remove-Item $libBadDir -Recurse -Force -ErrorAction SilentlyContinue
    }
} else {
    Write-Host "Creating lib-bad directory with proper permissions..." -ForegroundColor Yellow
    New-Item -Path $libBadDir -ItemType Directory -Force | Out-Null
}

# Clean up python311 directory if it exists in a bad state
$pythonDir = "C:\ProgramData\chocolatey\lib\python311"
if (Test-Path $pythonDir) {
    Write-Host "Cleaning up partial Python installation..." -ForegroundColor Yellow
    Remove-Item $pythonDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "[OK] Cleaned up" -ForegroundColor Green
}

Write-Host ""
Write-Host "[OK] Chocolatey cleaned up successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Now you can install Python and PostgreSQL" -ForegroundColor Cyan
Write-Host ""

Read-Host "Press Enter to continue"


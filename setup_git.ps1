# Git setup script for DevGenius deployment (PowerShell)

Write-Host "🚀 Setting up Git repository for DevGenius..." -ForegroundColor Green

# Initialize git if not already done
if (!(Test-Path ".git")) {
    Write-Host "📁 Initializing Git repository..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "✅ Git repository already exists" -ForegroundColor Green
}

# Add all files
Write-Host "📋 Adding files to Git..." -ForegroundColor Yellow
git add .

# Check if there are changes to commit
$status = git status --porcelain
if ($status) {
    # Commit changes
    Write-Host "💾 Committing changes..." -ForegroundColor Yellow
    git commit -m "Setup DevGenius AI Multi-Agent System for deployment"
} else {
    Write-Host "⚠️  No changes to commit" -ForegroundColor Yellow
}

Write-Host "✅ Git setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Create a repository on GitHub" -ForegroundColor White
Write-Host "2. Add remote: git remote add origin https://github.com/yourusername/devgenius.git" -ForegroundColor White
Write-Host "3. Push to GitHub: git push -u origin main" -ForegroundColor White
Write-Host "4. Deploy to Streamlit Cloud!" -ForegroundColor White

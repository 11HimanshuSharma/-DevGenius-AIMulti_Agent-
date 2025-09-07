#!/bin/bash
# Git setup script for DevGenius deployment

echo "🚀 Setting up Git repository for DevGenius..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already exists"
fi

# Add all files
echo "📋 Adding files to Git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "⚠️  No changes to commit"
else
    # Commit changes
    echo "💾 Committing changes..."
    git commit -m "Setup DevGenius AI Multi-Agent System for deployment"
fi

echo "✅ Git setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a repository on GitHub"
echo "2. Add remote: git remote add origin https://github.com/yourusername/devgenius.git"
echo "3. Push to GitHub: git push -u origin main"
echo "4. Deploy to Streamlit Cloud!"

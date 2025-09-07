<!-- @format -->

# 🚀 Deploy DevGenius to Streamlit Cloud

## Quick Deployment Guide

### Prerequisites

- GitHub account
- Streamlit Cloud account (free at
  [share.streamlit.io](https://share.streamlit.io))
- Azure OpenAI API credentials

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Push your project files:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/devgenius.git
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Deploy an app"
3. Connect your GitHub repository
4. Set main file path to: `app.py`
5. Click "Deploy!"

### Step 3: Add Secrets

1. In your Streamlit Cloud app dashboard, click "Manage app"
2. Go to "Secrets" tab
3. Add your Azure OpenAI credentials in this exact format:
   ```toml
   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = "your_deployment_name"
   AZURE_OPENAI_CHAT_ENDPOINT = "https://your-resource.openai.azure.com/"
   AZURE_OPENAI_CHAT_API_KEY = "your_api_key"
   ```
4. Save secrets

### Step 4: Your App is Live! 🎉

Your DevGenius AI Multi-Agent System will be available at:
`https://your-app-name.streamlit.app`

### Files included for deployment:

- ✅ `app.py` - Main application
- ✅ `requirements.txt` - Dependencies
- ✅ `config.py` - Handles both local and cloud secrets
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ All module files (agents.py, workflow.py, models.py, utils.py)

### Local Testing

Test locally before deploying:

```bash
streamlit run app.py
```

That's it! Your AI development team is now deployed and accessible worldwide! 🌍

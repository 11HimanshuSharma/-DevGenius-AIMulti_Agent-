<!-- @format -->

# 🔧 Troubleshooting Guide: Missing Credentials Error

## ❌ Error Description

```
OpenAIError: Missing credentials. Please pass one of `api_key`, `azure_ad_token`, `azure_ad_token_provider`, or the `AZURE_OPENAI_API_KEY` or `AZURE_OPENAI_AD_TOKEN` environment variables.
```

## 🔍 Root Cause

This error occurs when the Azure OpenAI credentials are not properly configured
in your deployment environment. The application cannot access the required API
credentials to initialize the LLM.

## 💡 Solutions

### 🌐 **For Streamlit Cloud Deployment**

#### Step 1: Check Secrets Configuration

1. Go to your Streamlit Cloud app dashboard
2. Click "Manage app" → "Secrets" tab
3. Ensure your secrets are formatted exactly like this:

```toml
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = "your_deployment_name"
AZURE_OPENAI_CHAT_ENDPOINT = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_CHAT_API_KEY = "your_api_key"
```

#### Step 2: Verify Values

- **Deployment Name**: Should match your Azure OpenAI deployment name exactly
- **Endpoint**: Should be your full Azure OpenAI resource endpoint URL
- **API Key**: Should be your valid Azure OpenAI API key

#### Step 3: Common Mistakes to Avoid

❌ **Wrong**: Using brackets `[AZURE_OPENAI]` ✅ **Correct**: Flat structure
without brackets

❌ **Wrong**: Missing quotes around values ✅ **Correct**: All values in quotes

❌ **Wrong**: Extra spaces or special characters ✅ **Correct**: Clean, exact
values

#### Step 4: Restart App

After adding/updating secrets:

1. Save the secrets
2. Click "Reboot app" in Streamlit Cloud
3. Wait for the app to restart

### 💻 **For Local Development**

#### Step 1: Create .env File

Create a `.env` file in your project root:

```env
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_CHAT_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_API_KEY=your_api_key
```

#### Step 2: Install python-dotenv

```bash
pip install python-dotenv
```

#### Step 3: Restart Application

```bash
streamlit run app.py
```

### 🔄 **Alternative LLM Options (If Azure Issues Persist)**

If you continue having Azure OpenAI issues, you can temporarily switch to other
providers:

#### Option 1: OpenAI GPT-3.5 Turbo

Update your `.env` or Streamlit secrets:

```env
OPENAI_API_KEY=your_openai_api_key
```

Then modify `config.py` to use OpenAI instead of Azure.

#### Option 2: Free Alternatives

- Google Gemini Pro (via Vertex AI)
- Hugging Face models
- Local models via Ollama

## ✅ Verification Steps

### 1. **Check Configuration**

The app now includes built-in configuration validation. If credentials are
missing, you'll see a clear error message with instructions.

### 2. **Test Locally First**

Before deploying to Streamlit Cloud:

1. Set up `.env` file locally
2. Run `streamlit run app.py`
3. Verify the app works locally
4. Then deploy to cloud

### 3. **Validate Credentials**

Ensure your Azure OpenAI credentials are:

- ✅ Active and not expired
- ✅ Have sufficient quota
- ✅ Correctly formatted
- ✅ Have proper permissions

## 🚨 Quick Fixes

### **Immediate Solution for Streamlit Cloud:**

1. **Copy this exact format** to your Streamlit Cloud secrets:

```toml
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = "gpt-4"
AZURE_OPENAI_CHAT_ENDPOINT = "https://your-resource-name.openai.azure.com/"
AZURE_OPENAI_CHAT_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

2. **Replace** the placeholder values with your actual credentials

3. **Save and reboot** the app

### **Alternative Quick Fix:**

If you have OpenAI API access instead of Azure:

1. Get your OpenAI API key from https://platform.openai.com/
2. Update the code to use OpenAI instead of Azure
3. Much simpler setup process

## 📞 Getting Help

### **If you're still stuck:**

1. **Verify Azure Setup**: Check your Azure OpenAI resource is properly
   configured
2. **Check Quotas**: Ensure you have available quota in Azure
3. **Test Credentials**: Try using the credentials in a simple script first
4. **Review Logs**: Check Streamlit Cloud logs for additional error details

### **Documentation References:**

- [Azure OpenAI Setup Guide](https://docs.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
- [LangChain Azure OpenAI Integration](https://python.langchain.com/docs/integrations/chat/azure_chat_openai)

## ✨ Prevention Tips

1. **Always test locally** before deploying
2. **Use template files** (like `.env.example`) for consistent formatting
3. **Double-check credentials** before deployment
4. **Keep backup credentials** for different environments
5. **Monitor API quotas** and usage limits

Your DevGenius AI Multi-Agent System should work perfectly once the credentials
are properly configured! 🚀

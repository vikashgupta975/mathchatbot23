# Streamlit Deployment Guide

## Quick Deployment Steps

### 1. Set Up GitHub Repository
- Create a new GitHub repository
- Copy all these files to your repository:
  - `app.py`
  - `utils.py`
  - `styles.py`
  - `.streamlit/config.toml`
  - `requirements.txt` (rename requirements_for_deploy.txt to requirements.txt)

### 2. Deploy on Streamlit Cloud
- Go to https://streamlit.io/cloud
- Sign in with GitHub
- Click "New app"
- Select your repository
- Select main branch
- Enter "app.py" as the main file path
- Click "Deploy"

### 3. Set Up Your API Key
- After deployment, go to app settings
- Click on "Secrets"
- Add this code (replace with your actual API key):
  ```
  MISTRAL_API_KEY = "your-actual-api-key-here"
  ```
- Click "Save"
- Click "Reboot app"

## Common Deployment Issues & Solutions

### Issue 1: API Key Not Working
- Make sure the API key is correctly entered in secrets
- Check for extra spaces or quotes
- Verify your Mistral AI account is active

### Issue 2: Missing Packages
- If you get package errors, check that your requirements.txt has:
  ```
  streamlit==1.44.1
  requests==2.32.3
  ```

### Issue 3: App Fails to Load
- Check Streamlit Cloud logs for error messages
- Make sure all files are correctly uploaded to GitHub
- Verify the main file path is set to "app.py"

### Issue 4: Timeout Errors
- Mistral AI API requests might time out
- Increase the timeout value in utils.py if needed

## Need Help?
- Check Streamlit's documentation: https://docs.streamlit.io/streamlit-cloud
- Check Mistral AI's documentation: https://docs.mistral.ai/
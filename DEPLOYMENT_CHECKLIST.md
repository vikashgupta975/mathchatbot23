# Deployment Checklist

## Files to Upload to GitHub
Make sure your repository includes these files:

- [x] `app.py` - Main application file
- [x] `utils.py` - Contains the Mistral API integration
- [x] `styles.py` - Teaching styles definitions
- [x] `.streamlit/config.toml` - Streamlit configuration
- [ ] `requirements.txt` - Rename requirements_for_deploy.txt to requirements.txt
- [x] `README.md` - Project documentation
- [x] `DEPLOYMENT_GUIDE.md` - Deployment instructions

## Before Deploying on Streamlit Cloud
1. Create a GitHub account if you don't have one
2. Create a new repository
3. Upload all files listed above
4. Ensure you've renamed requirements_for_deploy.txt to requirements.txt

## Streamlit Cloud Deployment Steps
1. Go to https://streamlit.io/cloud
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository, branch (main) and file path (app.py)
5. Click "Deploy"
6. In app settings, go to "Secrets" section
7. Add your Mistral API key:
   ```
   MISTRAL_API_KEY = "your-actual-api-key-here"
   ```
8. Save and click "Reboot app"

## Testing After Deployment
1. Open your deployed app URL
2. Try a simple math problem
3. Verify that all teaching styles work correctly

## Secrets Management
- Make sure your GitHub repository is public (or you have a Streamlit paid plan)
- Never commit your actual API key to the repository
- Only add your API key through Streamlit's secrets management

If you follow these steps exactly, your application will be deployed successfully!
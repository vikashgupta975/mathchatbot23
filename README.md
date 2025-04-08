# Math Problem Solver

A Streamlit-based math problem-solving chatbot using Mistral AI with multiple teaching styles.

## Created By
- Vikash Gupta (Reg: 12321380)
- Khushdeep Saini (Reg: 12316852)
- Satyam Upadhyay (Reg: 12318963)

## Features
- Interactive chat interface for submitting math problems
- 5 different teaching styles to choose from:
  - Standard: Clear and straightforward explanations
  - Detailed: Very thorough explanations with extensive breakdowns
  - Simplified: Simpler language for beginners
  - Visual-oriented: Emphasizes visual representations when applicable
  - Socratic: Guides through the solution with leading questions
- Powered by Mistral AI for accurate and helpful math solutions

## Requirements
- Python 3.7+
- Streamlit
- Requests
- Mistral AI API key

## Local Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements_for_deploy.txt
   ```
3. Set your Mistral AI API key as an environment variable:
   ```
   export MISTRAL_API_KEY="your-api-key"
   ```
4. Run the application:
   ```
   streamlit run app.py
   ```

## Deployment on Streamlit Cloud

### Step 1: Prepare Your GitHub Repository
1. Create a GitHub repository
2. Upload all the files from this project
3. Ensure you have the following files:
   - `app.py`
   - `utils.py`
   - `styles.py`
   - `.streamlit/config.toml`
   - `requirements.txt` (rename requirements_for_deploy.txt to requirements.txt)

### Step 2: Connect to Streamlit Cloud
1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub account
3. Click on "New app"
4. Select your repository, branch, and main file path (app.py)
5. Click "Deploy"

### Step 3: Set Up Secrets
1. Once deployed, go to your app settings
2. Find the "Secrets" section
3. Add your Mistral AI API key in toml format:
   ```
   MISTRAL_API_KEY = "your-mistral-api-key"
   ```
4. Save your secrets

### Step 4: Advanced Settings (Optional)
1. In app settings, you can customize:
   - App name
   - Theme
   - Python version (use 3.9+ for best compatibility)

### Step 5: Redeploy
1. After configuring secrets, click "Reboot app"

Your Math Problem Solver should now be live and accessible via the Streamlit Cloud URL!

## Troubleshooting Deployment Issues

### API Key Issues
- Verify your API key is correctly entered in the Streamlit secrets management
- Make sure there are no extra spaces or quotation marks
- Check if your Mistral AI account is active and the API key is valid

### Dependencies Problems
- If you see package-related errors, ensure requirements.txt has the correct versions:
  ```
  streamlit==1.44.1
  requests==2.32.3
  ```

### Port Configuration
- Streamlit Cloud handles port configuration automatically, so the port specified in config.toml is only for local development

### Application Errors
- Check the Streamlit Cloud logs for specific error messages
- Verify that all imported modules are included in requirements.txt
- Ensure file paths use forward slashes and are relative

## Updating Your App
To update your app after making changes:
1. Push changes to your GitHub repository
2. Streamlit Cloud will automatically detect changes and rebuild your app
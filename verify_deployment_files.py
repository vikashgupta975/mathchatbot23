"""
Deployment Verification Script

This script checks if all required files for deployment are present.
Run this before creating your GitHub repository.
"""

import os
import sys

# List of required files
REQUIRED_FILES = [
    "app.py",
    "utils.py",
    "styles.py",
    ".streamlit/config.toml",
    "requirements_for_deploy.txt",  # This will be renamed to requirements.txt
    "README.md",
    "DEPLOYMENT_GUIDE.md",
    "DEPLOYMENT_CHECKLIST.md"
]

# Optional files
OPTIONAL_FILES = [
    "secrets_example.toml",
    "generated-icon.png"
]

def check_files():
    """Check if all required files exist."""
    print("Checking required files for deployment...\n")
    
    missing_files = []
    for file_path in REQUIRED_FILES:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"✅ {file_path}")
    
    print("\nChecking optional files...")
    for file_path in OPTIONAL_FILES:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (optional)")
    
    if missing_files:
        print(f"\n❌ Missing {len(missing_files)} required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease create these files before proceeding with deployment.")
        return False
    else:
        print("\n✅ All required files are present!")
        print("\nREMINDER: When creating your GitHub repository, rename requirements_for_deploy.txt to requirements.txt")
        return True

def check_api_key_usage():
    """Check if API key is correctly handled in utils.py."""
    try:
        with open("utils.py", "r") as file:
            content = file.read()
            if "os.getenv(\"MISTRAL_API_KEY\")" in content:
                print("\n✅ API key is correctly accessed from environment variables")
            else:
                print("\n⚠️ Warning: Make sure API key is accessed via os.getenv(\"MISTRAL_API_KEY\")")
    except FileNotFoundError:
        print("\n❌ Could not check API key usage: utils.py not found")

if __name__ == "__main__":
    if check_files():
        check_api_key_usage()
        print("\nYour project is ready for deployment! Follow these steps:")
        print("1. Create a GitHub repository")
        print("2. Upload all files (rename requirements_for_deploy.txt to requirements.txt)")
        print("3. Deploy on Streamlit Cloud")
        print("4. Add your Mistral API key in Streamlit secrets management")
        print("\nSee DEPLOYMENT_GUIDE.md and DEPLOYMENT_CHECKLIST.md for detailed instructions.")
    else:
        sys.exit(1)
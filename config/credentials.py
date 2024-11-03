from dotenv import load_dotenv
import os

load_dotenv()

# LinkedIn API Credentials
LINKEDIN_API_KEY = os.getenv('LINKEDIN_API_KEY')
LINKEDIN_API_SECRET = os.getenv('LINKEDIN_API_SECRET')

# LinkedIn Login Credentials (for Selenium)
LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
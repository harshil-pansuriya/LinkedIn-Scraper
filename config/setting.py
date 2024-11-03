from dotenv import load_dotenv
import os

load_dotenv()

LINKEDIN_LOGIN_URL = os.getenv('LINKEDIN_LOGIN_URL')
LINKEDIN_SEARCH_URL = os.getenv('LINKEDIN_SEARCH_URL')


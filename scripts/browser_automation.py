from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

from config.credentials import LINKEDIN_USERNAME, LINKEDIN_PASSWORD
from config.setting import LINKEDIN_LOGIN_URL, LINKEDIN_SEARCH_URL
from utils.logger import setup_logger

logger = setup_logger(__name__)

#it will setup browser
def setup_browser():
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument('--incognito')
    browser_options.add_argument('--disable-notifications')
    browser = webdriver.Chrome(options=browser_options)
    browser.implicitly_wait(5)
    return browser

#login function
def login(browser):
    try:
        browser.get(LINKEDIN_LOGIN_URL)
        time.sleep(3)
        email_field = browser.find_element(By.ID, "username")
        email_field.send_keys(LINKEDIN_USERNAME)
        
        password_field = browser.find_element(By.ID, "password")
        password_field.send_keys(LINKEDIN_PASSWORD)
        
        login_button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
        login_button.click()
        logger.info("Logged in to LinkedIn")
        
    except Exception as e:
        logger.error(f"Login failed: {e}")
        browser.quit()
        raise

#search profile in linkedin
def search_profiles(first_name, last_name):
    browser = None
    try:
        browser = setup_browser()
        login(browser)
        
        search_url = LINKEDIN_SEARCH_URL.format(f"{first_name} {last_name}")
        browser.get(search_url)
        time.sleep(3)
        
        results = []
        profiles = browser.find_elements(By.CSS_SELECTOR, "li.reusable-search__result-container")[:10]
        
        for profile in profiles:
            try:
                data = extract_profile_data(profile)
                if data:
                    results.append(data)
                    if len(results) >= 5:
                        break
            except Exception as e:
                logger.warning(f"Failed to process profile: {e}")
                continue
        return results
    except Exception as e:
        logger.error(f"Search failed: {e}")
        raise
    finally:
        if browser:
            browser.quit()
            
# extract the profile data            
def extract_profile_data(profile):
    profile_html = profile.get_attribute('outerHTML')
    soup = BeautifulSoup(profile_html, 'html.parser')
    
    # skip linkedin promotions
    if 'premium-upsell' in profile.get_attribute('class'):
        return None
        
    name = soup.select_one('.entity-result__title-text span[aria-hidden="true"]')
    if not name or "LinkedIn Member" in name.text:
        return None
        
    job = soup.select_one('.entity-result__primary-subtitle')
    location = soup.select_one('.entity-result__secondary-subtitle')
    
    profile_info= {
        'name': name.text.strip(),
        'job_title': job.text.strip() if job else "N/A",
        'location': location.text.strip() if location else "N/A"
    }
    return profile_info
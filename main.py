import time
import os
import random
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from the .env file and retrieve credentials
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Store URL of activity
activityUrl = "https://anc.ca.apm.activecommunities.com/burnaby/activity/search/detail/50889?onlineSiteId=0&from_original_cui=true"

# Navigate to login page
driver = webdriver.Chrome()
loginPageUrl = "https://anc.ca.apm.activecommunities.com/burnaby/signin"
driver.get(loginPageUrl)

# Enter the email
email_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter your Email address"]')
email_input.send_keys(email)

# Enter the password
password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
password_input.send_keys(password)

api_key = os.getenv("CAPTCHA_API_KEY")
sitekey = "6LdJqskaAAAAAFsn-RktxwmkRKhBEoilSTX89roU"
solver = TwoCaptcha(api_key)
result = solver.recaptcha(
    sitekey=sitekey,
    url=loginPageUrl
)

print(f'Result: {result["code"]}')

# # Submit the form
# submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
# submit_button.click()

# Don't close the browser immediately
time.sleep(300)

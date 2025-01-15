from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twocaptcha import TwoCaptcha
import time
import os
from dotenv import load_dotenv

# Load environment variables from the .env file and retrieve credentials
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
api_key = os.getenv("CAPTCHA_API_KEY")

# Simple verification
print(f"Email: {email}")
print(f"Password: {password}")
print(f"API Key: {api_key}")

# Store URL of activity
activityUrl = "https://anc.ca.apm.activecommunities.com/burnaby/activity/search/detail/50889?onlineSiteId=0&from_original_cui=true"

# Navigate to login page
driver = webdriver.Chrome()
loginPageUrl = "https://anc.ca.apm.activecommunities.com/burnaby/signin"
driver.get(loginPageUrl)

# Fill in login credentials
email_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter your Email address"]')
email_input.send_keys(f"{email}")
password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
password_input.send_keys(f"{password}")

# Define sitekey and initialize solver
sitekey = "6LdJqskaAAAAAFsn-RktxwmkRKhBEoilSTX89roU"
solver = TwoCaptcha(api_key)
result = solver.recaptcha(
    sitekey=sitekey,
    url=loginPageUrl
)

print(f'Result: {result["code"]}')

# Send the captcha response to the reCAPTCHA response input
driver.execute_script("document.getElementById('g-recaptcha-response').value = '{}';".format(result['code']))

# Submit the form
submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_button.click()

# Don't close the browser immediately
time.sleep(300)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os 
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the email and password
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Simple verification
print(f"Email: {email}")
print(f"Password: {password}")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the specified URL
url = "https://anc.ca.apm.activecommunities.com/burnaby/activity/search/detail/50889?onlineSiteId=0&from_original_cui=true"
driver.get(url)

# Locate the "Sign In" button and click it
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign In")
sign_in_button.click()

# Locate the email input field and enter the email address
email_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter your Email address"]')
email_input.send_keys(f"{email}")

# Locate the password input field and enter the password
password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
password_input.send_keys(f"{password}")

# Don't close the browser immediately
time.sleep(300)


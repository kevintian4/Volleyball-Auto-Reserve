import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for using different locators

# Store URL of activity
activityUrl = "https://anc.ca.apm.activecommunities.com/burnaby/activity/search/detail/50889?onlineSiteId=0&from_original_cui=true"

# Navigate to login page
driver = webdriver.Chrome()
loginPageUrl = "https://anc.ca.apm.activecommunities.com/burnaby/signin"
driver.get(loginPageUrl)

# Load cookies from the saved file
with open("cookies.pkl", "rb") as cookie_file:
    cookies = pickle.load(cookie_file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Refresh the page to apply the cookies and be logged in
driver.refresh()

# Navigate to the activity page
driver.get(activityUrl)

# Use By.XPATH to locate the button and click it
submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_button.click()

# Don't close the browser immediately
time.sleep(300)

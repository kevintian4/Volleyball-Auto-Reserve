import time
import os
import pickle
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables from the .env file and retrieve credentials
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Initialize Selenium WebDriver
driver = webdriver.Chrome()
login_page_url = "https://anc.ca.apm.activecommunities.com/burnaby/signin"
driver.get(login_page_url)

# Fill in credentials
email_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter your Email address"]')
email_input.send_keys(email)
password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
password_input.send_keys(password)

# Click the reCAPTCHA checkbox
iframe = driver.find_element(By.XPATH, '//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(iframe)
captcha_checkbox = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
ActionChains(driver).move_to_element(captcha_checkbox).click().perform()
driver.switch_to.default_content()

# Popup function to prompt the user to click 'Done' after logging in
def prompt_user_to_continue():
    # Create a simple popup with a "Done" button
    root = tk.Tk()
    root.title("Login Confirmation")
    
    def on_done_button_click():
        # Save the cookies to a file
        cookies = driver.get_cookies()
        with open("cookies.pkl", "wb") as cookie_file:
            pickle.dump(cookies, cookie_file)
        root.destroy()  # Close the popup
    
    # Create the "Done" button
    done_button = tk.Button(root, text="Done", command=on_done_button_click)
    done_button.pack(pady=20)
    
    # Display the message
    label = tk.Label(root, text="Please solve the CAPTCHA and sign in.\nClick 'Done' ONLY AFTER you have logged in. \nYour cookies will be saved for future sessions and you will only need to run main.py next time.")
    label.pack(pady=10)
    label.pack(padx=10)
    
    # Show the popup
    root.mainloop()

# Wait for the user to click the "Done" button in the popup
prompt_user_to_continue()

print("Cookies saved successfully.")

import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

# Your credentials
USER_NAME = "example user"
ACCOUNT_EMAIL = "admin@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "admin123"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
# Keep Chrome browser open if script finishes or crashes
chrome_options.add_experimental_option("detach", True)
# Folder for the Chrome Profile selenium will use everytime
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to gym site
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

# Login as admin
login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# Fill in the form
email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

# Click to Log in
submit_button = driver.find_element(By.ID, "submit-button")
submit_button.click()
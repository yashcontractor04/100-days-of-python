import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load Environment Variables
load_dotenv()

# Login credentials
ACCOUNT_EMAIL = os.getenv("TINDOG_ACCOUNT_EMAIL")  # The email you registered with
ACCOUNT_PASSWORD = os.getenv("TINDOG_ACCOUNT_PASSWORD")  # The password you used during registration
TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/WDN8gp0fGI9oAY3SLVjIQcIzxWvB0cTw"

# Keep Chrome browser open if script finishes or crashes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# Navigate to Tindog site
driver.get(TINDOG_URL)

sleep(2)

# Open login modal and select social login option
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(1)
facebark_button = driver.find_element(By.CLASS_NAME, value='btn-facebark')
facebark_button.click()

# Switch driver focus to the pop-up login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Fill in user credentials
driver.find_element(By.XPATH, value='//*[@id="email"]').send_keys(ACCOUNT_EMAIL)
driver.find_element(By.XPATH, value='//*[@id="pass"]').send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

# Return back to main app window
driver.switch_to.window(base_window)
print(driver.title)

# Dismiss permissions/pop-ups
sleep(1)
driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button').click()
sleep(1)
# driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button[1]').click()
# sleep(1)
driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button[2]').click()
sleep(1)
driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button').click()
sleep(1)

# Like upto 20 profiles, handling match popups or slow-loading buttons along the way
for i in range(20):
    sleep(1)
    try:
        driver.find_element(By.CLASS_NAME, value='btn-like').click()
    except ElementClickInterceptedException:
        # Match pop-up - dismiss it to continue
        try:
            driver.find_element(By.CLASS_NAME, value='match-popup-link').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not yet loaded OR all dogs have been swiped
        sleep(2)

driver.quit()
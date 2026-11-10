import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Load environment variables
load_dotenv()

# Guaranteed speeds promised by ISP (in Mbps)
PROMISED_DOWN = 1000
PROMISED_UP = 1000

Y_USERNAME = os.getenv("Y_USERNAME")
Y_PASSWORD = os.getenv("Y_PASSWORD")
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"

class InternetSpeedXBot:
    def __init__(self):
        # Set Chrome options
        chrome_options = webdriver.ChromeOptions()
        # Keep the browser open after script runs
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 30)

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """Navigates to Speedtest.net, handles cookie prompts, runs test, and reads speeds."""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        # Reject cookie consent prompt
        self.driver.find_element(By.ID, "onetrust-reject-all-handler").click()

        # Click the "Go" button to start speed test
        go_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button")))
        go_button.click()

        # Wait for the test to complete
        time.sleep(45)

        try:
            self.down = float(
                self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3"))).text
            )
            self.up = float(self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/h3").text)

            print(f"Download Speed: {self.down}")
            print(f"Upload Speed: {self.up}")
        except ElementClickInterceptedException:
            # Dismiss overlay pop-up if it blocks reading the results
            self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/button/svg").click()

    def y_at_provider(self):
        """Logs into Y web app (clone of X) and posts a complaint."""
        self.driver.get("https://app.100daysofpython.dev/services/y")
        time.sleep(1)

        # Open login modal and submit credentials
        self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "y-login-link"))).click()
        time.sleep(2)
        self.wait.until(ec.presence_of_element_located((By.ID, "email"))).send_keys(Y_USERNAME)
        self.driver.find_element(By.ID, "password").send_keys(Y_PASSWORD, Keys.ENTER)
        time.sleep(3)

        # Compose post text and send
        post_text = f"Hey Internet Provider, why is my internet speed {self.down} Mbps down/{self.up} Mbps up when I pay for {PROMISED_DOWN} Mbps down/{PROMISED_UP} Mbps up?"
        self.driver.find_element(By.ID, "tweet-compose").send_keys(post_text)
        time.sleep(1)
        self.wait.until(ec.element_to_be_clickable((By.ID, "post-btn"))).click()
        # self.driver.find_element(By.ID, "modal-post-btn").click()
        time.sleep(2)
        self.driver.quit()

def main():
    bot = InternetSpeedXBot()
    bot.get_internet_speed()

    # Trigger complaint post if either download or upload speed falls below promised thresholds
    if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
        print("Internet Speed is below promised limits. Posting complaint on Y...")
        bot.y_at_provider()
    else:
        print("It's all good")
        bot.driver.quit()

if __name__ == "__main__":
    main()
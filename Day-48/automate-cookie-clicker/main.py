import os
from time import time, sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# Setup chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Optional: custom profile path if you want browser settings/cookies to persist natively
# chrome_options.add_argument("--user-data-dir=/path/to/custom/selenium/profile")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")
sleep(3)    # Page loading

# Restore saved progress from saved_progress.txt if it exists
if os.path.exists("saved_progress.txt"):
    try:
        with open("saved_progress.txt", "r") as f:
            saved_code = f.read().strip()
        if saved_code:
            # Inject saved string into localStorage and reload page to apply it
            driver.execute_script(f"localStorage.setItem('CookieClickerGame', '{saved_code}');")
            driver.refresh()
            sleep(3)
            print("Loaded progress from saved_progress.txt")
    except Exception as e:
        print(f"Could not load saved file: {e}")

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    english = driver.find_element(By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    english.click()
    sleep(3)    # more loading
except NoSuchElementException:
    print("Language selection not found")

sleep(2)

cookie_button = driver.find_element(By.ID, value="bigCookie")

item_ids = [f"product{i}" for i in range(20)]

wait_time = 5
# Check for purchase every 5 seconds
timeout = time() + wait_time
# Run for a total of 5 minutes
five_min = time() + 5 * 60

# Word-to-multiplier mapping for large numbers
multipliers = {
    "million": 1e6,
    "billion": 1e9,
    "trillion": 1e12,
    "quadrillion": 1e15,
}

while True:
    cookie_button.click()

    # Every 5 seconds, buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Clean string format (handles "999,999" and "1.000 million")
            raw_text = driver.find_element(By.ID, value="cookies").text.split("\n")[0]
            parts = raw_text.split(" ")
            count_val = float(parts[0].replace(",", ""))

            # Apply scale multiplier if suffix is present
            if len(parts) > 1 and parts[1].lower() in multipliers:
                count_val *= multipliers[parts[1].lower()]

            # Get current cookie count
            cookie_count = int(count_val)

            # Find all available products in store
            products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            # Start from the bottom
            for product in reversed(products):
                # Check if the item/product is available and affordable (enables class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time

    # Stop after 5 minutes and saved progress
    if time() > five_min:
        try:
            cookie_element = driver.find_element(By.ID, value="cookies")
            print(f"Final result: {cookie_element.text}")

            # Trigger in-game save and extract localStorage data to saved_progress.txt
            saved_code = driver.execute_script("return localStorage.getItem('CookieClickerGame');")
            if saved_code:
                with open("saved_progress.txt", "w") as f:
                    f.write(saved_code)
                print("Saved game progress to saved_progress.txt")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break

driver.quit()
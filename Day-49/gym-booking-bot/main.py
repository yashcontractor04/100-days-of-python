import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# Load Environment Variables
load_dotenv()

# Read credentials from environment variables
USERNAME = "example_user"
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
# Keep Chrome open after completion/error for manual checking
chrome_options.add_experimental_option("detach", True)

# Save Chrome profile in repo directory to retain session state
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)
wait = WebDriverWait(driver, 2)

def retry(func, retries=7, description=None):
    """Retries flaky network or DOM actions up to `retries` times."""
    for attempt in range(retries):
        try:
            print(f"Trying {description}. Attempt: {attempt + 1}")
            return func()
        except Exception as e:
            print(f"[{description}] Attempt {attempt + 1} failed. Retrying... (Error: {e})")
            time.sleep(2)

    print(f"[{description}] Completely failed after {retries} attempts.")
    return None

def login():
    """Logs into the gym portal and waits for the schedule page to render."""
    login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)
    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)
    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    # Raise error if simulated network failure occurs on login
    try:
        wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    except TimeoutException:
        raise Exception("Schedule page did not load")

def book_class(target_button):
    """Clicks a booking or waitlist button and waits for DOM state to update."""
    target_button.click()
    wait.until(lambda d: target_button.text in ["Booked", "Waitlisted"])

# Authenticate with retries
retry(login, retries=7, description="User Login")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
processed_classes = []

for card in class_cards:
    # Extract day header from parent container
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Target Tuesday and Thursday 6:00 PM slots
    if 'Tue' in day_title or 'Thu' in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if '6:00 PM' in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            book_button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            class_info = f"{class_name} on {day_title}"

            if book_button.text == "Booked":
                already_booked_count += 1
                print(f"✓ Already booked: {class_info}")
                processed_classes.append(f"[Booked] {class_info}")

            elif book_button.text == "Waitlisted":
                already_booked_count += 1
                print(f"✓ Already on waitlist: {class_info}")
                processed_classes.append(f"[Waitlisted] {class_info}")

            elif book_button.text == "Join Waitlist":
                if retry(lambda: book_class(book_button), description="Waitlisting") is not None:
                    waitlist_count += 1
                    print(f"✓ Joined Waitlist for: {class_info}")
                    processed_classes.append(f"[New Waitlist] {class_info}")
                    time.sleep(0.5)

            elif book_button.text == "Book Class":
                if retry(lambda: book_class(book_button), description="Booking") is not None:
                    booked_count += 1
                    print(f"✓ Booked: {class_info}")
                    processed_classes.append(f"[New Booking] {class_info}")
                    time.sleep(0.5)

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---\n")
print("--- VERIFYING ON MY BOOKINGS PAGE ---")

def get_my_bookings():
    """Navigates to My Bookings and fetches booked class elements."""
    my_bookings = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings.click()
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards

# Fetch verified bookings list using retry logic
all_cards = retry(get_my_bookings, description="Get my bookings") or []
verified_count = 0

for booking in all_cards:
    try:
        when_paragraph = booking.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ('Tue' in when_text or 'Thu' in when_text) and '6:00 PM' in when_text:
            class_name = booking.find_element(By.TAG_NAME, "h3").text
            print(f"✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if verified_count != total_booked:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")
else:
    print("✅ SUCCESS: All bookings verified!")

driver.quit()

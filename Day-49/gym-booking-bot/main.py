import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Load environment variables
load_dotenv()

# Read credentials from environment variables
USER_NAME = "example user"
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")  # The email you registered with
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")  # The password you used during registration
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

def retry(func, retries=7, description=None):
    """Retries flaky network or DOM actions up to `retries` times."""
    for attempt in range(retries):
        try:
            # Try to execute the function
            print(f"Trying {description}. Attempt: {attempt + 1}")
            return func()
        except Exception as e:
            print(f"[{description}] Attempt {attempt + 1} failed. Retrying... (Error: {e})")
            time.sleep(2)  # moment to recover

    print(f"[{description}] Completely failed after {retries} attempts.")
    return None


# Step 2: Log in
def login():
    """Logs into the gym portal and waits for the schedule page to render."""
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

    # Verify login success
    try:
        wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    except TimeoutException:
        # If the page didn't load, the network simulated a fail. Raise an error to trigger a retry.
        raise Exception("Schedule page did not load")


# Step 3: Book/Join Waitlist the next available class on Tuesday 6 pm
def book_class(booking_button):
    """Clicks a booking or waitlist button and waits for DOM state to update."""
    book_button.click()
    wait.until(lambda d: book_button.text == "Booked")

retry(login, retries=7, description="User Login")

# Counters for booked classes for the booking summary
booked_count = 0
waitlist_count = 0
already_booked_count = 0

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

processed_classes = []

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Step 6: Book every class on Tuesday and Thursday and print class list
    # Check if this is a tuesday or thursday
    if 'Tue' in day_title or 'Thu' in day_title:
        # Check if the class is at 6 pm
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if '6:00 PM' in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            # Find and click the Book Class/Join Waitlist button
            book_button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            # Track class details
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
                # Use retry for entire waitlist action
                retry(lambda: book_class(book_button), description="Waitlisting")
                waitlist_count += 1
                book_button.click()
                print(f"✓ Joined Waitlist for: {class_info}")
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist] {class_info}")
                # Wait a moment for the button state to update
                time.sleep(0.5)
            elif book_button.text == "Book Class":
                # Use retry for entire booking action
                retry(lambda: book_class(book_button), description="Booking")
                book_button.click()
                print(f"✓ Booked: {class_info}")
                booked_count += 1
                processed_classes.append(f"[New Booking] {class_info}")
                # Wait a moment for the button state to update
                time.sleep(0.5)

total_booked = already_booked_count + booked_count + waitlist_count
print(f"--- Total Tuesday/Thursday 6pm classes: {total_booked} ---\n")
print("--- VERIFYING ON MY BOOKINGS PAGE ---")


# Step 7: Verify booking from My Bookings tab
def get_my_bookings():
    """Navigates to My Bookings and fetches booked class elements."""
    my_bookings = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings.click()
    # Wait for My Bookings page to load
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    # Ensure we actually found cards - if empty, the page might not have loaded
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards

# Put navigation to the Bookings page and get cards in the retry wrapper
all_cards = retry(get_my_bookings, description="Get my bookings")
# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

for booking in all_cards:
    try:
        when_paragraph = booking.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if the cards (when) has a class on Tuesday/Thursday at 6:00 PM
        if ('Tue' in when_text or 'Thu' in when_text) and '6:00 PM' in when_text:
            class_name = booking.find_element(By.TAG_NAME, "h3").text
            print(f"✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip
        pass

print("--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if verified_count != total_booked:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")
else:
    print(f"✅ SUCCESS: All bookings verified!")

driver.quit()

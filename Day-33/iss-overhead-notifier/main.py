import os
import time
from dotenv import load_dotenv
import requests
from datetime import datetime, timezone
import smtplib

# Load local environment variables (.env)
load_dotenv()

# Coordinates for Berlin, Germany
MY_LAT = 55.516651
MY_LONG = 18.335524

# Shared email credentials
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_EMAIL_PASSWORD")

def iss_within_bounds():
    """Queries Open-Notify API to check if the ISS coordinates fall within +/- 5 degrees of the target coordinates."""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])

    lat_diff = abs(iss_latitude - MY_LAT)
    lng_diff = abs(iss_longitude - MY_LONG)

    return lat_diff <= 5 and lng_diff <= 5


def is_dark():
    """Queries Sunrise-Sunset API in UTC format and checks whether current UTC hour falls during nighttime."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        'formatted' : 0
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    # Sunrise & Sunset are returned as UTC timestamps: 'YYYY-MM-DDTHH:MM:SS+00:00'
    sunrise_utc = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset_utc = int(data["results"]["sunset"].split('T')[1].split(':')[0])

    # Current UTC hour for an accurate comparison
    current_utc_hour = datetime.now(timezone.utc).hour

    # Nighttime occurs after sunset or before sunrise
    return current_utc_hour >= sunset_utc or current_utc_hour <= sunrise_utc


def send_notification() -> None:
    """Dispatches email notification alerting user to look up."""
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        message = (
            f"From: {MY_EMAIL}\r\n"
            f"To: {MY_EMAIL}\r\n"
            f"Subject: Look Up 👆\r\n\r\n"
            f"The ISS is overhead in your night sky! Step outside and look up."
        )
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.encode("utf-8")
        )
    print("Notification email sent successfully!")


# Main execution polling loop (intended for local continuous run)
if __name__ == "__main__":
    print("Monitoring ISS location...")
    while True:
        try:
            if iss_within_bounds() and is_dark():
                print("ISS is overhead in darkness! Sending email...")
                send_notification()
            else:
                print("ISS not nearby or currently daytime. Polling again in 60s...")
        except requests.RequestException as e:
            print(f"Network error during polling: {e}")

        time.sleep(60)
import os
import smtplib
import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    """Dispatches formatted flight deal notifications via Telegram and Gmail."""
    def __init__(self):
        self.bot_token = os.environ.get("TELEGRAM_FLIGHT_BOT_TOKEN")
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        self.my_email = os.environ.get("MY_EMAIL")
        self.email_password = os.environ.get("MY_EMAIL_PASSWORD")

    def send_flight_alerts(self, flight_data, old_price: float) -> None:
        """Sends a formatted flight deal message to your Telegram account."""
        if not self.bot_token or not self.chat_id:
            print("Telegram credentials missing. Skipping notification.")
            return

        savings = old_price - flight_data.price if old_price != float("inf") else 0

        message = (
            f"✈️ *Low Price Flight Alert!*\n\n"
            f"*Route:* {flight_data.origin_city} ➡️ {flight_data.destination_city}\n"
            f"*Dates:* {flight_data.out_date} to {flight_data.return_date}\n"
            f"*New Price:* €{flight_data.price}\n"
            f"*Previous Price:* €{old_price}\n"
            f"*Savings:* €{savings}\n"
            f"*Duration:* {flight_data.duration} hrs\n"
        )

        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }

        try:
            response = requests.post(self.api_url, data=payload)
            response.raise_for_status()
            print(f"Telegram alert sent for {flight_data.destination_city}!")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send Telegram alert: {e}")

    def send_emails(self, email_list: list, flight_data, old_price: float) -> None:
        """Broadcasts deal details to all registered user emails using smtplib."""
        if not self.my_email or not self.email_password or not email_list:
            print("Email credentials or user list missing. Skipping email dispatch.")
            return

        savings = old_price - flight_data.price if old_price != float("inf") else 0
        subject = f"Low Price Flight Alert: {flight_data.origin_city} to {flight_data.destination_city}!"
        body = (
            f"Low Price Flight Alert!\n\n"
            f"Route: {flight_data.origin_city} to {flight_data.destination_city}\n"
            f"Dates: {flight_data.out_date} to {flight_data.return_date}\n"
            f"New Price: EUR {flight_data.price}\n"
            f"Previous Price: EUR {old_price}\n"
            f"Savings: EUR {savings}\n"
            f"Flight Duration: {flight_data.duration} hrs\n"
        )
        message = f"Subject:{subject}\n\n{body}"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.email_password)
                for email in email_list:
                    connection.sendmail(
                        from_addr=self.my_email,
                        to_addrs=email,
                        msg=message.encode("utf-8"),
                    )
            print(f"Flight deal emails sent to {len(email_list)} members.")
        except Exception as e:
            print(f"Failed to send emails: {e}")

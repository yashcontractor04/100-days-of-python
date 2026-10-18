import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    """Dispatches formatted flight deal notifications via Telegram Bot HTTP API."""
    def __init__(self):
        self.bot_token = os.environ.get("TELEGRAM_FLIGHT_BOT_TOKEN")
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

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
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'Markdown',
        }

        try:
            response = requests.post(self.api_url, data=payload)
            response.raise_for_status()
            print(f"Telegram alert sent for {flight_data.destination_city}!")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send Telegram alert: {e}")
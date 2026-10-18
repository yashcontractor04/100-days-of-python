import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:
    """Handles read and write interactions with Google Sheets via Sheety REST API."""
    def __init__(self):
        # self.data = None
        self.api_endpoint = "https://api.sheety.co/54e10fae340fc530e5e332be4a63d7c8/flightPriceTracker/prices"
        self.BEARER_TOKEN = os.environ.get("SHEETY_FLIGHT_BEARER_TOKEN")
        self.auth = {'Authorization': f'Bearer {self.BEARER_TOKEN}'}
        self.destination_data = {}

    def get_row_data(self) -> list:
        """Retrieves all route rows from the target Google Sheet."""
        response = requests.get(self.api_endpoint, headers=self.auth)
        response.raise_for_status()

        # Log cache usage status if requests_cache is active
        print(f"Sheety data loaded from cache: {getattr(response, 'from_cache', False)}")

        return response.json().get("prices", [])

    def update_lowest_price(self, row_id: int, new_price: float, new_duration: float) -> None:
        """Updates both lowestPrice and duration fields for a specific row in Google Sheets via Sheety."""
        put_url = f"{self.api_endpoint}/{row_id}"
        data = {
            'price': {
                'lowestPrice': new_price,
                # Ensures duration is sent as a float in hours
                "duration": float(new_duration),
            }
        }
        response = requests.put(put_url, headers=self.auth, json=data)
        response.raise_for_status()
        print(f"Row {row_id} updated successfully: {response.text}")
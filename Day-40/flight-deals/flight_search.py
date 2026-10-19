import os
import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    """Queries live Google Flights route prices via SerpAPI."""
    def __init__(self):
        self.serp_endpoint = "https://serpapi.com/search"
        self.api_key = os.environ.get("SERPAPI_API_KEY")

    def check_flights(self, origin_city: str, destination_city: str, from_date: str, to_date: str) -> dict:
        """Executes a round-trip Google Flights search query via SerpAPI."""
        if not self.api_key:
            print("Missing SERPAPI_API_KEY environment variable.")
            return {}
        query = {
            'engine': 'google_flights',
            'departure_id': origin_city,
            'arrival_id': destination_city,
            'outbound_date': from_date,
            'return_date': to_date,
            'type': '1',
            'adults': '1',
            'currency': 'EUR',
            'api_key': self.api_key,
        }

        try:
            response = requests.get(self.serp_endpoint, params=query)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"SerpAPI flight search request failed for {destination_city}: {e}")
            return {}

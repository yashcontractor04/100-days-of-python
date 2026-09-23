import os
import requests
from dotenv import load_dotenv

# Load local environment variables from .env
load_dotenv()

# Coordinates for Berlin, Germany
MY_LAT = 55.516651
MY_LONG = 18.335524

# OpenWeatherMap 5-day / 3-hour forecast endpoint
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
OWM_API_KEY = os.environ.get("OWM_API_KEY")

# Telegram Bot credentials
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Ingest next 12 hours of forecast data (4 timestamps * 3 hours per block)
weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': OWM_API_KEY,
    'cnt': 4,
}

def send_telegram_message(text: str):
    """Dispatches a push notification via the Telegram Bot HTTP API."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
    }
    tg_response = requests.post(url, json=payload)
    tg_response.raise_for_status()
    print("Telegram alert sent successfully.!")

def check_rain_forecast() -> None:
    """Queries OpenWeatherMap and alerts via Telegram if rain is predicted."""
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()

    # Weather condition codes < 700 signify Thunderstorm (2xx), Drizzle (3xx), Rain (5xx), or Snow (6xx)
    will_rain = any(
        int(hour["weather"][0]["id"]) < 700 for hour in weather_data["list"]
    )

    if will_rain:
        message = (
            "Rain Alert ☔️\n\n"
            "Precipitation is forecasted in your area within the next 12 hours. "
            "Don't forget to grab an umbrella before heading out!"
        )
        send_telegram_message(message)
    else:
        print("No rain forecasted in the upcoming 12 hours.")

if __name__ == "__main__":
    check_rain_forecast()

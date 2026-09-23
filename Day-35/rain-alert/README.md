# Automated Rain Alert with Telegram Bot API
An automated meteorological alert script that queries the OpenWeatherMap 5-day/3-hour forecast API for precipitation condition codes (< 700) across the upcoming 12 hours. Triggers push notifications via the Telegram Bot API over HTTPS.

### Tech / Concepts
* REST API parameter handling & pagination using `requests`
* Weather condition classification using OpenWeather standard condition codes
* Automated push messaging with Telegram Bot HTTP endpoints (`sendMessage`)
* Secure credential management via `dotenv` and environment variables

### Quickstart
1. Install dependencies from the repository root:
   `pip install -r requirements.txt`
2. Populate `.env`:
   ```text
   OWM_API_KEY=your_openweathermap_api_key
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_numeric_chat_id
3. Run the script:
   `python main.py`

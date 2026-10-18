# Automated Flight Deal Finder
A live flight price monitoring service built with Python, SerpAPI (Google Flights engine), Sheety API, and the Telegram Bot API. Continuously monitors targeted international flight routes stored in a Google Sheet, compares live ticket quotes against historical baseline prices, updates price logs upon discovering cheaper options, and dispatches real-time push deal alerts via Telegram.

### Tech / Concepts
* Live flight telemetry extraction using `SerpAPI` (Google Flights engine)
* RESTful sheet row synchronization using `Sheety API`
* Automated push notifications via `Telegram Bot API`
* Local API response caching using `requests-cache` to protect query quotas
* Dynamic price difference calculations and baseline mutation

### Quickstart
1. Ensure dependencies are installed from root:
   `pip install -r requirements.txt`
2. Create `.env` inside `Day-39/flight-deals/`:
   ```text
   SERPAPI_API_KEY=your_serpapi_key
   SHEETY_FLIGHT_BEARER_TOKEN=your_sheety_token
   TELEGRAM_FLIGHT_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_numeric_chat_id
3. Run the script:
   `python main.py`

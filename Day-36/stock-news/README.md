# Stock Trading News Alert Service
An automated market-monitoring script that tracks significant daily price fluctuations for equities (e.g., TSLA) using the Alpha Vantage API. When closing prices change by 5% or more across consecutive trading sessions, the service fetches the top three relevant headlines from NewsAPI and delivers formatted push notifications via the Telegram Bot HTTP API.

### Tech / Concepts
* Multi-source REST API orchestration (`Alpha Vantage`, `NewsAPI`, `Telegram Bot API`)
* Time series extraction & percentage difference delta calculation
* Defensive JSON payload parsing to handle API rate limiting
* Asynchronous push notification distribution using HTTP POST payloads

### Quickstart
1. Install dependencies from the repository root:
   `pip install -r requirements.txt`
2. Configure `.env`:
   ```text
   STOCK_API_KEY=your_alphavantage_key
   NEWS_API_KEY=your_newsapi_key
   TELEGRAM_STOCK_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
3. Run the script:
   `python main.py`

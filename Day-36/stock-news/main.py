import os
import requests
from typing import List
from dotenv import load_dotenv

load_dotenv()

# Configuration constants
STOCK = "PLTR"
COMPANY_NAME = "Palantir"
PERCENT_THRESHOLD = 5.0

# API endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Environment credentials
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_STOCK_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news() -> List[dict]:
    """Queries NewsAPI for the top 3 recent news articles related to the company."""
    params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])[:3]
    return articles


def send_tele_messages(articles: List[dict], percentage_change: float) -> None:
    """Dispatches a formatted push notification via Telegram for each article."""
    direction = "🔺" if percentage_change >= 0 else "🔻"
    abs_change = round(abs(percentage_change))
    header = f"{STOCK}: {direction}{abs_change}%"

    for article in articles:
        title = article.get("title", "No Title")
        description = article.get("description", "No Description")
        message_body = (
            f"{header}\n"
            f"Headline: {title}\n"
            f"Brief: {description}\n"
        )
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message_body,
        }
        tg_response = requests.post(url, json=payload)
        tg_response.raise_for_status()

    print("News alerts sent successfully.!")


def check_stock_fluctuation() -> None:
    """Calculates daily price delta and triggers news alerts if threshold is exceeded."""
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'outputsize': 'compact',
        'apikey': STOCK_API_KEY,
    }

    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()

    # Defensive check against API rate limits or invalid keys
    if "Time Series (Daily)" not in data:
        print(f"Error fetching stock pdata: {data.get('Note') or data.get('Error Message') or 'Unknown Error'}")
        return

    daily_data = data["Time Series (Daily)"]
    # Alpha Vantage returns chronological dates as keys; extracting top 2 recent sessions
    time_series_list = list(daily_data.values())
    yesterday_close = float(time_series_list[0]["4. close"])
    day_before_close = float(time_series_list[1]["4. close"])

    # Relative percentage fluctuation calculation
    price_diff = yesterday_close - day_before_close
    percent_change = (price_diff / day_before_close) * 100

    print(f"{STOCK} price changed by {percent_change:+.2f}% (Yesterday: {yesterday_close:+.2f}, Day Before: ${day_before_close:+.2f})")

    # Evaluate absolute percentage change against threshold
    if abs(percent_change) >= PERCENT_THRESHOLD:
        print(f"Threshold exceeded (>= {PERCENT_THRESHOLD}%). Fetching market news...")
        articles = get_news()
        if articles:
            send_tele_messages(articles, percent_change)
        else:
            print("No relevant news articles found.")
    else:
        print(f"Fluctuation is within normal range. No alerts sent")


if __name__ == "__main__":
    check_stock_fluctuation()


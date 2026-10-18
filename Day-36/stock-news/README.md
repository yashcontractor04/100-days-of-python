# Day 36: Stock News Alert

Watches one stock, currently Palantir (`PLTR`). To watch a different one, change `STOCK` and `COMPANY_NAME` at the top of `main.py`.

It compares the last two daily closing prices from Alpha Vantage. If the price moved 5% or more up or down, it gets the three newest news articles about the company from NewsAPI and sends them to you on Telegram, with a red or green arrow and the percentage.

If Alpha Vantage doesn't send any prices (for example a wrong key, or you used up the free limit), the program prints an error and stops.

## Setup

Create a file called `.env` in this folder:

```text
STOCK_API_KEY=your_alphavantage_key
NEWS_API_KEY=your_newsapi_key
TELEGRAM_STOCK_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

To run it: `python main.py`

## It also runs by itself

A GitHub Actions workflow (`.github/workflows/day_36_stock_news.yml`) runs it Monday to Friday at 21:00 UTC, which is after the US stock market closes. The keys are saved as "secrets" in the GitHub repository settings. You can also start it by hand from the Actions tab.

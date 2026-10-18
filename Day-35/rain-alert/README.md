# Day 35: Rain Alert

Checks the weather forecast and sends you a Telegram message if rain is coming. It asks OpenWeatherMap for the next 12 hours (four forecasts, 3 hours apart). If any of them has a weather code under 700, which means thunderstorm, drizzle, rain or snow, it tells you to take an umbrella.

My location is set at the top of `main.py` (`MY_LAT` and `MY_LONG`) and is currently Berlin.

## Setup

You need a free OpenWeatherMap key and a Telegram bot (you make one by chatting with Telegram's BotFather). You also need the number ID of your chat with the bot. Put them in a file called `.env` in this folder:

```text
OWM_API_KEY=your_openweathermap_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

To run it: `python main.py`. It checks once and then stops. It isn't set up to run on a schedule.

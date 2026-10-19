# Day 40: Flight Club

Looks for cheap flights and emails a list of people when it finds a deal. It does everything the Day 39 project does, but it also reads user emails from a second tab in the Google Sheet and sends them all an email via Gmail.

To read and write the Google Sheet it uses Sheety, a service that lets Python work with a Google Sheet.

The code is split into small files:

- `main.py`: goes through each route and ties everything together
- `data_manager.py`: reads and updates the sheet, and gets the user emails
- `flight_search.py`: asks SerpAPI for flights
- `flight_data.py`: the `FlightData` class and `find_cheapest_flight()`, which picks the cheapest flight from the answer
- `notification_manager.py`: sends the Telegram message and the emails

`main.py` also turns on a cache (a short term memory for answers) for one hour. This way, running the program again and again while testing doesn't use up your free SerpAPI searches. It also applies to the sheet, so a change you just made in the sheet can take up to an hour to show up.

## Setup

- The sheet needs a `prices` tab with the columns as described in [Day-39 README](../../Day-39/flight-deals/README.md) and a `users` tab with an `email` column.
- The Sheety links in `data_manager.py` point to my own sheet. Replace them with yours.
- Create a file called `.env` in this folder:

 ```text
 SERPAPI_API_KEY=your_serpapi_key
 SHEETY_FLIGHT_BEARER_TOKEN=your_sheety_token
 TELEGRAM_FLIGHT_BOT_TOKEN=your_bot_token
 TELEGRAM_CHAT_ID=your_chat_id
 MY_EMAIL=you@gmail.com
 MY_EMAIL_PASSWORD=your_gmail_app_password
 ```
To run it: `python main.py`

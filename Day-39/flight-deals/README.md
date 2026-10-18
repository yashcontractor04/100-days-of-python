# Day 39: Flight Deal Finder

Looks for cheap flights. The routes you care about are saved in a Google Sheet. For each route, the program asks SerpAPI (a service that gives Python access to Google Flights) for round trip prices in euros and picks the cheapest one. If it is cheaper than the `lowestPrice` saved in the sheet, the program updates the sheet and sends you a Telegram message with the route, dates, old price, new price, how much you save and the flight duration.

To read and write the Google Sheet it uses Sheety, a service that lets Python work with a Google Sheet.

The code is split into small files:

- `main.py`: goes through each route and ties everything together
- `data_manager.py`: reads and updates the sheet
- `flight_search.py`: asks SerpAPI for flights
- `flight_data.py`: the `FlightData` class and `find_cheapest_flight()`, which picks the cheapest flight from the answer
- `notification_manager.py`: sends the Telegram message

`main.py` also turns on a cache (a short term memory for answers) for one hour. This way, running the program again and again while testing doesn't use up your free SerpAPI searches. It also applies to the sheet, so a change you just made in the sheet can take up to an hour to show up.

## Setup

- The sheet needs these columns: `departure` and `arrival` (airport codes like `BER`), `from` and `to` (dates written as `YYYY-MM-DD`), `lowestPrice` and `duration`.
- The Sheety link in `data_manager.py` points to my own sheet. Replace it with yours.
- Create a file called `.env` in this folder:

  ```text
  SERPAPI_API_KEY=your_serpapi_key
  SHEETY_FLIGHT_BEARER_TOKEN=your_sheety_token
  TELEGRAM_FLIGHT_BOT_TOKEN=your_bot_token
  TELEGRAM_CHAT_ID=your_chat_id
  ```

To run it: `python main.py`

There is also a GitHub Actions workflow (`.github/workflows/day_39_flight_deals.yml`) that can run it, but it only starts when you click the button yourself in the Actions tab.

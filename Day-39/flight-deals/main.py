import time
import requests_cache

# Enable 1-hour response caching to preserve API quota during local testing
requests_cache.install_cache(
    cache_name='flight_cache',
    expire_after=3600,
)

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


def main() -> None:
    """Coordinates row retrieval from Google Sheets, queries SerpAPI for live flights, updates lowest prices, and triggers Telegram alerts for deals."""
    data_manager = DataManager()
    sheet_data = data_manager.get_row_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    # Iterate through every route/row in the sheet
    for row in sheet_data:
        origin_city = row.get("departure")
        destination_city = row.get("arrival")
        from_date = row.get("from")
        to_date = row.get("to")
        row_id = row.get("id")
        current_lowest_price = row.get("lowestPrice", float("inf"))

        # Search flights via SerpAPI
        raw_flight_response = flight_search.check_flights(
            origin_city=origin_city,
            destination_city=destination_city,
            from_date=from_date,
            to_date=to_date,
        )

        # Parse the cheapest flight option
        cheapest = find_cheapest_flight(raw_flight_response, return_date=to_date)

        if cheapest.price == 'N/A':
            print(f'Skipping {destination_city}: No valid flight options found.\n')
            continue

        print(f'Cheapest found for {destination_city}: EUR {cheapest.price} (Duration: {cheapest.duration} hrs)')

        # Check if a cheaper deal was found
        if cheapest.price < current_lowest_price:
            print(f'🔥 Deal found! Updating sheet (New: EUR {cheapest.price} vs Old: EUR {current_lowest_price}).')
            data_manager.update_lowest_price(
                row_id=row_id,
                new_price=cheapest.price,
                new_duration=cheapest.duration,
            )
            # Send Telegram Alert
            notification_manager.send_flight_alerts(
                flight_data=cheapest, old_price=current_lowest_price
            )
        else:
            print(f'No cheaper deal (Current lowest recorded: EUR {current_lowest_price}).')

        print('-' * 40)

        # Delay between requests
        time.sleep(1)

    print('\nAll routes processed successfully!')


if __name__ == '__main__':
    main()

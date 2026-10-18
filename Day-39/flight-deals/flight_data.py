from typing import Any, Dict


class FlightData:
    """Structured container for single flight route offer attributes."""

    def __init__(
            self,
            price: Any,
            origin_city: str,
            destination_city: str,
            out_date: str,
            return_date: str,
            duration: float = 0.0
    ):
        self.price = price
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.out_date = out_date
        self.return_date = return_date
        self.duration = duration


def find_cheapest_flight(data: Dict[str, Any], return_date: str) -> FlightData:
    """Parses SerpAPI Google Flights response dict to locate the absolute lowest priced offer."""
    # In case API returned None or error
    if not data:
        print("No flight data returned from API.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # Combine best_flights and other_flights returned from SerpAPI
    best_flights = data.get("best_flights", [])
    other_flights = data.get("other_flights", [])
    all_flights = best_flights + other_flights

    if not all_flights:
        print("No flights available for this route/date.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    cheapest_flight_data = None
    lowest_price = float("inf")

    # Iterate through flights to find the lowest price
    for flight in all_flights:
        try:
            # Skip if price key is missing
            if "price" not in flight:
                continue

            price = flight["price"]
            if price < lowest_price:
                lowest_price = price
                cheapest_flight_data = flight

        except (KeyError, TypeError):
            continue

    if not cheapest_flight_data:
        print("No valid priced flights found.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # Parse details from flight segments
    flights_list = cheapest_flight_data.get("flights", [])
    origin_city = flights_list[0]["departure_airport"]["id"]
    destination_city = flights_list[-1]["arrival_airport"]["id"]
    # '2026-12-21 15:05' -> '2026-12-21' using split()
    out_date = flights_list[0]["departure_airport"]["time"].split(" ")[0]

    # total_duration in minutes; converted to float hours (rounded)
    total_minutes = cheapest_flight_data.get("total_duration", 0)
    duration_hours = round(float(total_minutes) / 60.0, 1)

    return FlightData(
        price=lowest_price,
        origin_city=origin_city,
        destination_city=destination_city,
        out_date=out_date,
        return_date=return_date,
        duration=duration_hours
    )

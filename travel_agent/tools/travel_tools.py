"""ADK function tools: call mock APIs for flights, hotels, activities."""

from __future__ import annotations

from travel_agent.mock_apis import flights as mock_flights
from travel_agent.mock_apis import hotels as mock_hotels
from travel_agent.mock_apis import places as mock_places


def search_flights(
    origin: str,
    destination: str,
    date_preference: str = "",
    budget: str = "moderate",
    max_results: int = 4,
) -> str:
    """Search for flights from origin to destination.

    Args:
        origin: Departure city (e.g. Pune, Mumbai).
        destination: Arrival city (e.g. Goa, Delhi).
        date_preference: Preferred date or day (e.g. Friday night).
        budget: budget, moderate, or luxury.
        max_results: Maximum number of options to return (default 4).
    """
    results = mock_flights.search_flights_mock(
        origin=origin,
        destination=destination,
        date_preference=date_preference,
        budget=budget,
        max_results=max_results,
    )
    if not results:
        return "No flights found for this route."
    return "\n".join(
        f"- {r['airline']}: {r['departure']} → {r['arrival']} | {r['duration']} | ₹{r['price_inr']} | {r['stops']} stop(s)"
        for r in results
    )


def search_hotels(
    destination: str,
    check_in: str = "",
    check_out: str = "",
    budget: str = "moderate",
    max_results: int = 4,
) -> str:
    """Search for hotels in the destination city.

    Args:
        destination: City or area (e.g. Goa, Baga).
        check_in: Check-in date if known.
        check_out: Check-out date if known.
        budget: budget, moderate, or luxury.
        max_results: Maximum number of options (default 4).
    """
    results = mock_hotels.search_hotels_mock(
        destination=destination,
        check_in=check_in,
        check_out=check_out,
        budget=budget,
        max_results=max_results,
    )
    if not results:
        return "No hotels found."
    return "\n".join(
        f"- {r['name']} ({r['area']}): ₹{r['price_per_night_inr']}/night | Rating {r['rating']} | {r.get('tradeoffs', '')}"
        for r in results
    )


def search_activities(
    destination: str,
    preferences: str = "",
    num_days: int = 3,
    max_results: int = 6,
) -> str:
    """Search for things to do and places to visit at the destination.

    Args:
        destination: City or region (e.g. Goa).
        preferences: User preferences (e.g. beaches, local food, sightseeing).
        num_days: Number of days of the trip to suggest activities for.
        max_results: Maximum number of activities (default 6).
    """
    results = mock_places.search_activities_mock(
        destination=destination,
        preferences=preferences,
        num_days=num_days,
        max_results=max_results,
    )
    if not results:
        return "No activities found."
    return "\n".join(
        f"- {r['name']} ({r['type']}): {r['description']} | Best time: {r.get('best_time', 'Any')}"
        for r in results
    )

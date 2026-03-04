"""Mock flights API (replace with Skyscanner/AviationStack later)."""

from __future__ import annotations

import logging
import random
from typing import Any

logger = logging.getLogger(__name__)

MOCK_FLIGHTS = [
    {"id": "FL001", "airline": "IndiGo", "departure": "Fri 22:00 PNQ", "arrival": "Sat 00:15 GOI", "duration": "1h 15m", "price_inr": 4200, "stops": 0},
    {"id": "FL002", "airline": "SpiceJet", "departure": "Fri 23:30 PNQ", "arrival": "Sat 01:45 GOI", "duration": "1h 15m", "price_inr": 3800, "stops": 0},
    {"id": "FL003", "airline": "Air India", "departure": "Fri 20:00 PNQ", "arrival": "Fri 22:15 GOI", "duration": "1h 15m", "price_inr": 5500, "stops": 0},
    {"id": "FL004", "airline": "IndiGo", "departure": "Sat 06:00 PNQ", "arrival": "Sat 08:15 GOI", "duration": "1h 15m", "price_inr": 4900, "stops": 0},
    {"id": "FL005", "airline": "IndiGo", "departure": "Mon 22:00 GOI", "arrival": "Sat 00:15 PNQ", "duration": "1h 15m", "price_inr": 4200, "stops": 1},
    {"id": "FL006", "airline": "SpiceJet", "departure": "Tue 23:30 GOI", "arrival": "Sat 01:45 PNQ", "duration": "1h 15m", "price_inr": 3800, "stops": 1},
    {"id": "FL007", "airline": "Air India", "departure": "Wed 20:00 GOI", "arrival": "Fri 22:15 PNQ", "duration": "1h 15m", "price_inr": 5500, "stops": 1},
    {"id": "FL008", "airline": "IndiGo", "departure": "Sat 06:00 GOI", "arrival": "Sat 08:15 PNQ", "duration": "1h 15m", "price_inr": 4900, "stops": 1},    
]


def search_flights_mock(
    origin: str,
    destination: str,
    date_preference: str = "",
    budget: str = "moderate",
    max_results: int = 4,
) -> list[dict[str, Any]]:
    origin = (origin or "Pune").strip().title()
    destination = (destination or "Goa").strip().title()
    results = list(MOCK_FLIGHTS)
    random.shuffle(results)
    if budget and "budget" in budget.lower():
        results = [r for r in results if r["price_inr"] <= 4500]
    elif budget and "luxury" in budget.lower():
        results = [r for r in results if r["price_inr"] >= 5000]
    logger.info(f"Flight API Results: {results}")    
    return results[:max_results]

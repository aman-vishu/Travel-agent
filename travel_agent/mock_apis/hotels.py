"""Mock hotels API (replace with Booking/RapidAPI later)."""

from __future__ import annotations

import logging
import random
from typing import Any

logger = logging.getLogger(__name__)

MOCK_HOTELS = [
    {"id": "HT001", "name": "Beach Haven Resort", "area": "Baga", "price_per_night_inr": 3500, "rating": 4.5, "tradeoffs": "Great beach access, can be noisy at night."},
    {"id": "HT002", "name": "Goa Heritage Inn", "area": "Panjim", "price_per_night_inr": 2200, "rating": 4.2, "tradeoffs": "Budget-friendly, slightly away from main beaches."},
    {"id": "HT003", "name": "Sunset Vista", "area": "Calangute", "price_per_night_inr": 4800, "rating": 4.7, "tradeoffs": "Premium views, higher price."},
    {"id": "HT004", "name": "Local Stay Goa", "area": "Anjuna", "price_per_night_inr": 1800, "rating": 4.0, "tradeoffs": "Very budget, basic amenities."},
]


def search_hotels_mock(
    destination: str,
    check_in: str = "",
    check_out: str = "",
    budget: str = "moderate",
    max_results: int = 4,
) -> list[dict[str, Any]]:
    results = list(MOCK_HOTELS)
    random.shuffle(results)
    if budget and "budget" in budget.lower():
        results = [r for r in results if r["price_per_night_inr"] <= 2500]
    elif budget and "luxury" in budget.lower():
        results = [r for r in results if r["price_per_night_inr"] >= 4000]
    logger.info(f"Hotel API Results: {results}")     
    return results[:max_results]

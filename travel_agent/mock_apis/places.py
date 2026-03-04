"""Mock places/activities API (replace with Google Places/Yelp later)."""

from __future__ import annotations

import logging
import random
from typing import Any

logger = logging.getLogger(__name__)

MOCK_ACTIVITIES = [
    {"id": "AC001", "name": "Baga Beach", "type": "beach", "description": "Popular beach with water sports and shacks.", "best_time": "Morning or sunset"},
    {"id": "AC002", "name": "Anjuna Flea Market", "type": "shopping", "description": "Wednesday flea market, local crafts and food.", "best_time": "Wednesday morning"},
    {"id": "AC003", "name": "Local Fish Thali Spots", "type": "food", "description": "Authentic Goan fish thali at beach shacks.", "best_time": "Lunch"},
    {"id": "AC004", "name": "Dudhsagar Falls", "type": "sightseeing", "description": "Day trip to majestic waterfall.", "best_time": "Morning"},
    {"id": "AC005", "name": "Calangute Beach", "type": "beach", "description": "Lively beach with cafes and activities.", "best_time": "Late afternoon"},
    {"id": "AC006", "name": "Goan Cafes & Curlies", "type": "food", "description": "Famous beachside cafes for local food.", "best_time": "Evening"},
]


def search_activities_mock(
    destination: str,
    preferences: str = "",
    num_days: int = 3,
    max_results: int = 6,
) -> list[dict[str, Any]]:
    destination = (destination or "Goa").strip().title()
    results = list(MOCK_ACTIVITIES)
    random.shuffle(results)
    pref = (preferences or "").lower()
    if pref:
        matching = [r for r in results if any(p in r["type"] or p in r["description"].lower() for p in pref.split())]
        if matching:
            results = matching + [r for r in results if r not in matching]
    logger.info(f"Activities API Results: {results}")         
    return results[:max_results]

"""
Travel Agent: Planner → Parallel (Flights | Hotels | Activities) → Merge.
"""

import os

try:
    from dotenv import load_dotenv
    from pathlib import Path
    load_dotenv()  # cwd (e.g. project root when running adk web .)
    load_dotenv(Path(__file__).resolve().parent / ".env")  # travel_agent/.env if present
    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.5-flash")
except ImportError:
    print("Warning: python-dotenv not installed. Ensure API key is set.")
    MODEL_NAME = "gemini-2.0-flash"

from google.adk.agents import Agent, ParallelAgent, SequentialAgent

from travel_agent.instructions import (
    PLANNER_INSTRUCTION,
    FLIGHTS_INSTRUCTION,
    HOTELS_INSTRUCTION,
    ACTIVITIES_INSTRUCTION,
    MERGE_INSTRUCTION,
    TRAVEL_ORCHESTRATOR_INSTRUCTION,
)
from travel_agent.tools.travel_tools import search_activities, search_flights, search_hotels

# --- Planner: extract trip params for next agents ---
planner_agent = Agent(
    name="PlannerAgent",
    model=MODEL_NAME,
    description="Extracts trip details from the user's message and outputs a clear trip request.",
    instruction=PLANNER_INSTRUCTION,
)

# --- Data-fetch agents (run in parallel); each has one tool ---
flights_agent = Agent(
    name="FlightsAgent",
    model=MODEL_NAME,
    description="Searches for flight options.",
    instruction=FLIGHTS_INSTRUCTION,
    tools=[search_flights],
)

hotels_agent = Agent(
    name="HotelsAgent",
    model=MODEL_NAME,
    description="Searches for hotel options.",
    instruction=HOTELS_INSTRUCTION,
    tools=[search_hotels],
)

activities_agent = Agent(
    name="ActivitiesAgent",
    model=MODEL_NAME,
    description="Searches for activities and places to visit.",
    instruction=ACTIVITIES_INSTRUCTION,
    tools=[search_activities],
)

# --- Parallel: fetch flights, hotels, activities at once ---
parallel_fetcher = ParallelAgent(
    name="ParallelFetcher",
    sub_agents=[flights_agent, hotels_agent, activities_agent],
)

# --- Merge: validate and produce final curated response ---
merge_agent = Agent(
    name="MergeAgent",
    model=MODEL_NAME,
    description="Validates and merges flight, hotel, and activity results into one curated response.",
    instruction=MERGE_INSTRUCTION,
)

# --- Root: Planner → Parallel fetch → Merge ---
travel_orchestrator = SequentialAgent(
    name="TravelAgent",
    description=TRAVEL_ORCHESTRATOR_INSTRUCTION,
    sub_agents=[planner_agent, parallel_fetcher, merge_agent],
)

root_agent = travel_orchestrator

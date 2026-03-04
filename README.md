# Travel Agent (Google ADK)

A travel planning agent built with **Google ADK** (Agent Development Kit). It uses:

- **Planner Agent** → extracts trip params from your message  
- **ParallelAgent** → fetches **Flights**, **Hotels**, **Activities** at once  
- **SequentialAgent** → **Validate & merge** into one curated response  

## Architecture

```
User Input
    ↓
Planner Agent (extract trip params)
    ↓
Parallel Execution
  ┌───────────┬───────────┬─────────────┐
  │ Flights   │ Hotels    │ Activities  │
  └───────────┴───────────┴─────────────┘
    ↓
Merge Agent (validate & curate)
    ↓
Final response (2 flights, 2 hotels, 4 activities + “Why this recommendation?”)
```

## Tech stack

- **APIs:** Mock first (flights, hotels, places) – swap later for Skyscanner / Booking / Google Places  
- **UI:** Google ADK Web UI (built-in chat, events, session state)  

## Setup

```bash
cd /path/to/Travel-Agent
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` in the project root (or copy from `travel_agent/.env.example`):

```env
GOOGLE_API_KEY=your_gemini_api_key
GOOGLE_GENAI_MODEL=gemini-2.0-flash
```

### Run with Google ADK Web UI

Structure follows [AhsanAyaz/ai-agents-google-adk](https://github.com/AhsanAyaz/ai-agents-google-adk) (e.g. `1-marketing_campaign_agent`). From the project root:

```bash
PYTHONPATH=. adk web . --port 8000
```

Then open **http://localhost:8000** in your browser. Use the ADK Web UI to chat with the travel agent, inspect events, and manage sessions. No custom frontend needed.

## Example prompt

**“Plan a 3-day budget trip to Goa from Pune, leaving Friday night. I like beaches and local food.”**

You get:

- 2 flight options with reasoning  
- 2 hotels with tradeoffs  
- 4 curated activities  
- Natural language explanation and a “Why this recommendation?” section  

## API

- **POST /plan** – Body: `TripRequest` (origin, destination, num_days, budget, preferences, etc.)  
- **POST /plan/prompt** – Body: `{ "prompt": "Plan a 3-day..." }`  
- **GET /health** – Health check  

## Project structure (like ai-agents-google-adk)

```
travel_agent/           # Single agent package (like 1-marketing_campaign_agent)
  .env.example
  __init__.py
  agent.py              # root_agent, load_dotenv, MODEL from env
  instructions.py       # PLANNER_INSTRUCTION, FLIGHTS_INSTRUCTION, etc.
  mock_apis/            # flights, hotels, places (mock; swap for real APIs)
  tools/                # travel_tools.py → search_flights, search_hotels, search_activities
backend/                # Optional: main.py for /plan, /plan/prompt API
```

## Swapping to real APIs

- **Flights:** Implement `travel_agent/mock_apis/flights.py` with Skyscanner or AviationStack.  
- **Hotels:** Implement `travel_agent/mock_apis/hotels.py` with Booking or RapidAPI.  
- **Places:** Implement `travel_agent/mock_apis/places.py` with Google Places or Yelp.  

The tools in `travel_agent/tools/travel_tools.py` call these modules; keep the same function signatures.

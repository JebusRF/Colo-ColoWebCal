import requests
import json

URL = "https://sports.core.api.espn.com/v2/sports/soccer/leagues/chi.1/events/401850418"

respuesta = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", respuesta.status_code)

print("\n=== EVENTO ===\n")

print(json.dumps(respuesta.json(), indent=2))

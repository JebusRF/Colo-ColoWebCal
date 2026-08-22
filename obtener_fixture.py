import requests
import json

URL = "https://sports.core.api.espn.com/v2/sports/soccer/leagues/chi.1/seasons/2026/teams/2688/events"

respuesta = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

print("STATUS:", respuesta.status_code)

print("\n=== EVENTOS COLO-COLO ===\n")

print(json.dumps(respuesta.json(), indent=2))

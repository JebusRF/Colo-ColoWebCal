import requests
import json

URL = "https://sports.core.api.espn.com/v2/sports/soccer/leagues/chi.1/seasons/2026/teams/2688/summary"

r = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

print("STATUS:", r.status_code)
print(json.dumps(r.json(), indent=2))

import requests
import json

URL = "https://sports.core.api.espn.com/v2/sports/soccer/leagues/chi.1/events/401850418/competitions/401850418/competitors/2688"

r = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

print("STATUS:", r.status_code)
print(json.dumps(r.json(), indent=2))

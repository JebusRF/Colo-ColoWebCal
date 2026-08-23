import requests
import json

url = "https://sports.core.api.espn.com/v2/sports/soccer/leagues/conmebol.libertadores"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", r.status_code)

try:
    print(json.dumps(r.json(), indent=2))
except Exception:
    print(r.text)

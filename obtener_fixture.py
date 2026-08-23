import requests
import json

url = "https://sports.core.api.espn.com/v2/sports/soccer/leagues?page=1"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

print("STATUS:", r.status_code)

data = r.json()

for item in data["items"]:
    ref = item["$ref"]
    if "chi" in ref.lower() or "conmebol" in ref.lower():
        print(ref)

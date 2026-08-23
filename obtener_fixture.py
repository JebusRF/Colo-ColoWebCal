import requests

url = "https://sports.core.api.espn.com/v2/sports/soccer/leagues"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

data = r.json()

print("STATUS:", r.status_code)

for item in data["items"]:
    ref = item["$ref"]

    if "/chi" in ref.lower():
        print(ref)

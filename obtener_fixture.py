import requests

pruebas = [
    "chi.copa_chile",
    "chi.copachile",
    "chi.copa",
    "chi.cup",
    "copa.chile"
]

for liga in pruebas:

    url = f"https://sports.core.api.espn.com/v2/sports/soccer/leagues/{liga}"

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    print(liga, "->", r.status_code)

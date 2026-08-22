import requests
import json

URL = "https://sports.core.api.espn.com/v2/sports/soccer/leagues"

respuesta = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", respuesta.status_code)

datos = respuesta.json()

print(json.dumps(datos, indent=2)[:8000])

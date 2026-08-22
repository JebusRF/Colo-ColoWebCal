import requests
import json

URL = "https://sports.core.api.espn.com/v2/sports/soccer"

respuesta = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("STATUS:", respuesta.status_code)

datos = respuesta.json()

print("\n=== PRIMEROS 5000 CARACTERES ===\n")

print(json.dumps(datos, indent=2)[:5000])

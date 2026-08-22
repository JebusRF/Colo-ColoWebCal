import requests
import json

URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/chi.1/teams/2688"

try:

    respuesta = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    print("STATUS:", respuesta.status_code)

    datos = respuesta.json()

    print("\n=== JSON RECIBIDO ===\n")

    print(json.dumps(datos, indent=2)[:5000])

except Exception as error:

    print("ERROR:", error)

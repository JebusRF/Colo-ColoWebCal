import requests
from bs4 import BeautifulSoup

URL = "https://www.espn.cl/futbol/equipo/calendario/_/id/2688/chi.1"

try:

    respuesta = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    print("STATUS:", respuesta.status_code)

    print("\n--- PRIMEROS 1000 CARACTERES ---\n")

    print(respuesta.text[:1000])

except Exception as error:

    print("ERROR:", error)

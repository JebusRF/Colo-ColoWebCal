from icalendar import Calendar, Event
from datetime import datetime, timedelta
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def obtener_eventos():

    eventos = []
    pagina = 1

    while True:

        url = (
            "https://sports.core.api.espn.com/v2/"
            "sports/soccer/leagues/chi.1/"
            f"seasons/2026/teams/2688/events?page={pagina}"
        )

        respuesta = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        eventos.extend(
            item["$ref"]
            for item in datos["items"]
        )

        if pagina >= datos["pageCount"]:
            break

        pagina += 1

    return eventos


def obtener_detalle_evento(url):

    url = url.replace("http://", "https://")

    respuesta = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    respuesta.raise_for_status()

    return respuesta.json()


def crear_calendario():

    calendario = Calendar()

    calendario.add(
        "prodid",
        "-//JebusRF

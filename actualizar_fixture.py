from icalendar import Calendar, Event
from datetime import datetime, timedelta
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

TORNEOS = [
    "chi.1",
    "chi.copa_chi",
    "chi.super_cup",
    "conmebol.libertadores",
    "conmebol.sudamericana",
    "fifa.friendly"
]

TEAM_ID = 2688
SEASON = 2026


def obtener_eventos():

    eventos = {}

    for torneo in TORNEOS:

        pagina = 1

        while True:

            url = (
                "https://sports.core.api.espn.com/v2/"
                f"sports/soccer/leagues/{torneo}/"
                f"seasons/{SEASON}/teams/{TEAM_ID}/events"
                f"?page={pagina}"
            )

            respuesta = requests.get(
                url,
                headers=HEADERS,
                timeout=30
            )

            if respuesta.status_code != 200:
                break

            datos = respuesta.json()

            for item in datos.get("items", []):
                eventos[item["$ref"]] = True

            if pagina >= datos.get("pageCount", 1):
                break

            pagina += 1

    return list(eventos.keys())


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
        "-//JebusRF Colo-Colo WebCal//"
    )

    calendario.add(
        "version",
        "2.0"
    )

    eventos_ref = obtener_eventos()

    total = 0

    eventos_agregados = set()

    for ref in eventos_ref:

        try:

            partido = obtener_detalle_evento(ref)

            uid = f"{partido['id']}@jebusrf"

            if uid in eventos_agregados:
                continue

            eventos_agregados.add(uid)

            fecha = partido["date"]

            nombre = partido

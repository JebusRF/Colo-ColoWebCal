from icalendar import Calendar, Event, Alarm
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

        r = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        r.raise_for_status()

        datos = r.json()

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

    r = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    r.raise_for_status()

    return r.json()


def crear_calendario():

    cal = Calendar()

    cal.add(
        "prodid",
        "-//JebusRF Colo-Colo WebCal//"
    )

    cal.add("version", "2.0")

    refs = obtener_eventos()

    print(f"EVENTOS ENCONTRADOS: {len(refs)}")

    total = 0

    for ref in refs:

        try:

            partido = obtener_detalle_evento(ref)

            fecha = partido["date"]
            titulo = partido["name"]
            uid = f"{partido['id']}@jebusrf"

            inicio = datetime.fromisoformat(
                fecha.replace("Z", "+00:00")
            )

            termino = inicio + timedelta(hours=2)

            estadio = "Por confirmar"

            try:
                estadio = (
                    partido["

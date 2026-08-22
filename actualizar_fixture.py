from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

EVENTOS_URL = (
    "https://sports.core.api.espn.com/v2/"
    "sports/soccer/leagues/chi.1/"
    "seasons/2026/teams/2688/events"
)


def obtener_eventos():

    r = requests.get(
        EVENTOS_URL,
        headers=HEADERS,
        timeout=30
    )

    r.raise_for_status()

    datos = r.json()

    return [item["$ref"] for item in datos["items"]]


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

    total = 0

    for ref in refs:

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
                partido["competitions"][0]
                ["venue"]
                ["fullName"]
            )
        except Exception:
            pass

        evento = Event()

        evento.add("uid", uid)

        evento.add("summary", titulo)

        evento.add(
            "description",
            f"""Club: Colo-Colo

Estadio: {estadio}

Fuente: ESPN Core API

https://jebusrf.github.io/Colo-ColoWebCal/
"""
        )

        evento.add("location", estadio)
        evento.add("dtstart", inicio)
        evento.add("dtend", termino)

        alarma24 = Alarm()
        alarma24.add("action", "DISPLAY")
        alarma24.add(
            "description",
            "Partido de Colo-Colo en 24 horas"
        )
        alarma24.add(
            "trigger",
            timedelta(hours=-24)
        )
        evento.add_component(alarma24)

        alarma2 = Alarm()
        alarma2.add("action", "DISPLAY")
        alarma2.add(
            "description",
            "Partido de Colo-Colo en 2 horas"
        )
        alarma2.add(
            "trigger",
            timedelta(hours=-2)
        )
        evento.add_component(alarma2)

        cal.add_component(evento)

        total += 1

    with open("docs/colocolo.ics", "wb") as archivo:
        archivo.write(cal.to_ical())

    print("CALENDARIO GENERADO CORRECTAMENTE")
    print(f"PARTIDOS GENERADOS: {total}")


if __name__ == "__main__":
    crear_calendario()

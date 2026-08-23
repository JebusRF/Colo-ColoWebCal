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
    calendario.add("prodid", "-//JebusRF Colo-Colo WebCal//")
    calendario.add("version", "2.0")

    eventos_ref = obtener_eventos()

    total = 0

    for ref in eventos_ref:

        try:

            partido = obtener_detalle_evento(ref)

            fecha = partido["date"]

            titulo = partido["name"].replace(" at ", " vs ")

            uid = f"{partido['id']}@jebusrf"

            inicio = datetime.fromisoformat(
                fecha.replace("Z", "+00:00")
            )

            termino = inicio + timedelta(hours=2)

            estadio = "Por confirmar"

            try:
                estadio = (
                    partido["competitions"][0]["venue"]["fullName"]
                )
            except Exception:
                pass

            evento = Event()

            evento.add("uid", uid)
            evento.add("summary", titulo)
            evento.add("location", estadio)

            descripcion = (
                f"Club: Colo-Colo\r\n"
                f"\r\n"
                f"Estadio: {estadio}\r\n"
                f"\r\n"
                f"Fuente: ESPN Core API\r\n"
                f"\r\n"
                f"https://jebusrf.github.io/Colo-ColoWebCal/"
            )

            evento.add("description", descripcion)

            evento.add("dtstart", inicio)
            evento.add("dtend", termino)

            calendario.add_component(evento)

            total += 1

        except Exception as e:

            print(f"ERROR EN EVENTO: {ref}")
            print(e)

    with open("docs/colocolo.ics", "wb") as archivo:
        archivo.write(calendario.to_ical())

    print("CALENDARIO GENERADO CORRECTAMENTE")
    print(f"PARTIDOS GENERADOS: {total}")


if __name__ == "__main__":
    crear_calendario()

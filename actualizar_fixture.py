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
    "conmebol.sudamericana"
]

TEAM_ID = 2688
SEASON = 2026


def obtener_eventos_torneo(slug):

    eventos = []
    pagina = 1

    while True:

        url = (
            "https://sports.core.api.espn.com/v2/"
            f"sports/soccer/leagues/{slug}/"
            f"seasons/{SEASON}/teams/{TEAM_ID}/events"
            f"?page={pagina}"
        )

        respuesta = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        if respuesta.status_code != 200:
            print(f"TORNEO NO DISPONIBLE: {slug}")
            break

        datos = respuesta.json()

        eventos.extend(
            item["$ref"]
            for item in datos.get("items", [])
        )

        if pagina >= datos.get("pageCount", 1):
            break

        pagina += 1

    return eventos


def obtener_todos_los_eventos():

    eventos_unicos = {}
    resumen = {}

    for torneo in TORNEOS:

        refs = obtener_eventos_torneo(torneo)

        resumen[torneo] = len(refs)

        for ref in refs:
            eventos_unicos[ref] = True

    print("\nRESUMEN:")

    for torneo, total in resumen.items():
        print(f"{torneo}: {total}")

    return list(eventos_unicos.keys())


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

    eventos_ref = obtener_todos_los_eventos()

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

            nombre = partido["name"]

            if " at " in nombre:
                visitante, local = nombre.split(" at ")
                titulo = f"{local} vs {visitante}"
            else:
                titulo = nombre

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

            evento.add(
                "description",
                descripcion
            )

            evento.add("dtstart", inicio)
            evento.add("dtend", termino)

            calendario.add_component

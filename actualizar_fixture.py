from icalendar import Calendar, Event
from datetime import datetime, timedelta

PARTIDOS = [
    (
        "2026-08-23 15:00",
        "Universidad de Chile vs Colo-Colo",
        "Estadio Nacional, Santiago",
        "Primera División"
    ),
    (
        "2026-08-26 17:30",
        "Colo-Colo vs Unión Española",
        "Estadio Monumental, Santiago",
        "Copa Chile"
    ),
    (
        "2026-08-30 14:30",
        "Colo-Colo vs Audax Italiano",
        "Estadio Monumental, Santiago",
        "Primera División"
    ),
    (
        "2026-09-06 13:00",
        "Huachipato vs Colo-Colo",
        "Por confirmar",
        "Primera División"
    ),
    (
        "2026-09-13 13:30",
        "Colo-Colo vs Deportes Concepción",
        "Estadio Monumental, Santiago",
        "Primera División"
    ),
    (
        "2026-10-11 11:00",
        "Coquimbo Unido vs Colo-Colo",
        "Por confirmar",
        "Primera División"
    ),
    (
        "2026-10-25 12:00",
        "Palestino vs Colo-Colo",
        "Por confirmar",
        "Primera División"
    ),
    (
        "2026-11-01 12:00",
        "Colo-Colo vs Universidad de Concepción",
        "Estadio Monumental, Santiago",
        "Primera División"
    ),
    (
        "2026-11-08 12:00",
        "Ñublense vs Colo-Colo",
        "Por confirmar",
        "Primera División"
    ),
    (
        "2026-11-22 12:00",
        "Colo-Colo vs Universidad Católica",
        "Estadio Monumental, Santiago",
        "Primera División"
    ),
    (
        "2026-11-29 12:00",
        "Colo-Colo vs Deportes La Serena",
        "Estadio Monumental, Santiago",
        "Primera División"
    ),
    (
        "2026-12-06 12:00",
        "Cobresal vs Colo-Colo",
        "Por confirmar",
        "Primera División"
    )
]

cal = Calendar()
cal.add("prodid", "-//JebusRF Colo-Colo WebCal//")
cal.add("version", "2.0")

for i, (fecha, titulo, estadio, torneo) in enumerate(PARTIDOS):

    inicio = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
    termino = inicio + timedelta(hours=2)

    evento = Event()

    # UID único para que Outlook actualice en lugar de duplicar
    evento.add("uid", f"colocolo-2026-{i}@jebusrf")

    evento.add("summary", titulo)
    evento.add("location", estadio)

    evento.add(
        "description",
        f"Torneo: {torneo}\\nEstadio: {estadio}"
    )

    evento.add("dtstart", inicio)
    evento.add("dtend", termino)

    cal.add_component(evento)

with open("docs/colocolo.ics", "wb") as archivo:
    archivo.write(cal.to_ical())

print("CALENDARIO GENERADO CORRECTAMENTE")

import json
from datetime import datetime, timedelta
from icalendar import Calendar, Event

def cargar_respaldo():
    with open("fixture_respaldo.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

partidos = cargar_respaldo()

cal = Calendar()
cal.add("prodid", "-//JebusRF Colo-Colo WebCal//")
cal.add("version", "2.0")

for partido in partidos:

    inicio = datetime.strptime(
        partido["fecha"],
        "%Y-%m-%d %H:%M"
    )

    termino = inicio + timedelta(hours=2)

    evento = Event()

    uid = (
        f"{partido['fecha']}-{partido['titulo']}"
        .replace(" ", "-")
        .replace(":", "")
        .lower()
        + "@jebusrf"
    )

    evento.add("uid", uid)

    evento.add("summary", partido["titulo"])

    evento.add(
        "description",
        f"""
Club: Colo-Colo

Competición:
{partido['torneo']}

Estadio:
{partido['estadio']}

Estado:
Programado

Cómo verlo:
Por confirmar

Calendario generado automáticamente por Colo-Colo WebCal.

https://jebusrf.github.io/Colo-ColoWebCal/
"""
    )

    evento.add("location", partido["estadio"])
    evento.add("dtstart", inicio)
    evento.add("dtend", termino)

    cal.add_component(evento)

with open("docs/colocolo.ics", "wb") as archivo:
    archivo.write(cal.to_ical())

print(f"PARTIDOS GENERADOS: {len(partidos)}")

from icalendar import Calendar, Event
from datetime import datetime, timedelta
cal = Calendar()
cal.add("prodid", "-//JebusRF Colo-Colo WebCal//")
cal.add("version", "2.0")
partidos = [
    ("2026-08-23 15:00", "Universidad de Chile vs Colo-Colo"),
    ("2026-08-26 17:30", "Colo-Colo vs Unión Española"),
    ("2026-08-30 14:30", "Colo-Colo vs Audax Italiano")
]
for fecha, titulo in partidos:
    inicio = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
    evento = Event()
    evento.add("summary", titulo)
    evento.add("dtstart", inicio)
    evento.add("dtend", inicio + timedelta(hours=2))
    cal.add_component(evento)
with open("docs/colocolo.ics", "wb") as archivo:
    archivo.write(cal.to_ical())
print("CALENDARIO GENERADO CORRECTAMENTE")

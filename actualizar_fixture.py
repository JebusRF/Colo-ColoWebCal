from icalendar import Calendar, Event
from datetime import datetime, timedelta

PARTIDOS = [
    ("2026-08-23 15:00", "Universidad de Chile vs Colo-Colo",
     "Estadio Nacional, Santiago", "Primera División"),

    ("2026-08-26 17:30", "Colo-Colo vs Unión Española",
     "Estadio Monumental, Santiago", "Copa Chile"),

    ("2026-08-30 14:30", "Colo-Colo vs Audax Italiano",
     "Estadio Monumental, Santiago", "Primera División")
]

cal = Calendar()
cal.add("prodid", "-//Colo Colo WebCal//JebusRF//")
cal.add("version", "2.0")

for fecha, titulo, estadio, torneo in PARTIDOS:

    inicio = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
    fin = inicio + timedelta(hours=2)

    evento = Event()
    evento.add("summary", titulo)
    evento.add("location", estadio)
    evento.add("description", torneo)
    evento.add("dtstart", inicio)
    evento.add("dtend", fin)

    cal.add_component(evento)

with open("docs/colocolo.ics", "wb") as archivo:
    archivo.write(cal.to_ical())
print("CALENDARIO GENERADO CORRECTAMENTE")

from icalendar import Calendar, Event
from datetime import datetime, timedelta

cal = Calendar()
cal.add("prodid", "-//Colo Colo WebCal//")
cal.add("version", "2.0")

partidos = [
    {
        "titulo": "Colo-Colo vs Audax Italiano",
        "inicio": datetime(2026, 8, 30, 14, 30),
        "estadio": "Monumental David Arellano"
    }
]

for partido in partidos:
    event = Event()
    event.add("summary", partido["titulo"])
    event.add("dtstart", partido["inicio"])
    event.add("dtend", partido["inicio"] + timedelta(hours=2))
    event.add("location", partido["estadio"])
    cal.add_component(event)

with open("docs/colocolo.ics", "wb") as f:
    f.write(cal.to_ical())

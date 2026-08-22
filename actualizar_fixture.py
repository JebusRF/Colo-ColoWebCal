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

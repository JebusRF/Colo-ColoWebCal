import requests

URLS = [
    "https://site.api.espn.com/apis/site/v2/sports/soccer",
    "https://site.web.api.espn.com/apis/site/v2/sports/soccer",
    "https://sports.core.api.espn.com/v2/sports/soccer"
]

for url in URLS:

    try:

        respuesta = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30
        )

        print("\n===================================")
        print("URL:", url)
        print("STATUS:", respuesta.status_code)
        print("CONTENT-TYPE:", respuesta.headers.get("content-type"))
        print("===================================\n")

    except Exception as error:

        print("ERROR:", url, error)

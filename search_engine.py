import requests
import urllib.parse


def search(query):

    try:

        q = urllib.parse.quote(query)

        url = f"https://api.duckduckgo.com/?q={q}&format=json&no_html=1"

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()


        text = data.get("AbstractText")


        if text:

            return text


        topics = data.get("RelatedTopics", [])

        if topics:

            return topics[0].get("Text", "Ничего не найдено.")


        return "Информация не найдена."


    except Exception as e:

        return f"Ошибка поиска: {e}"

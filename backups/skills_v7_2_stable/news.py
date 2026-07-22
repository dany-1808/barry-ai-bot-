import requests
import xml.etree.ElementTree as ET


def get_news(query):

    try:

        url = "https://news.google.com/rss/search"


        params = {
            "q": query,
            "hl": "ru",
            "gl": "RU",
            "ceid": "RU:ru"
        }


        response = requests.get(
            url,
            params=params,
            timeout=10,
            headers={
                "User-Agent": "BarryAI/5.7"
            }
        )


        response.raise_for_status()


        root = ET.fromstring(
            response.text
        )


        items = root.findall(".//item")


        if not items:
            return "Новостей не найдено."


        result = ""


        count = 0


        for item in items:

            title = item.find("title")


            if title is not None and title.text:

                result += (
                    "• "
                    + title.text
                    + "\n\n"
                )

                count += 1


            if count >= 5:
                break


        return result


    except Exception as e:

        return f"Ошибка: {e}"



def run(text):

    low = text.lower().strip()


    if not low.startswith("новости"):
        return None



    query = text[7:].strip()


    if not query:

        query = "главные новости"


    result = get_news(query)


    return (
        f"📰 Новости: {query}\n\n"
        f"{result}"
    )

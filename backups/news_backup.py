import requests
import xml.etree.ElementTree as ET


def run(text):

    low = text.lower().strip()


    if low != "новости":
        return None


    try:

        url = "https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru"


        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "BarryAI/5.7"
            }
        )


        response.raise_for_status()


        root = ET.fromstring(
            response.text
        )


        items = root.findall(
            ".//item"
        )


        if not items:

            return (
                "📰 Новости Barry\n\n"
                "Новости не найдены."
            )


        result = (
            "📰 Последние новости:\n\n"
        )


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


        return (
            "❌ Ошибка получения новостей:\n"
            f"{e}"
        )

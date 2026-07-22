import os
import json
from datetime import datetime


FILE = "data/development_memory.json"


def save_development(text):

    os.makedirs(
        "data",
        exist_ok=True
    )

    data = []

    if os.path.exists(FILE):

        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:
            data = json.load(f)


    data.append(
        {
            "date": datetime.now().strftime(
                "%d.%m.%Y %H:%M"
            ),
            "analysis": text
        }
    )


    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def get_developments():

    if not os.path.exists(FILE):
        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def run(text):

    if text.lower().strip() == "история развития":

        history = get_developments()

        if not history:
            return "📘 История развития пуста."


        result = "📘 Barry Development Memory\n\n"

        for item in history[-10:]:

            result += (
                f"📅 {item['date']}\n"
                f"{item['analysis']}\n\n"
            )

        return result


    return None

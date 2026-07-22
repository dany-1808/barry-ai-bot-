import os
import json
from datetime import datetime


FILE = "data/error_memory.json"


def save_error(error):

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
            "error": error,
            "status": "open"
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


def get_errors():

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def clear_errors():

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            [],
            f,
            ensure_ascii=False,
            indent=2
        )


def run(text):

    command = text.lower().strip()


    if command == "история ошибок":

        errors = get_errors()


        if not errors:

            return (
                "🧠 Barry Error Memory\n\n"
                "Ошибок нет."
            )


        result = (
            "🧠 Barry Error Memory\n\n"
        )


        for item in errors[-10:]:

            result += (
                f"📅 {item.get('date','')}\n"
                f"⚠ {item.get('error','')}\n\n"
            )


        return result


    if command == "очистить ошибки":

        clear_errors()

        return (
            "🧹 Barry Error Memory\n\n"
            "✅ История ошибок очищена."
        )


    return None

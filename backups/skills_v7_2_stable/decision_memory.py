import os
from datetime import datetime


FILE = "data/decisions.txt"


def save_decision(
    instrument,
    result
):

    os.makedirs(
        "data",
        exist_ok=True
    )


    with open(
        FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n"
            + "=" * 40
            + "\n"
        )

        f.write(
            datetime.now().strftime(
                "%d.%m.%Y %H:%M"
            )
            + "\n"
        )

        f.write(
            f"Инструмент: {instrument}\n"
        )

        f.write(
            result
            + "\n"
        )



def run(text):

    if text.lower().startswith(
        "запомни решение"
    ):

        data = text.replace(
            "запомни решение",
            ""
        ).strip()


        save_decision(
            "Manual",
            data
        )


        return (
            "🧠 Barry Memory\n\n"
            "Решение сохранено."
        )


    if text.lower().strip() == "история решений":

        if not os.path.exists(FILE):

            return (
                "📒 История решений пуста."
            )


        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = f.read()


        return (
            "📒 Barry Decision Memory\n\n"
            + data[-3000:]
        )


    return None

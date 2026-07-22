import os
from datetime import datetime


FILE = "data/decisions.txt"


def save_decision(
    instrument,
    price,
    decision,
    confidence
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
            f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        )

        f.write(
            f"Инструмент: {instrument}\n"
        )

        f.write(
            f"Цена: {price}\n"
        )

        f.write(
            f"Уверенность Barry: {confidence}%\n"
        )

        f.write(
            f"Решение Barry: {decision}\n"
        )


    return True



def run(text):

    return None

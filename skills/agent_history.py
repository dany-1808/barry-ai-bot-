import os
from datetime import datetime


FILE = "data/agent_history.txt"


def save_action(action):

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
            f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} | {action}\n"
        )


def run(text):

    low = text.lower().strip()

    if low == "история barry":

        if not os.path.exists(FILE):
            return "📜 История действий Barry пуста."


        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = f.readlines()


        last = data[-20:]


        return (
            "📜 Barry Agent History\n\n"
            +
            "".join(last)
        )


    return None

import os
from datetime import datetime


FILE = "data/actions.txt"


def add_action(action):

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


def get_actions(limit=20):

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        data = f.readlines()


    return data[-limit:]

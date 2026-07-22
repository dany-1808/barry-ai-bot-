import json
import os
from datetime import datetime


FILE = "data/updates.json"


def add_update(text):

    os.makedirs("data", exist_ok=True)

    updates = []

    if os.path.exists(FILE):

        with open(FILE, "r", encoding="utf-8") as f:
            updates = json.load(f)


    updates.append({
        "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "update": text
    })


    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            updates,
            f,
            ensure_ascii=False,
            indent=2
        )


def get_updates():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

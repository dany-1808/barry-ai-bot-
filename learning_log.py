import json
import os
from datetime import datetime


FILE = "data/learning_log.json"


def add_log(text):

    os.makedirs("data", exist_ok=True)

    logs = []

    if os.path.exists(FILE):

        with open(FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)


    logs.append({
        "date": datetime.now().strftime("%d.%m.%Y"),
        "text": text
    })


    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            logs,
            f,
            ensure_ascii=False,
            indent=2
        )


def get_logs():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

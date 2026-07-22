import json
import os
from datetime import datetime


FILE = "data/reminders.json"


def load():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save(data):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )



def add(text):

    data = load()

    data.append({
        "text": text,
        "date": datetime.now().strftime("%d.%m.%Y")
    })

    save(data)



def get_all():

    return load()

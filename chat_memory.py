import json
import os
from datetime import datetime


FILE = "data/chat_history.json"


def save_chat(user, assistant):

    os.makedirs("data", exist_ok=True)

    history = []

    if os.path.exists(FILE):

        with open(FILE, "r", encoding="utf-8") as f:
            history = json.load(f)


    history.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "user": user,
        "assistant": assistant
    })


    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            history,
            f,
            ensure_ascii=False,
            indent=2
        )


def get_history():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

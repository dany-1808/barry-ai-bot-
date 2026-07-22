import json
import os


FILE = "data/goals.json"


def save_goal(name, steps):

    os.makedirs("data", exist_ok=True)

    data = {}

    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)


    data[name] = steps


    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def get_goal(name):

    if not os.path.exists(FILE):
        return None


    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)


    return data.get(name)

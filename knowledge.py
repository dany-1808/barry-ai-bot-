import json
import os


FILE = "data/knowledge.json"


def load():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):
        return {}

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



def add(title, text):

    data = load()

    data[title] = text

    save(data)



def search(title):

    data = load()

    return data.get(title)

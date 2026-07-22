import json
import os


FILE = "data/progress.json"


def load_progress():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_progress(data):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )



def complete(topic, day):

    data = load_progress()

    if topic not in data:
        data[topic] = []


    if day not in data[topic]:
        data[topic].append(day)


    save_progress(data)



def get_progress(topic, total):

    data = load_progress()

    done = len(data.get(topic, []))

    percent = int(done / total * 100)

    return done, percent

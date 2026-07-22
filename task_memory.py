import os
import json


FILE = "data/task_memory.json"


def save_context(key, value):

    os.makedirs(
        "data",
        exist_ok=True
    )

    data = load_context()

    data[key] = value


    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_context(key):

    data = load_context()

    return data.get(
        key
    )



def load_context():

    if not os.path.exists(FILE):

        return {}


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

import os
import json
from datetime import datetime


FILE = "data/skill_usage.json"



def save_usage(skill):

    os.makedirs(
        "data",
        exist_ok=True
    )


    data = []


    if os.path.exists(FILE):

        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)



    found = False


    for item in data:

        if item["skill"] == skill:

            item["count"] += 1
            item["last"] = datetime.now().strftime(
                "%d.%m.%Y %H:%M"
            )

            found = True



    if not found:

        data.append(
            {
                "skill": skill,
                "count": 1,
                "last": datetime.now().strftime(
                    "%d.%m.%Y %H:%M"
                )
            }
        )



    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )





def get_usage():

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

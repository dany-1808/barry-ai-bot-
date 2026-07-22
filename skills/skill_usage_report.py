import os
import json


FILE = "data/skill_usage.json"



def run(text):

    if "использование навыков" not in text.lower():

        return None



    if not os.path.exists(FILE):

        return (
            "📊 Barry Skill Usage\n\n"
            "История использования пока пустая."
        )



    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)



    if not data:

        return (
            "📊 Barry Skill Usage\n\n"
            "Нет данных."
        )



    data = sorted(
        data,
        key=lambda x: x.get("count", 0),
        reverse=True
    )



    result = (
        "📊 Barry Skill Usage\n\n"
        "🔥 Активные навыки:\n"
    )



    for item in data[:10]:

        result += (
            f"• {item['skill']} — "
            f"{item['count']} раз\n"
        )



    result += "\n💤 Неактивные:\n"



    inactive = [
        x for x in data
        if x.get("count", 0) == 0
    ]



    if inactive:

        for item in inactive[:10]:

            result += (
                f"• {item['skill']}\n"
            )

    else:

        result += "Нет данных\n"



    return result

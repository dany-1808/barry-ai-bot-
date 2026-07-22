import os
import json


USAGE_FILE = "data/skill_usage.json"



def get_usage():

    if not os.path.exists(USAGE_FILE):

        return []


    with open(
        USAGE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




def run(text):

    if "рекомендации развития" not in text.lower():

        return None



    usage = get_usage()


    result = (
        "🚀 Barry Recommendation Engine\n\n"
    )



    if not usage:

        return (
            result +
            "Нет данных использования навыков."
        )



    usage = sorted(
        usage,
        key=lambda x: x.get("count", 0),
        reverse=True
    )



    result += "🔥 Приоритетные модули:\n"



    for item in usage[:5]:

        result += (
            f"• {item['skill']} — "
            f"{item['count']} раз\n"
        )



    result += "\n🧠 Рекомендации:\n"



    result += (
        "• Улучшать часто используемые навыки\n"
        "• Проверять редко используемые модули\n"
        "• Тестировать новые функции перед добавлением\n"
    )



    return result

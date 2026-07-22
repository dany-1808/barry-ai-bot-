from goals import save_goal, get_goal
import os
import json


FILE = "data/goals.json"


def load_all_goals():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def run(text):

    low = text.lower().strip()



    if "цели barry" in low or "покажи цели" in low:

        goals = load_all_goals()


        if not goals:
            return "🎯 Целей Barry пока нет."


        result = "🎯 Цели Barry:\n\n"


        for name, steps in goals.items():

            result += f"🔹 {name}\n"

            for step in steps:
                result += f"   • {step}\n"

            result += "\n"


        return result




    if low.startswith("добавь цель"):

        name = text[len("добавь цель"):].strip()


        if not name:
            return "❌ Укажи название цели."


        steps = [
            "Анализ текущего состояния",
            "Создание улучшения",
            "Проверка результата"
        ]


        save_goal(name, steps)


        return (
            "🎯 Новая цель Barry создана:\n"
            f"{name}"
        )




    if low.startswith("цель"):

        name = text[4:].strip()


        goal = get_goal(name)


        if goal:

            return (
                f"🎯 Цель: {name}\n\n"
                + "\n".join(
                    "• " + x for x in goal
                )
            )


        return "❌ Такая цель не найдена."



    return None

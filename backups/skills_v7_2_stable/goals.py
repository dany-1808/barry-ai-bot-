from goals import save_goal, get_goal
from ai_brain import ask_ai


def run(text):

    low = text.lower()


    if low.startswith("создай план"):

        topic = text.replace(
            "создай план",
            "",
            1
        ).strip()


        if not topic:
            return "Напиши тему плана."


        plan = ask_ai(
            f"Создай подробный план: {topic}"
        )


        save_goal(topic, plan)


        return (
            "📚 План создан и сохранён:\n\n"
            + plan
        )



    if low.startswith("покажи план"):

        topic = text.replace(
            "покажи план",
            "",
            1
        ).strip()


        plan = get_goal(topic)


        if plan:
            return (
                "📚 Твой сохранённый план:\n\n"
                + plan
            )


        return "План не найден."


    return None

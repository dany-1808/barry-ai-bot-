from action_log import get_actions


def run(text):

    if "покажи журнал" not in text.lower():
        return None


    logs = get_actions()


    if not logs:
        return "📜 Журнал пуст."


    result = "📜 Журнал Barry:\n\n"


    for item in logs[-10:]:

        result += (
            f"📅 {item['time']}\n"
            f"✅ {item['action']}\n\n"
        )


    return result

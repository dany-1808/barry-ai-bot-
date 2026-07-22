from chat_memory import get_history


def run(text):

    low = text.lower().strip()

    if low not in [
        "что мы делали",
        "что мы делали?",
        "вспомни разговор",
        "вспомни"
    ]:
        return None


    history = get_history()


    if not history:
        return "История разговоров пустая."


    answer = "🧠 Последние события:\n\n"


    for item in history[-5:]:

        answer += (
            f"🕒 {item['time']}\n"
            f"Ты: {item['user']}\n"
            f"Barry: {item['assistant']}\n\n"
        )


    return answer

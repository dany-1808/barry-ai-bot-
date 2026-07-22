from learning_log import add_log, get_logs


def run(text):

    low = text.lower()


    if low.startswith("сегодня изучил"):

        info = text[15:].strip()

        add_log(info)

        return "📔 Записал в дневник обучения."


    if "покажи дневник обучения" in low:

        logs = get_logs()


        if not logs:
            return "Дневник пуст."


        result = "📔 Дневник обучения:\n\n"

        for item in logs[-10:]:

            result += (
                f"📅 {item['date']}\n"
                f"✅ {item['text']}\n\n"
            )


        return result


    return None

from reminders import add, get_all


def run(text):

    low = text.lower()


    if low.startswith("напомни"):

        task = text[7:].strip()

        if task:

            add(task)

            return "⏰ Напоминание создано."


        return "Напиши что напомнить."


    if "мои напоминания" in low:

        data = get_all()


        if not data:
            return "📅 Напоминаний нет."


        result = "📅 Напоминания:\n\n"


        for i, item in enumerate(data, 1):

            result += (
                f"{i}. {item['text']}\n"
                f"📅 {item['date']}\n\n"
            )


        return result


    return None

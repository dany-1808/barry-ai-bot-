from progress import complete, get_progress


def run(text):

    low = text.lower()


    if low.startswith("отметь день"):

        parts = low.split()

        try:

            day = int(parts[2])

        except:

            return "Напиши: отметь день 1 Python"


        topic = "Python"


        complete(topic, day)


        done, percent = get_progress(
            topic,
            30
        )


        return (
            f"✅ День {day} выполнен\n"
            f"📊 Прогресс Python: {done}/30 ({percent}%)"
        )


    if "мой прогресс python" in low:

        done, percent = get_progress(
            "Python",
            30
        )


        return (
            f"📚 Python 30 дней\n\n"
            f"✅ Выполнено: {done}/30\n"
            f"📊 Прогресс: {percent}%"
        )


    return None

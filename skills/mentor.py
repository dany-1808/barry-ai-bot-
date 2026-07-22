from progress import get_progress


def run(text):

    low = text.lower()


    if "что дальше по python" in low:

        done, percent = get_progress(
            "Python",
            30
        )


        next_day = done + 1


        lessons = {
            1: "Введение в Python",
            2: "Переменные и типы данных",
            3: "Условия if/else",
            4: "Циклы for и while",
            5: "Функции"
        }


        lesson = lessons.get(
            next_day,
            "Продолжай следующий день плана Python"
        )


        return (
            f"📚 Python\n\n"
            f"✅ Пройдено: {done}/30 ({percent}%)\n\n"
            f"➡ Следующий шаг: День {next_day}\n"
            f"Тема: {lesson}\n\n"
            f"💪 Практика: напиши небольшую программу по теме."
        )


    return None

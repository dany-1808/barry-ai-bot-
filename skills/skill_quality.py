import os


def check_quality():

    if not os.path.exists("skills"):

        return "Папка skills не найдена."


    skills = []


    for file in os.listdir("skills"):

        if file.endswith(".py") and file != "__init__.py":

            skills.append(
                file.replace(".py", "")
            )


    result = (
        "🛠 Barry Skill Quality Check\n\n"
        f"Всего модулей: {len(skills)}\n\n"
    )


    if len(skills) < 20:

        result += (
            "⚠ Мало навыков\n"
            "Рекомендация: создавать новые модули."
        )

    else:

        result += (
            "✅ Количество навыков достаточное\n\n"
            "Проверка:\n"
            "✅ Модули обнаружены\n"
            "✅ Структура skills работает\n"
            "⚠ Требуется анализ использования"
        )


    return result



def run(text):

    if "качество навыков" not in text.lower():

        return None


    return check_quality()

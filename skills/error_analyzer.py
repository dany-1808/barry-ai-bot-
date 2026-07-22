import os
from skills.error_memory import get_errors


def analyze():

    errors = get_errors()


    if not errors:

        return (
            "🔎 Анализ ошибок Barry\n\n"
            "Ошибок не найдено.\n"
            "Система работает стабильно."
        )



    count = len(errors)


    result = (
        "🔎 Barry Error Analyzer\n\n"
        f"Всего ошибок: {count}\n\n"
    )


    result += "Последние проблемы:\n"


    for item in errors[-5:]:

        result += (
            f"⚠ {item['error']}\n"
        )


    result += (
        "\n🚀 Рекомендация Barry:\n"
        "Проверить проблемные модули "
        "и улучшить их."
    )


    return result



def run(text):

    if "анализ ошибок" not in text.lower():

        return None


    return analyze()

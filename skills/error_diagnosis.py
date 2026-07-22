import os

from skills.error_memory import get_errors


def run(text):

    if "диагностика ошибок" not in text.lower():
        return None


    errors = get_errors()


    if not errors:

        return (
            "🧠 Barry Error Diagnosis\n\n"
            "✅ Ошибок для анализа нет."
        )


    last = errors[-1]


    error_text = last.get(
        "error",
        "Неизвестная ошибка"
    )


    result = (
        "🧠 Barry Error Diagnosis\n\n"
        "Последняя ошибка:\n"
        f"⚠ {error_text}\n\n"

        "🔎 Анализ:\n"
        "• Ошибка записана в Error Memory\n"
        "• Требуется проверка модуля\n"
        "• Нужно определить источник ошибки\n\n"

        "🚀 Рекомендация:\n"
        "Проверить связанный навык и протестировать исправление."
    )


    return result

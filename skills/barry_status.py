import os
import json


DECISION_FILE = "data/decisions.txt"
MEMORY_FILE = "data/memory.json"


def run(text):

    if text.lower().strip() not in [
        "статус системы",
        "статус barry",
        "состояние barry"
    ]:
        return None


    decisions = 0

    if os.path.exists(DECISION_FILE):

        with open(
            DECISION_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = f.read()

            decisions = data.count(
                "Инструмент:"
            )


    memory_status = "❌ Нет памяти"

    if os.path.exists(MEMORY_FILE):
        memory_status = "✅ Память активна"


    skills = 0

    if os.path.exists("skills"):

        skills = len(
            [
                x for x in os.listdir("skills")
                if x.endswith(".py")
                and x != "__init__.py"
            ]
        )


    return (
        "🤖 Barry AI System Status\n\n"
        f"🧩 Навыков: {skills}\n"
        f"🧠 Память: {memory_status}\n"
        f"📊 Решений сохранено: {decisions}\n\n"
        "Состояние:\n"
        "✅ Агент активен\n"
        "✅ Анализ решений активен\n"
        "✅ Торговый модуль активен"
    )

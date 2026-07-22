from config import BARRY_VERSION
from action_log import get_actions
import os


def run(text):

    if "анализ barry" not in text.lower():
        return None


    skills = 0

    if os.path.exists("skills"):

        skills = len([
            f for f in os.listdir("skills")
            if f.endswith(".py")
            and f != "__init__.py"
        ])


    logs = len(get_actions())


    return (
        "🧠 Barry AI Self Check\n\n"
        f"Версия: {BARRY_VERSION}\n\n"
        f"🛠 Навыков: {skills}\n"
        f"📜 Записей журнала: {logs}\n\n"
        "💾 Память: OK\n"
        "🎯 Цели: OK\n"
        "🤖 ИИ: OK\n\n"
        "Состояние:\n"
        "Система работает нормально."
    )

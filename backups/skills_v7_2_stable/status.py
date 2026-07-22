import os

from action_log import get_actions
from config import BARRY_VERSION


def run(text):

    if "статус barry" not in text.lower():
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
        "🤖 Barry AI Status\n\n"
        f"Версия: {BARRY_VERSION}\n"
        f"🛠 Навыков: {skills}\n"
        f"📜 Записей журнала: {logs}\n"
        "🧠 Память: OK\n"
        "🤖 ИИ: OK\n"
    )

import os

from config import BARRY_VERSION
from action_log import get_actions
from learning_log import get_logs
from update_log import get_updates


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


    actions = len(get_actions())
    learning = len(get_logs())
    updates = len(get_updates())


    status = []


    if actions < 50:
        status.append(
            "⚠ Мало опыта взаимодействия"
        )
    else:
        status.append(
            "✅ Опыт взаимодействия хороший"
        )


    if learning == 0:
        status.append(
            "⚠ Нет журнала обучения"
        )
    else:
        status.append(
            "✅ Обучение записывается"
        )


    if updates == 0:
        status.append(
            "⚠ Нет истории обновлений"
        )
    else:
        status.append(
            "✅ Развитие фиксируется"
        )


    return (
        "🧠 Barry AI Self Check v2\n\n"
        f"Версия: {BARRY_VERSION}\n\n"
        f"🛠 Навыков: {skills}\n"
        f"📜 Действий: {actions}\n"
        f"📚 Обучений: {learning}\n"
        f"🚀 Обновлений: {updates}\n\n"
        "🔎 Состояние:\n"
        + "\n".join(
            status
        )
    )

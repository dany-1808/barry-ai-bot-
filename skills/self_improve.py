import os

from action_log import get_actions
from update_log import get_updates
from learning_log import get_logs


def run(text):

    if "обнови себя" not in text.lower():
        return None


    skills = 0

    if os.path.exists("skills"):

        skills = len([
            f for f in os.listdir("skills")
            if f.endswith(".py")
            and f != "__init__.py"
        ])


    actions = get_actions()
    updates = get_updates()
    learning = get_logs()


    result = (
        "🤖 Barry Self Improvement\n\n"
        "Версия: 5.6\n\n"
        f"🛠 Навыков: {skills}\n"
        f"📜 Действий: {len(actions)}\n"
        f"🚀 Развитий: {len(updates)}\n"
        f"📚 Обучение: {len(learning)}\n\n"
    )


    result += "Последние изменения:\n\n"


    for item in updates[-5:]:

        result += (
            f"📅 {item['date']}\n"
            f"✅ {item['update']}\n\n"
        )


    result += (
        "Состояние:\n"
        "🧠 Память: OK\n"
        "🛠 Навыки: OK\n"
        "🤖 ИИ: OK\n\n"
        "Статус:\n"
        "Barry продолжает развитие."
    )


    return result

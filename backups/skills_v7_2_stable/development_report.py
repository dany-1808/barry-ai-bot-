from action_log import get_actions
from learning_log import get_logs
import os
from difflib import get_close_matches


def run(text):

    low = text.lower().strip()


    commands = [
        "покажи развитие",
        "развитие barry",
        "отчет развития",
        "отчёт развития"
    ]


    if not get_close_matches(low, commands, n=1, cutoff=0.75):
        return None


    skills = 0

    if os.path.exists("skills"):

        skills = len([
            f for f in os.listdir("skills")
            if f.endswith(".py")
            and f != "__init__.py"
        ])


    actions = get_actions()
    learning = get_logs()


    result = (
        "🚀 Развитие Barry AI\n\n"
        "Версия: 5.5\n\n"
        f"🛠 Навыки: {skills}\n"
        f"📜 Действий: {len(actions)}\n"
        f"📔 Обучение: {len(learning)}\n\n"
        "Последние события:\n\n"
    )


    for item in actions[-5:]:

        result += (
            f"📅 {item['time']}\n"
            f"✅ {item['action']}\n\n"
        )


    result += "Статус:\nАктивное развитие."

    return result

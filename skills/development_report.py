import os

from action_log import get_actions
from learning_log import get_logs


def run(text):

    low = text.lower().strip()


    commands = [
        "покажи развитие",
        "развитие barry",
        "отчет развития",
        "отчёт развития",
        "приоритет развития"
    ]


    if low not in commands:
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
        "Версия: 6.0\n\n"
        f"🛠 Навыки: {skills}\n"
        f"📜 Действий: {len(actions)}\n"
        f"📔 Обучение: {len(learning)}\n\n"
        "Последние события:\n\n"
    )


    for item in actions[-5:]:

        if isinstance(item, dict):

            result += (
                f"📅 {item.get('time','')}\n"
                f"✅ {item.get('action','')}\n\n"
            )

        else:

            result += (
                "📅\n"
                f"✅ {str(item)}\n\n"
            )


    result += (
        "Статус:\n"
        "✅ Активное развитие.\n"
        "✅ Журналы работают.\n"
        "✅ Ошибки обработки исправлены."
    )


    return result

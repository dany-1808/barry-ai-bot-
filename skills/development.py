from action_log import get_actions
from learning_log import get_logs
import os


def run(text):

    if "развитие barry" not in text.lower():
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


    return (
        "📈 Развитие Barry AI\n\n"
        "Версия: 5.4\n\n"
        f"🛠 Навыки: {skills}\n"
        f"📜 Действий: {actions}\n"
        f"📚 Обучение: {learning}\n\n"
        "💾 Память: OK\n"
        "🤖 ИИ: OK\n\n"
        "Статус:\n"
        "Активное развитие."
    )

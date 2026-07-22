from memory import remember, recall, load_memory
from datetime import datetime
from ai_brain import ask_ai
from skill_manager import skill_manager


def think(user_input):

    text = user_input.strip()
    low = text.lower()


    # =====================
    # ОБЩИЕ ОТВЕТЫ CHAT
    # =====================

    if "привет" in low:

        return "Привет! Я Barry AI v7.0 🤖"


    if "кто ты" in low:

        return (
            "Я Barry AI v7.0. "
            "Персональный ИИ агент с памятью, "
            "анализом рынка и системой агентов."
        )


    if "как дела" in low:

        return "Все системы работают ✅"


    if "время" in low:

        return datetime.now().strftime("%H:%M:%S")



    # =====================
    # ПАМЯТЬ
    # =====================

    if low.startswith("меня зовут"):

        name = text[11:].strip()

        remember(
            "name",
            name
        )

        return (
            f"Запомнил. Приятно познакомиться, {name} 🤖"
        )



    if "кто я" in low:

        name = recall("name")

        if name:

            return (
                f"Ты {name}."
            )

        return (
            "Я пока не знаю твоё имя."
        )



    # =====================
    # SKILLS / AGENTS
    # =====================

    result = skill_manager.run(text)


    if result:

        return result



    # =====================
    # AI FALLBACK
    # =====================

    try:

        return ask_ai(text)


    except:

        return (
            "🧠 Barry AI v7.0\n\n"
            "Команда не распознана."
        )

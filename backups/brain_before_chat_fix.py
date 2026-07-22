from memory import remember, recall, load_memory
from datetime import datetime
from ai_brain import ask_ai
from skill_manager import skill_manager


def think(user_input):

    text = user_input.strip()
    low = text.lower()


    # =====================
    # СНАЧАЛА НАВЫКИ BARRY
    # =====================

    result = skill_manager.run(text)

    if result:
        return result



    # =====================
    # ПАМЯТЬ
    # =====================

    if low.startswith("меня зовут"):

        name = text[11:].strip()

        remember("name", name)

        return f"Запомнил. Тебя зовут {name}"



    if "кто я" in low:

        name = recall("name")

        if name:
            return f"Тебя зовут {name}"

        return "Я пока не знаю твоего имени"



    if low.startswith("запомни"):

        fact = text[7:].strip()

        memory = load_memory()

        facts = memory.get("facts", [])

        facts.append(fact)

        remember("facts", facts)

        return "✅ Запомнил"



    if "что ты помнишь" in low:

        memory = load_memory()

        answer = []


        name = recall("name")

        if name:
            answer.append(f"Имя: {name}")


        for fact in memory.get("facts", []):

            answer.append("• " + fact)


        if answer:
            return "\n".join(answer)


        return "Пока ничего не помню"



    # =====================
    # ОБЩИЕ ОТВЕТЫ
    # =====================

    if "привет" in low:

        return "Привет! Я Barry AI v5.6"



    if "кто ты" in low:

        return "Я Barry AI v5.6. Персональный помощник"



    if "как дела" in low:

        return "Все системы работают"



    if "время" in low:

        return datetime.now().strftime("%H:%M:%S")



    # =====================
    # ИИ
    # =====================

    return ask_ai(text)

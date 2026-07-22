import os


def run(text):

    if "проверка системы" not in text.lower():
        return None


    result = "🩺 Barry AI System Check\n\n"


    checks = [
        ("Память", "memory.py"),
        ("ИИ", "ai_brain.py"),
        ("Навыки", "skills"),
        ("Данные", "data"),
        ("Планы", "goals.py"),
    ]


    for name, path in checks:

        if os.path.exists(path):

            result += f"✅ {name}\n"

        else:

            result += f"❌ {name}\n"


    return result

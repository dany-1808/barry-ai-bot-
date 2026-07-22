import os
from datetime import datetime
from action_log import add_action


SKILLS_DIR = "skills"


def create_skill(name):

    filename = name.lower().replace(" ", "_")

    path = f"{SKILLS_DIR}/{filename}.py"


    if os.path.exists(path):
        return "Такой навык уже существует."


    code = f'''# Создан Barry AI
# Дата: {datetime.now()}


def run(text):

    low = text.lower()


    if "{name.lower()}" in low:

        return "Навык {name} активирован."


    return None
'''


    with open(path, "w", encoding="utf-8") as f:
        f.write(code)


    add_action(
        f"Создан новый навык: {filename}"
    )


    return f"✅ Создан новый навык: {filename}"

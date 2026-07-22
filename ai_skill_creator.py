from action_log import add_action
from update_log import add_update


def create_ai_skill(name):

    prompt = f"""
Создай Python навык для Barry AI.

Название навыка:
{name}

Требования:
- файл должен содержать функцию run(text)
- если команда подходит, вернуть ответ
- если нет, вернуть None
- только Python код без объяснений
"""


    code = ask_ai(prompt)


    if "```" in code:

        code = code.replace("```python", "")
        code = code.replace("```", "")


    filename = name.lower().replace(" ", "_")

    path = f"skills/{filename}.py"


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)



    # обычный журнал действий

    add_action(
        f"Создан ИИ навык: {filename}"
    )


    # журнал развития Barry

    add_update(
        f"Добавлен новый навык: {filename}"
    )


    return f"✅ ИИ создал навык: {filename}"

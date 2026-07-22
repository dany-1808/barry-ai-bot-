import os
import shutil
import py_compile
from datetime import datetime

from ai_brain import ask_ai
from update_log import add_update
from action_log import add_action


BACKUP_DIR = "backups"


def backup_skill(path):

    os.makedirs(
        BACKUP_DIR,
        exist_ok=True
    )

    name = os.path.basename(path)

    backup_name = (
        name.replace(
            ".py",
            ""
        )
        + "_"
        + datetime.now().strftime("%d%m%Y_%H%M")
        + ".py"
    )

    backup_path = os.path.join(
        BACKUP_DIR,
        backup_name
    )

    shutil.copy(
        path,
        backup_path
    )

    return backup_path



def upgrade_skill(name):

    path = f"skills/{name}.py"


    if not os.path.exists(path):

        return "❌ Навык не найден."



    backup = backup_skill(path)


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        old_code = f.read()



    prompt = f"""
Улучши Python навык Barry AI.

Требования:
- сохранить функцию run(text)
- сохранить совместимость
- вернуть только Python код
- не удалять существующий функционал

Старый код:

{old_code}
"""


    new_code = ask_ai(prompt)



    if "```" in new_code:

        new_code = new_code.replace(
            "```python",
            ""
        )

        new_code = new_code.replace(
            "```",
            ""
        )



    temp = path + ".test"


    with open(
        temp,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(new_code)



    try:

        py_compile.compile(
            temp,
            doraise=True
        )


    except Exception as e:

        os.remove(temp)

        return (
            "❌ Новая версия не прошла проверку:\n"
            + str(e)
        )



    os.replace(
        temp,
        path
    )


    add_action(
        f"Улучшен навык: {name}"
    )


    add_update(
        f"Улучшен навык: {name}. Backup: {backup}"
    )


    return (
        f"🚀 Навык {name} улучшен.\n"
        f"💾 Backup: {backup}"
    )

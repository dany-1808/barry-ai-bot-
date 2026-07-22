import py_compile
import os

from action_log import add_action
from update_log import add_update


def test_skill(name):

    path = f"skills/{name}.py"


    if not os.path.exists(path):

        return "Навык не найден."


    try:

        py_compile.compile(
            path,
            doraise=True
        )


        add_action(
            f"Проверен навык: {name} — успешно"
        )


        add_update(
            f"Проверен навык: {name} — ошибок нет"
        )


        return f"✅ Навык {name} работает без ошибок."


    except Exception as e:


        add_action(
            f"Ошибка проверки навыка: {name}"
        )


        add_update(
            f"Ошибка в навыке: {name}"
        )


        return (
            f"❌ Ошибка в навыке {name}:\n"
            f"{e}"
        )

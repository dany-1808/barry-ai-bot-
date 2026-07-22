import os

from learning_log import add_log
from update_log import get_updates
from action_log import get_actions

from skills.development_memory import save_development
from skills.error_memory import get_errors
from skills.skill_quality import check_quality
from skills.skill_efficiency import run as get_efficiency



def run(text):

    if "развивайся" not in text.lower():

        return None


    skills = 0


    if os.path.exists("skills"):

        skills = len([
            f for f in os.listdir("skills")
            if f.endswith(".py")
            and f != "__init__.py"
        ])


    actions = len(get_actions())

    updates = len(get_updates())

    errors = len(get_errors())


    quality = check_quality()


    efficiency = get_efficiency(
        "эффективность навыков"
    )


    problems = []

    improvements = []



    if actions < 50:

        problems.append(
            "Недостаточно опыта взаимодействия"
        )

        improvements.append(
            "Собрать больше опыта"
        )



    if errors > 0:

        problems.append(
            f"Есть ошибки: {errors}"
        )

        improvements.append(
            "Анализировать ошибки"
        )


    else:

        improvements.append(
            "Продолжать мониторинг ошибок"
        )



    if not problems:

        problems.append(
            "Критических проблем нет"
        )



    result = (

        "🧠 Barry Evolution Core v6\n\n"

        f"🛠 Навыков: {skills}\n"

        f"📜 Действий: {actions}\n"

        f"🚀 Обновлений: {updates}\n"

        f"⚠ Ошибок: {errors}\n\n"


        "🛠 Качество:\n"

        + quality

        +

        "\n\n📊 Эффективность:\n"

        + efficiency


        +

        "\n\n⚠ Анализ:\n"

        +

        "\n".join(
            "• " + x for x in problems
        )


        +

        "\n\n🚀 Улучшения:\n"

        +

        "\n".join(
            "• " + x for x in improvements
        )

    )


    add_log(result)

    save_development(result)


    return result

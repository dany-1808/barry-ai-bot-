import os
import json


USAGE_FILE = "data/skill_usage.json"



def get_all_skills():

    skills = []

    if os.path.exists("skills"):

        for file in os.listdir("skills"):

            if file.endswith(".py") and file != "__init__.py":

                skills.append(
                    file.replace(".py", "")
                )

    return skills




def get_usage():

    if not os.path.exists(USAGE_FILE):

        return {}


    with open(
        USAGE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)



    return {
        item["skill"].replace("skills.", ""):
        item["count"]
        for item in data
    }





def run(text):

    if "эффективность навыков" not in text.lower():

        return None



    skills = get_all_skills()

    usage = get_usage()



    active = []

    inactive = []



    for skill in skills:

        count = usage.get(skill, 0)


        if count > 0:

            active.append(
                (skill, count)
            )

        else:

            inactive.append(skill)



    active.sort(
        key=lambda x: x[1],
        reverse=True
    )



    result = (

        "📊 Barry Skill Efficiency\n\n"

        f"Всего навыков: {len(skills)}\n\n"

        "🔥 Используются:\n"

    )



    if active:

        for skill, count in active[:10]:

            result += (
                f"• {skill} — {count} раз\n"
            )

    else:

        result += "Нет данных\n"



    result += "\n💤 Не использовались:\n"



    for skill in inactive[:15]:

        result += (
            f"• {skill}\n"
        )



    result += (

        "\n🚀 Рекомендация:\n"

        "Улучшать активные модули и проверять неиспользуемые навыки."

    )


    return result

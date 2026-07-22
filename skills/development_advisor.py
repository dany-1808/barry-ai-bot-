import os
import json


USAGE_FILE = "data/skill_usage.json"


IMPORTANT_SKILLS = [

    "development_engine",
    "skill_analyzer",
    "skill_quality",
    "error_analyzer",
    "decision_memory",
    "decision_review"

]



def load_usage():

    if not os.path.exists(USAGE_FILE):

        return {}


    try:

        with open(
            USAGE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        result = {}

        for item in data:

            name = item.get(
                "skill",
                ""
            ).replace(
                "skills.",
                ""
            )

            result[name] = item.get(
                "count",
                0
            )


        return result


    except:

        return {}




def get_best_skill():


    usage = load_usage()


    skills = []



    if os.path.exists("skills"):


        for file in os.listdir("skills"):


            if file.endswith(".py"):

                name = file.replace(
                    ".py",
                    ""
                )


                if name != "__init__":

                    skills.append(name)




    ranking = []



    for skill in skills:


        score = usage.get(
            skill,
            0
        )


        if skill in IMPORTANT_SKILLS:

            score += 5



        ranking.append(
            (
                skill,
                score
            )
        )



    ranking.sort(
        key=lambda x:x[1],
        reverse=True
    )


    if ranking:

        return ranking[0]



    return (
        "нет",
        0
    )




def run(text):


    if "совет развития" not in text.lower():

        return None



    skill, score = get_best_skill()



    result = (

        "🧠 Barry Development Advisor\n\n"

        f"🎯 Главный кандидат развития:\n"

        f"• {skill}\n\n"

        f"⭐ Приоритет: {score}\n\n"

        "Причина:\n"

        "• Анализ активности модуля\n"

        "• Важность для системы\n"

        "• Возможность улучшения\n\n"

        "🚀 Следующий шаг:\n"

        "Проверить модуль и создать улучшение."

    )


    return result

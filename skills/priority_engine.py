import os
import json


USAGE_FILE = "data/skill_usage.json"


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
        item.get("count", 0)
        for item in data
    }



def get_skills():

    skills = []

    if os.path.exists("skills"):

        for file in os.listdir("skills"):

            if file.endswith(".py") and file != "__init__.py":

                skills.append(
                    file.replace(".py", "")
                )

    return skills



def run(text):

    if "приоритет развития" not in text.lower():

        return None


    usage = get_usage()

    skills = get_skills()


    scores = []


    for skill in skills:

        count = usage.get(skill, 0)

        score = count


        # важные системные модули получают бонус

        if skill in [
            "development_engine",
            "skill_analyzer",
            "skill_quality",
            "error_analyzer",
            "decision_memory"
        ]:

            score += 5


        scores.append(
            (
                skill,
                score,
                count
            )
        )



    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )



    result = (
        "🎯 Barry Priority Engine\n\n"
        "Главные кандидаты на улучшение:\n"
    )


    for skill, score, count in scores[:5]:

        result += (
            f"• {skill}\n"
            f"  📊 Использование: {count}\n"
            f"  ⭐ Приоритет: {score}\n\n"
        )


    result += (
        "🚀 Рекомендация:\n"
        "Улучшать сначала модули с высоким влиянием."
    )


    return result

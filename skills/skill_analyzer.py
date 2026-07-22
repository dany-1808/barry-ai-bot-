import os


def analyze_skills():

    if not os.path.exists("skills"):

        return "Папка skills не найдена."


    skills = []


    for file in os.listdir("skills"):

        if file.endswith(".py") and file != "__init__.py":

            skills.append(
                file.replace(".py", "")
            )



    result = (
        "🛠 Barry Skill Analyzer\n\n"
        f"Всего навыков: {len(skills)}\n\n"
    )


    result += "📚 Список навыков:\n"


    for skill in skills:

        result += f"• {skill}\n"



    result += (
        "\n🚀 Рекомендация Barry:\n"
        "Проверять навыки перед улучшением "
        "и развивать самые важные модули."
    )


    return result



def run(text):

    if "анализ навыков" not in text.lower():

        return None


    return analyze_skills()

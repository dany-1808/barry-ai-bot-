import os
import json
from datetime import datetime


FILE = "data/skill_registry.json"



def scan_skills():

    skills = []


    if os.path.exists("skills"):

        for file in os.listdir("skills"):

            if file.endswith(".py") and file != "__init__.py":

                skills.append(
                    file.replace(".py", "")
                )


    return sorted(skills)




def save_registry():

    os.makedirs(
        "data",
        exist_ok=True
    )


    data = {

        "date": datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        ),

        "count": len(scan_skills()),

        "skills": scan_skills()

    }



    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )



    return data




def get_registry():

    if not os.path.exists(FILE):

        return save_registry()


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)





def run(text):

    if "реестр навыков" not in text.lower():

        return None



    data = save_registry()



    result = (

        "📚 Barry Skill Registry\n\n"

        f"Всего навыков: {data['count']}\n\n"

        "Модули:\n"

    )



    for skill in data["skills"]:

        result += f"• {skill}\n"



    return result

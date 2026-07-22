import os


def run(text):

    low = text.lower()


    if low == "покажи навыки":

        files = []

        for file in os.listdir("skills"):

            if file.endswith(".py") and file != "__init__.py":

                files.append(file.replace(".py", ""))


        if not files:
            return "Навыков нет."


        result = "🛠 Навыки Barry:\n\n"

        for i, skill in enumerate(files, 1):

            result += f"{i}. {skill}\n"


        return result



    if low.startswith("удали навык"):

        name = text[11:].strip()

        filename = f"skills/{name}.py"


        if os.path.exists(filename):

            os.remove(filename)

            return f"🗑 Навык удалён: {name}"


        return "Такого навыка нет."


    return None

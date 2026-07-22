from ai_skill_creator import create_ai_skill


def run(text):

    low = text.lower()


    if low.startswith("создай навык"):

        name = text[len("создай навык"):].strip()


        if not name:
            return "Напиши название навыка."


        return create_ai_skill(name)


    return None

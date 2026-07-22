from skill_upgrader import upgrade_skill


def run(text):

    low = text.lower()


    if low.startswith("улучши навык"):

        name = text[len("улучши навык"):].strip()

        return upgrade_skill(name)


    return None

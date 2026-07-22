from skill_tester import test_skill


def run(text):

    low = text.lower()


    if low.startswith("проверь навык"):

        name = text[len("проверь навык"):].strip()

        return test_skill(name)


    return None

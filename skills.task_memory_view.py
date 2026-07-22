from task_memory import load_context


def run(text):

    low = text.lower().strip()


    if "покажи память задачи" not in low:
        return None


    data = load_context()


    if not data:
        return "🧠 Память задач пуста."


    result = "🧠 Barry Task Memory:\n\n"


    for key, value in data.items():

        result += f"🔹 {key}\n"

        result += str(value)

        result += "\n\n"


    return result

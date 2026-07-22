from knowledge import add, search


def run(text):

    low = text.lower()


    if low.startswith("добавь в знания"):

        content = text[16:].strip()

        if ":" in content:

            title, info = content.split(":", 1)

            add(
                title.strip(),
                info.strip()
            )

            return "✅ Знание сохранено."


        return "Формат: добавь в знания тема: текст"



    if low.startswith("что ты знаешь про"):

        title = text[18:].strip()

        result = search(title)

        if result:
            return f"🧠 {title}:\n{result}"

        return "Пока ничего не знаю об этом."


    return None

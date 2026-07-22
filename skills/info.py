from search_engine import search
from action_log import add_action
from update_log import add_update


def run(text):

    low = text.lower().strip()


    if low == "новости":

        return (
            "📰 Новости Barry\n\n"
            "Модуль новостей готов."
        )


    if low.startswith("найди информацию"):

        query = text[len("найди информацию"):].strip()


        if not query:
            return "Укажи тему поиска."


        add_action(
            f"Поиск информации: {query}"
        )


        result = search(query)


        add_update(
            f"Поиск выполнен: {query}"
        )


        return (
            f"🔎 Поиск: {query}\n\n"
            f"{result}"
        )


    if low.startswith("расскажи про"):

        topic = text[len("расскажи про"):].strip()


        if not topic:
            return "Укажи тему."


        result = search(topic)


        return (
            f"📚 Информация: {topic}\n\n"
            f"{result}"
        )


    return None

from update_log import get_updates


def run(text):

    if "что нового в barry" not in text.lower():
        return None


    updates = get_updates()


    if not updates:

        return "📘 История обновлений пуста."


    result = "🚀 История развития Barry:\n\n"


    for item in updates[-10:]:

        result += (
            f"📅 {item['date']}\n"
            f"✅ {item['update']}\n\n"
        )


    return result

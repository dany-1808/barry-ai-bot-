def run(text):
    text = text.lower().replace("посчитай", "").strip()

    try:
        result = eval(text)
        return f"Ответ: {result}"
    except:
        return None

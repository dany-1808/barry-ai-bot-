import os


FILE = "data/decisions.txt"


def run(text):

    if text.lower().strip() != "анализ решений":
        return None


    if not os.path.exists(FILE):
        return "📊 Нет истории решений."


    with open(FILE, "r", encoding="utf-8") as f:
        data = f.read()


    total = data.count("Инструмент:")

    low_conf = data.count("Уверенность Barry: 50%")
    weak_adx = data.count("ADX очень слабый")
    observe = data.count("наблюдать")


    return (
        "🧠 Barry Decision Review\n\n"
        f"Всего решений: {total}\n\n"
        f"⚠ Решений с уверенностью 50%: {low_conf}\n"
        f"📉 Слабый ADX встречался: {weak_adx}\n"
        f"👀 Наблюдение выбрано: {observe}\n\n"
        "Вывод Barry:\n"
        "Нужно улучшать фильтр силы движения (ADX) "
        "и избегать слабых трендов."
    )

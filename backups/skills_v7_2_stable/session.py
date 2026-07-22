import json


def run(text):

    low = text.lower()

    if low != "начинаем торговлю":
        return None

    with open("data/settings.json", "r", encoding="utf-8") as f:
        s = json.load(f)

    risk = s["deposit"] * s["risk_percent"] / 100

    return f"""
📈 Торговая сессия

👤 Трейдер: {s["name"]}

💰 Депозит: {s["deposit"]}

⚠ Риск: {risk:.2f}

📊 Стратегия:
{s["strategy"]}

✅ Чек-лист

□ Жду сигнал

□ Не спешу

□ Следую стратегии

□ Не увеличиваю риск

Удачной торговли!
"""

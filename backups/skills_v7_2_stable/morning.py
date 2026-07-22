from datetime import datetime
import json
import os


def run(text):

    if text.lower().strip() != "утренний запуск":
        return None

    if not os.path.exists("data/settings.json"):
        return "Нет файла настроек."

    with open("data/settings.json", "r", encoding="utf-8") as f:
        s = json.load(f)

    risk = s["deposit"] * s["risk_percent"] / 100

    now = datetime.now().strftime("%H:%M")

    return f"""
🌅 Доброе утро, {s["name"]}

🕒 Время: {now}

💰 Депозит: {s["deposit"]}

⚠ Риск на сделку:
{risk:.2f}

📊 Стратегия:
{s["strategy"]}

=====================

Чек-лист

✅ Не торопиться

✅ Ждать подтверждение

✅ Следовать стратегии

✅ Не превышать риск

Удачной торговли!
"""

import os

FILE = "data/trades.txt"


def run(text):

    low = text.lower().strip()

    os.makedirs("data", exist_ok=True)

    if low.startswith("сделка "):

        trade = text[8:]

        with open(FILE, "a", encoding="utf-8") as f:
            f.write(trade + "\n")

        return "✅ Сделка сохранена."

    if low == "покажи сделки":

        if not os.path.exists(FILE):
            return "Журнал пуст."

        with open(FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()

        if not data:
            return "Журнал пуст."

        return "📒 Журнал сделок:\n\n" + data

    if low == "итоги дня":

        if not os.path.exists(FILE):
            return "Нет сделок."

        with open(FILE, "r", encoding="utf-8") as f:
            trades = [x.strip() for x in f if x.strip()]

        total = len(trades)
        win = 0
        lose = 0

        for trade in trades:

            if "+" in trade:
                win += 1

            elif "-" in trade:
                lose += 1

        return (
            f"📊 Итоги дня\n\n"
            f"Всего сделок: {total}\n"
            f"✅ Прибыльных: {win}\n"
            f"❌ Убыточных: {lose}"
        )

    return None

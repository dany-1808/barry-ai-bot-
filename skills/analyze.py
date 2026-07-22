import os

FILE = "data/trades.txt"


def run(text):

    if text.lower().strip() != "проанализируй сделки":
        return None

    if not os.path.exists(FILE):
        return "Нет сделок для анализа."

    with open(FILE, "r", encoding="utf-8") as f:
        trades = [x.strip() for x in f if x.strip()]

    wins = 0
    losses = 0
    streak = 0
    max_streak = 0

    for trade in trades:

        if "+" in trade:
            wins += 1
            streak = 0

        elif "-" in trade:
            losses += 1
            streak += 1

            if streak > max_streak:
                max_streak = streak

    total = wins + losses

    if total == 0:
        winrate = 0
    else:
        winrate = wins / total * 100

    advice = []

    if max_streak >= 3:
        advice.append("⚠ У тебя была серия убытков. После 3 минусов подряд лучше сделать перерыв.")

    if winrate >= 60:
        advice.append("✅ Хороший винрейт. Продолжай соблюдать стратегию.")

    elif winrate < 50:
        advice.append("⚠ Винрейт низкий. Проверь дисциплину и точки входа.")

    if len(advice) == 0:
        advice.append("Продолжай собирать статистику.")

    return (
        f"📊 Анализ сделок\n\n"
        f"Всего: {total}\n"
        f"✅ Побед: {wins}\n"
        f"❌ Поражений: {losses}\n"
        f"🎯 WinRate: {winrate:.1f}%\n"
        f"📉 Максимальная серия убытков: {max_streak}\n\n"
        + "\n".join(advice)
    )

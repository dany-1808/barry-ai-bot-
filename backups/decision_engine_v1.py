def analyze(
    trend,
    rsi,
    adx
):

    decision = []


    # тренд

    if "Вверх" in trend:

        decision.append(
            "🟢 Тренд восходящий"
        )

    elif "Вниз" in trend:

        decision.append(
            "🔴 Тренд нисходящий"
        )


    # RSI

    if rsi >= 70:

        decision.append(
            "⚠ RSI высокий — рынок перегрет"
        )

    elif rsi <= 30:

        decision.append(
            "🟢 RSI низкий — возможен отскок"
        )

    else:

        decision.append(
            "✅ RSI в рабочей зоне"
        )


    # ADX

    if adx >= 25:

        decision.append(
            "💪 Сила движения подтверждена"
        )

    else:

        decision.append(
            "😐 Сила движения слабая"
        )


    # итог

    if rsi >= 70 and adx < 25:

        decision.append(
            "⏳ Решение Barry: ждать откат"
        )


    elif adx >= 25:

        decision.append(
            "📈 Решение Barry: тренд можно рассматривать"
        )


    else:

        decision.append(
            "👀 Решение Barry: наблюдать"
        )


    return "\n".join(decision)



def run(text):

    return None

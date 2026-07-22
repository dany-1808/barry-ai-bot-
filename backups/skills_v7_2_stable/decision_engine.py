from skills import confidence_engine


def analyze(
    trend,
    rsi,
    adx,
    ma20=None,
    ma50=None
):

    result = []


    if "Вверх" in trend:

        result.append(
            "🟢 Тренд восходящий"
        )

    elif "Вниз" in trend:

        result.append(
            "🔴 Тренд нисходящий"
        )


    if rsi >= 70:

        result.append(
            "⚠ RSI высокий — рынок перегрет"
        )

    elif rsi <= 30:

        result.append(
            "🟢 RSI низкий — возможен отскок"
        )

    else:

        result.append(
            "✅ RSI в рабочей зоне"
        )


    if adx >= 25:

        result.append(
            "💪 Сила движения подтверждена"
        )

    else:

        result.append(
            "😐 Сила движения слабая"
        )


    if ma20 and ma50:

        confidence = confidence_engine.calculate(
            trend,
            rsi,
            adx,
            ma20,
            ma50
        )

        result.append("")

        result.append(
            f"🧠 Уверенность Barry: {confidence['confidence']}%"
        )

        for reason in confidence["reasons"]:

            result.append(
                reason
            )


    if rsi >= 70 and adx < 25:

        result.append(
            "⏳ Решение Barry: ждать откат"
        )

    elif adx >= 25:

        result.append(
            "📈 Решение Barry: рассмотреть вход"
        )

    else:

        result.append(
            "👀 Решение Barry: наблюдать"
        )


    return "\n".join(result)



def run(text):

    return None

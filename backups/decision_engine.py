from skills import confidence_engine


def analyze(
    trend,
    rsi,
    adx,
    ma20=None,
    ma50=None
):

    result = []


    # =====================
    # ТРЕНД
    # =====================

    if "Вверх" in trend:

        result.append(
            "🟢 Тренд восходящий"
        )

    elif "Вниз" in trend:

        result.append(
            "🔴 Тренд нисходящий"
        )

    else:

        result.append(
            "⚪ Тренд не определён"
        )


    # =====================
    # RSI
    # =====================

    if rsi >= 80:

        result.append(
            "🔴 RSI экстремально перегрет"
        )

    elif rsi >= 70:

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


    # =====================
    # ADX
    # =====================

    if adx >= 25:

        result.append(
            "💪 Сила движения подтверждена"
        )

    elif adx >= 15:

        result.append(
            "😐 Сила движения слабая"
        )

    else:

        result.append(
            "🔴 Тренд почти отсутствует"
        )


    # =====================
    # УВЕРЕННОСТЬ
    # =====================

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


    # =====================
    # РЕШЕНИЕ BARRY
    # =====================

    if rsi >= 80 and adx < 25:

        result.append(
            "⏳ Решение Barry: ждать сильный откат"
        )


    elif rsi >= 70 and adx < 25:

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

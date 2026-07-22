from skills import confidence_engine


def analyze(
    trend,
    rsi,
    adx,
    ma20=None,
    ma50=None
):

    decision = []


    # базовый анализ тренда

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



    # Confidence

    if ma20 is not None and ma50 is not None:

        confidence = confidence_engine.calculate(
            trend,
            rsi,
            adx,
            ma20,
            ma50
        )


        decision.append(
            ""
        )


        decision.append(
            f"🧠 Уверенность Barry: "
            f"{confidence['confidence']}%"
        )


        decision.extend(
            confidence["reasons"]
        )



    # итоговое решение

    if rsi >= 70 and adx < 25:

        decision.append(
            "⏳ Решение Barry: ждать откат"
        )


    elif adx >= 25:

        decision.append(
            "📈 Решение Barry: рассмотреть вход"
        )


    else:

        decision.append(
            "👀 Решение Barry: наблюдать"
        )


    return "\n".join(decision)



def run(text):

    return None

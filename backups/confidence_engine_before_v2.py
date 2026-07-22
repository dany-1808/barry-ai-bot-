def calculate(
    trend,
    rsi,
    adx,
    ma20,
    ma50
):

    score = 50


    reasons = []


    # MA тренд

    if ma20 > ma50:

        score += 15

        reasons.append(
            "✅ MA подтверждают рост"
        )

    else:

        score -= 15

        reasons.append(
            "⚠ MA показывают слабость"
        )



    # RSI

    if rsi >= 70:

        score -= 10

        reasons.append(
            "⚠ RSI перегрет"
        )

    elif rsi <= 30:

        score += 10

        reasons.append(
            "🟢 RSI низкий"
        )

    else:

        reasons.append(
            "✅ RSI нормальный"
        )



    # ADX

    if adx >= 25:

        score += 15

        reasons.append(
            "💪 ADX подтверждает силу"
        )

    else:

        reasons.append(
            "😐 ADX слабый"
        )



    # границы

    if score < 0:

        score = 0


    if score > 100:

        score = 100



    return {

        "confidence": score,

        "reasons": reasons

    }



def run(text):

    return None

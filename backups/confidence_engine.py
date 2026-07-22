def calculate(
    trend,
    rsi,
    adx,
    ma20,
    ma50
):

    score = 50

    reasons = []


    # =====================
    # MA
    # =====================

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


    # =====================
    # RSI
    # =====================

    if rsi >= 80:

        score -= 25

        reasons.append(
            "🔴 RSI экстремально перегрет"
        )


    elif rsi >= 70:

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


    # =====================
    # ADX
    # =====================

    if adx >= 25:

        score += 15

        reasons.append(
            "💪 ADX подтверждает силу"
        )


    elif adx >= 15:

        score -= 5

        reasons.append(
            "😐 ADX средний"
        )


    else:

        score -= 15

        reasons.append(
            "🔴 ADX очень слабый"
        )


    # =====================
    # Ограничения
    # =====================

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

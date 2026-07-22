# ==========================
# Barry Decision Engine v3.0
# Full Trading Logic
# ==========================


def analyze(
    trend,
    rsi,
    pattern_signal,
    candle_power,
    pattern_name=""
):

    score = 0
    reasons = []


    # TREND

    if trend == "Вверх":

        score += 25
        reasons.append("Trend рост +25")

    elif trend == "Вниз":

        score += 25
        reasons.append("Trend снижение +25")

    else:

        score -= 10
        reasons.append("Флэт -10")



    # RSI ZONE 30-70

    if 30 <= rsi <= 70:

        score += 20
        reasons.append("RSI зона 30-70 +20")

    elif rsi > 70:

        score -= 10
        reasons.append("RSI перегрев -10")

    elif rsi < 30:

        score += 10
        reasons.append("RSI перепроданность +10")



    # PATTERN

    name = pattern_name.lower()


    if "поглощение" in name:

        score += 30
        reasons.append("Поглощение +30")


    elif "три быч" in name:

        score += 25
        reasons.append("3 бычьи свечи +25")


    elif "три медв" in name:

        score += 25
        reasons.append("3 медвежьи свечи +25")


    elif "быч" in name:

        score += 10
        reasons.append("Бычий паттерн +10")


    elif "медв" in name:

        score += 10
        reasons.append("Медвежий паттерн +10")


    else:

        reasons.append("Pattern нет сигнала")



    # CANDLE POWER

    if candle_power >= 70:

        score += 15
        reasons.append("Сильная свеча +15")


    elif candle_power >= 40:

        score += 5
        reasons.append("Средняя свеча +5")


    else:

        score -= 5
        reasons.append("Слабая свеча -5")



    score = max(
        0,
        min(score,100)
    )


    decision = "WAIT"


    # ENTRY FILTER

    if score >= 70:

        if trend == "Вверх" and rsi <= 70:

            decision = "BUY"


        elif trend == "Вниз" and rsi >= 30:

            decision = "SELL"



    if score >= 90:

        quality = "A+"

    elif score >= 75:

        quality = "A"

    elif score >= 60:

        quality = "B"

    else:

        quality = "C"



    return {

        "decision": decision,

        "score": score,

        "quality": quality,

        "reasons": reasons

    }



def run(text):

    return None

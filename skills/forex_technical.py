from skills.forex_candles import get_candles
from skills.indicator_engine import calculate
from skills import decision_engine
from skills import decision_memory


SUPPORTED = [
    "EURUSD",
    "GBPUSD",
    "AUDUSD",
    "AUDNZD"
]


def run(text):

    text = text.upper()


    pair = None

    for item in SUPPORTED:

        if item in text:
            pair = item
            break


    if pair is None:
        return None


    candles = get_candles(pair)


    if not candles:

        return "❌ Нет свечей Forex"


    prices = [
        candle["close"]
        for candle in candles
    ]


    data = calculate(prices)


    ema7 = data["EMA7"]
    ema21 = data["EMA21"]
    rsi = data["RSI"]
    trend = data["Trend"]


    if trend == "Вверх" and rsi < 70:

        decision = "BUY"


    elif trend == "Вниз" and rsi > 30:

        decision = "SELL"


    else:

        decision = "WAIT"



    result = (

        "📊 Barry Forex Technical v2\n\n"

        f"💱 Пара: {pair}\n\n"

        "📈 Индикаторы:\n"

        f"EMA7: {ema7:.5f}\n"
        f"EMA21: {ema21:.5f}\n"
        f"RSI: {rsi:.1f}\n"
        f"Тренд: {trend}\n\n"

        "🧠 Решение Barry:\n"

        f"{decision}"

    )


    decision_memory.save_decision(
        pair,
        result
    )


    return result

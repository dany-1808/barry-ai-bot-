# ==========================
# Barry Trader Agent v11.0
# Full Trading Brain
# ==========================

from skills.forex_candles import get_candles
from skills.indicator_engine import calculate
from skills.market_data_agent import get_market
from skills.pattern_agent import analyze as pattern_analyze
from skills.decision_engine import analyze as decision_analyze
from skills.risk_agent import analyze as risk_analyze


SUPPORTED = [
    "EURUSD",
    "GBPUSD",
    "AUDUSD",
    "AUDNZD"
]


def get_pair(text):

    text = text.upper()

    for pair in SUPPORTED:

        if pair in text:

            return pair

    return "EURUSD"



def candle_power(candles):

    last = candles[-1]

    body = abs(
        last["close"] - last["open"]
    )

    size = (
        last["high"] - last["low"]
    )

    if size == 0:

        return 0

    return round(
        body / size * 100,
        1
    )



def run(text):


    if "анализ трейдера" not in text.lower():

        return None



    pair = get_pair(text)



    market = get_market(pair)


    if not market:

        return "❌ Нет данных рынка"



    candles = get_candles(pair)


    if not candles:

        return "❌ Нет данных свечей"



    prices = [
        c["close"]
        for c in candles
    ]



    data = calculate(prices)



    ema7 = data["EMA7"]

    ema21 = data["EMA21"]

    rsi = data["RSI"]

    trend = data["Trend"]



    power = candle_power(candles)



    pattern = pattern_analyze(candles)



    decision = decision_analyze(

        trend,

        rsi,

        pattern["signal"],

        power,

        pattern["pattern"]

    )



    risk = risk_analyze(

        decision["decision"],

        decision["score"],

        rsi

    )



    result = (

        "🤖 Barry Trader Agent v11.0\n\n"

        f"💱 Пара: {pair}\n"

        f"💰 Цена рынка: {market['price']:.5f}\n\n"


        "📊 Индикаторы:\n"

        f"EMA7: {ema7:.5f}\n"

        f"EMA21: {ema21:.5f}\n"

        f"RSI: {rsi:.2f}\n"

        f"Тренд: {trend}\n\n"


        "🕯 Pattern Agent:\n"

        f"{pattern['pattern']}\n"

        f"Сила свечи: {power}%\n\n"


        "🧠 Barry Decision Engine v3:\n"

        f"{decision['decision']}\n\n"


        f"🎯 Score: {decision['score']}/100\n"

        f"🏆 Класс: {decision['quality']}\n\n"


        "📋 Причины:\n"
    )



    for reason in decision["reasons"]:

        result += f"• {reason}\n"



    result += "\n🛡 Barry Risk Agent\n\n"

    result += risk["status"] + "\n"



    for warning in risk["warnings"]:

        result += f"• {warning}\n"



    return result

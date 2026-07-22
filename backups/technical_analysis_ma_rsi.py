import requests


def get_candles():

    try:
        url = (
            "https://api.binance.com/api/v3/klines"
            "?symbol=BTCUSDT"
            "&interval=1h"
            "&limit=100"
        )

        r = requests.get(
            url,
            timeout=5
        )

        return r.json()

    except:
        return None



def ma(values, period):

    if len(values) < period:
        return None

    return sum(values[-period:]) / period



def rsi(values, period=14):

    if len(values) < period + 1:
        return None

    gains = 0
    losses = 0


    for i in range(
        len(values)-period,
        len(values)
    ):

        diff = values[i] - values[i-1]

        if diff > 0:
            gains += diff
        else:
            losses += abs(diff)


    if losses == 0:
        return 100


    rs = gains / losses

    return 100 - (100 / (1 + rs))



def run(text):

    if "тех анализ" not in text.lower():
        return None


    candles = get_candles()


    if not candles:
        return "❌ Нет данных рынка"


    closes = [
        float(x[4])
        for x in candles
    ]


    price = closes[-1]

    ma20 = ma(closes, 20)
    ma50 = ma(closes, 50)

    rsi_value = rsi(closes)


    if ma20 > ma50:
        trend = "🟢 Восходящий"

    else:
        trend = "🔴 Нисходящий"


    return (
        "📊 Barry Technical Analysis\n\n"
        f"₿ BTC цена: ${price:.2f}\n\n"
        f"Тренд: {trend}\n\n"
        f"MA20: {ma20:.2f}\n"
        f"MA50: {ma50:.2f}\n"
        f"RSI: {rsi_value:.1f}\n\n"
        "🧠 Анализ завершён."
    )

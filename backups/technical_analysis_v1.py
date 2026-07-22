import requests


def get_symbol(text):

    text = text.lower()

    if "btc" in text or "bitcoin" in text:
        return "BTCUSDT"

    if "eth" in text:
        return "ETHUSDT"

    # пока оставляем валюты как заготовку
    if "eurusd" in text or "eur/usd" in text:
        return "EURUSD"

    if "audnzd" in text or "aud/nzd" in text:
        return "AUDNZD"

    return "BTCUSDT"



def get_candles(symbol):

    try:

        # крипто через Binance
        if symbol.endswith("USDT"):

            url = (
                "https://api.binance.com/api/v3/klines"
                f"?symbol={symbol}"
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

    return sum(values[-period:]) / period



def rsi(values, period=14):

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



def adx(values, period=14):

    moves = []

    for i in range(1, len(values)):

        moves.append(
            abs(values[i]-values[i-1])
        )


    avg = sum(
        moves[-period:]
    ) / period


    return (
        avg / values[-1]
    ) * 1000



def run(text):

    if "тех анализ" not in text.lower():
        return None


    symbol = get_symbol(text)


    if not symbol.endswith("USDT"):

        return (
            "📊 Barry Technical Analysis\n\n"
            f"Инструмент: {symbol}\n\n"
            "⚙️ Валютный источник готовится."
        )


    candles = get_candles(symbol)


    if not candles:
        return "❌ Нет данных рынка"


    closes = [
        float(x[4])
        for x in candles
    ]


    price = closes[-1]

    ma20 = ma(
        closes,
        20
    )

    ma50 = ma(
        closes,
        50
    )

    rsi_value = rsi(
        closes
    )

    adx_value = adx(
        closes
    )


    if ma20 > ma50:
        trend = "🟢 Вверх"
    else:
        trend = "🔴 Вниз"


    return (
        "📊 Barry Technical Analysis\n\n"
        f"Инструмент: {symbol}\n"
        f"Цена: ${price:.2f}\n\n"
        f"Тренд: {trend}\n\n"
        f"MA20: {ma20:.2f}\n"
        f"MA50: {ma50:.2f}\n"
        f"RSI: {rsi_value:.1f}\n"
        f"ADX: {adx_value:.1f}\n\n"
        "🧠 Анализ Barry готов."
    )

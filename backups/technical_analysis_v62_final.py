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
            abs(values[i] - values[i-1])
        )


    avg_move = sum(
        moves[-period:]
    ) / period


    return (
        avg_move / values[-1]
    ) * 1000



def market_comment(ma20, ma50, rsi_value, adx_value):

    result = []


    if ma20 > ma50:
        result.append(
            "📈 Тренд вверх подтверждён"
        )
    else:
        result.append(
            "📉 Тренд вниз"
        )


    if rsi_value > 70:

        result.append(
            "⚠ RSI высокий — рынок перегрет"
        )

    elif rsi_value < 30:

        result.append(
            "🟢 RSI низкий — возможна зона интереса"
        )

    else:

        result.append(
            "⚖ RSI в нормальной зоне"
        )



    if adx_value > 25:

        result.append(
            "💪 Движение имеет силу"
        )

    else:

        result.append(
            "😐 Сила движения слабая"
        )



    if (
        ma20 > ma50
        and rsi_value < 70
        and adx_value > 25
    ):

        advice = (
            "🟢 Условия выглядят лучше для поиска входа"
        )

    elif rsi_value > 70:

        advice = (
            "⏳ Не гнаться за ценой. Ждать откат"
        )

    else:

        advice = (
            "👀 Ждать подтверждение"
        )


    return (
        "\n".join(result)
        +
        "\n\nРешение Barry:\n"
        +
        advice
    )



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


    comment = market_comment(
        ma20,
        ma50,
        rsi_value,
        adx_value
    )


    return (
        "📊 Barry Technical Analysis\n\n"
        f"₿ BTC цена: ${price:.2f}\n\n"
        f"MA20: {ma20:.2f}\n"
        f"MA50: {ma50:.2f}\n"
        f"RSI: {rsi_value:.1f}\n"
        f"ADX: {adx_value:.1f}\n\n"
        "🧠 Анализ Barry:\n"
        f"{comment}"
    )

def ema(values, period):

    if len(values) < period:
        return None

    multiplier = 2 / (period + 1)

    ema_value = sum(values[:period]) / period

    for price in values[period:]:

        ema_value = (
            price - ema_value
        ) * multiplier + ema_value

    return ema_value



def rsi(values, period=14):

    if len(values) <= period:
        return None


    gains = []
    losses = []


    for i in range(1, len(values)):

        change = values[i] - values[i-1]

        if change >= 0:
            gains.append(change)
            losses.append(0)

        else:
            gains.append(0)
            losses.append(abs(change))


    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period


    if avg_loss == 0:
        return 100


    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))



def calculate(values):

    ema7 = ema(values, 7)
    ema21 = ema(values, 21)
    rsi_value = rsi(values)


    if ema7 > ema21:
        trend = "Вверх"

    elif ema7 < ema21:
        trend = "Вниз"

    else:
        trend = "Флэт"


    return {

        "EMA7": ema7,
        "EMA21": ema21,
        "RSI": rsi_value,
        "Trend": trend
    }

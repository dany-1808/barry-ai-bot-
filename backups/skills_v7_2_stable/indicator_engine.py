def sma(values, period):

    if len(values) < period:

        return None


    data = values[-period:]


    return sum(data) / period



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


    avg_gain = sum(
        gains[-period:]
    ) / period


    avg_loss = sum(
        losses[-period:]
    ) / period


    if avg_loss == 0:

        return 100


    rs = avg_gain / avg_loss


    return 100 - (
        100 / (1 + rs)
    )



def trend(ma20, ma50):

    if ma20 > ma50:

        return "Вверх"

    else:

        return "Вниз"



def calculate(values):

    ma20 = sma(
        values,
        20
    )

    ma50 = sma(
        values,
        50
    )

    rsi_value = rsi(
        values
    )


    return {

        "MA20": ma20,
        "MA50": ma50,
        "RSI": rsi_value,
        "Trend": trend(
            ma20,
            ma50
        )

    }

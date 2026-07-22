import requests


def get_price(pair):

    try:

        url = "https://open.er-api.com/v6/latest/AUD"

        r = requests.get(
            url,
            timeout=5
        )

        data = r.json()

        rates = data["rates"]

        if pair == "AUDNZD":
            return rates["NZD"]

        if pair == "AUDUSD":
            return rates["USD"]

        return None


    except:

        return None



def create_fake_history(price):

    """
    Временная история.
    Следующим шагом заменим
    на реальные свечи Forex.
    """

    history = []

    for i in range(100):

        history.append(
            price * (1 + (i-50) * 0.0001)
        )

    return history



def ma(values, period):

    return sum(
        values[-period:]
    ) / period



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

    return 100 - (100/(1+rs))



def run(text):

    text = text.lower()


    pair = None


    if "audnzd" in text:
        pair = "AUDNZD"


    if pair is None:
        return None


    price = get_price(pair)


    if price is None:
        return "❌ Нет данных Forex"


    history = create_fake_history(
        price
    )


    ma20 = ma(
        history,
        20
    )

    ma50 = ma(
        history,
        50
    )

    rsi_value = rsi(
        history
    )


    if ma20 > ma50:

        trend = "🟢 Вверх"

    else:

        trend = "🔴 Вниз"



    return (
        "📊 Barry Forex Technical Analysis\n\n"
        f"💱 Пара: {pair}\n"
        f"Цена: {price:.5f}\n\n"
        f"Тренд: {trend}\n"
        f"MA20: {ma20:.5f}\n"
        f"MA50: {ma50:.5f}\n"
        f"RSI: {rsi_value:.1f}\n\n"
        "🧠 Анализ Barry готов."
    )

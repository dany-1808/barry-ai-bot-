import requests

from skills import decision_engine


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

            return float(
                rates["NZD"]
            )


        if pair == "AUDUSD":

            return float(
                rates["USD"]
            )


        return None


    except:

        return None



def calculate():

    # временные значения
    # позже заменим на реальные свечи Forex

    ma20 = 1.20150
    ma50 = 1.19970

    rsi_value = 65.0

    adx_value = 18.0


    if ma20 > ma50:

        trend = "Вверх"

    else:

        trend = "Вниз"


    return (
        trend,
        ma20,
        ma50,
        rsi_value,
        adx_value
    )



def run(text):

    text = text.lower()


    pair = None


    if "audnzd" in text:

        pair = "AUDNZD"


    elif "audusd" in text:

        pair = "AUDUSD"


    else:

        return None



    price = get_price(pair)


    if price is None:

        return "❌ Нет данных Forex"



    trend, ma20, ma50, rsi_value, adx_value = calculate()



    decision = decision_engine.analyze(
        trend,
        rsi_value,
        adx_value
    )



    return (

        "📊 Barry Forex Technical Analysis\n\n"

        f"💱 Пара: {pair}\n"

        f"Цена: {price:.5f}\n\n"

        f"Тренд: 🟢 {trend}\n\n"

        f"MA20: {ma20:.5f}\n"
        f"MA50: {ma50:.5f}\n"
        f"RSI: {rsi_value:.1f}\n"
        f"ADX: {adx_value:.1f}\n\n"

        "🧠 Решение Barry:\n"

        f"{decision}"

    )

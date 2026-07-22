import requests

from skills import decision_engine


def get_price():

    try:

        url = (
            "https://api.coingecko.com/api/v3/"
            "simple/price"
            "?ids=bitcoin&vs_currencies=usd"
        )

        r = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "BarryAI/6.8"
            }
        )

        data = r.json()

        return float(
            data["bitcoin"]["usd"]
        )


    except:

        return None



def calculate():

    # временные значения
    # позже заменим на реальные свечи

    ma20 = 65830.00
    ma50 = 65105.00
    rsi_value = 78.0
    adx_value = 2.5


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

    if "тех анализ" not in text.lower() and "анализ btc" not in text.lower():

        return None


    price = get_price()


    if price is None:

        return "❌ Нет данных BTC"



    trend, ma20, ma50, rsi_value, adx_value = calculate()



    decision = decision_engine.analyze(
        trend,
        rsi_value,
        adx_value
    )



    return (

        "📊 Barry Technical Analysis\n\n"

        "Инструмент: BTCUSDT\n"

        f"Цена: ${price:.2f}\n\n"

        f"Тренд: 🟢 {trend}\n\n"

        f"MA20: {ma20:.2f}\n"
        f"MA50: {ma50:.2f}\n"
        f"RSI: {rsi_value:.1f}\n"
        f"ADX: {adx_value:.1f}\n\n"

        "🧠 Решение Barry:\n"

        f"{decision}"

    )

import requests


def get_price(pair):

    try:

        url = "https://open.er-api.com/v6/latest/USD"

        r = requests.get(
            url,
            timeout=5
        )

        data = r.json()

        rates = data["rates"]


        if pair == "AUDNZD":
            return rates["NZD"] / rates["AUD"]

        if pair == "EURUSD":
            return 1 / rates["EUR"]

        if pair == "GBPUSD":
            return 1 / rates["GBP"]


        return None


    except:

        return None



def run(text):

    text = text.lower()


    pair = None


    if "audnzd" in text or "aud/nzd" in text:
        pair = "AUDNZD"

    elif "eurusd" in text or "eur/usd" in text:
        pair = "EURUSD"

    elif "gbpusd" in text or "gbp/usd" in text:
        pair = "GBPUSD"


    if pair is None:
        return None


    price = get_price(pair)


    if price is None:
        return "❌ Нет данных Forex"


    return (
        "📊 Barry Forex Analysis\n\n"
        f"💱 Пара: {pair}\n"
        f"Цена: {price:.5f}\n\n"
        "⚙️ Следующий этап:\n"
        "MA / RSI / ADX анализ Forex"
    )

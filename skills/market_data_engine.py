import requests
from datetime import datetime


SUPPORTED = [
    "EURUSD",
    "GBPUSD",
    "AUDUSD",
    "AUDNZD"
]


def get_price(pair):

    try:

        url = (
            "https://open.er-api.com/v6/latest/USD"
        )

        response = requests.get(
            url,
            timeout=5
        )

        data = response.json()

        rates = data["rates"]


        if pair == "EURUSD":
            return 1 / rates["EUR"]

        if pair == "GBPUSD":
            return 1 / rates["GBP"]

        if pair == "AUDUSD":
            return 1 / rates["AUD"]

        if pair == "AUDNZD":
            return rates["NZD"] / rates["AUD"]


        return None


    except:

        return None



def get_market(pair):

    price = get_price(pair)


    if price is None:
        return None


    return {

        "pair": pair,
        "price": price,
        "time": datetime.now().strftime(
            "%d.%m.%Y %H:%M:%S"
        )

    }



def run(text):

    text = text.upper()


    for pair in SUPPORTED:

        if pair in text:

            data = get_market(pair)


            if not data:
                return "❌ Нет данных рынка"


            return (
                "🌍 Barry Market Engine\n\n"
                f"Пара: {data['pair']}\n"
                f"Цена: {data['price']:.5f}\n"
                f"Время: {data['time']}"
            )


    return None

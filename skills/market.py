import requests


def get_bitcoin_price():

    url = (
        "https://api.coingecko.com/api/v3/"
        "simple/price"
        "?ids=bitcoin&vs_currencies=usd"
    )

    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "BarryAI/5.9"
        }
    )

    data = response.json()

    return data["bitcoin"]["usd"]



def run(text):

    low = text.lower().strip()


    if low not in [
        "цена bitcoin",
        "цена биткоина",
        "рынок"
    ]:
        return None


    try:

        price = get_bitcoin_price()


        return (
            "📈 Рынок Barry\n\n"
            f"₿ Bitcoin:\n"
            f"${price} USD\n\n"
            "Источник: CoinGecko"
        )


    except Exception as e:

        return (
            "❌ Ошибка рынка:\n"
            f"{e}"
        )

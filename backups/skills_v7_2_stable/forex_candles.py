import requests


def get_candles(pair):

    try:

        url = (
            "https://api.frankfurter.app/"
            "latest"
        )

        if pair == "AUDNZD":

            r = requests.get(
                url,
                params={
                    "from": "AUD",
                    "to": "NZD"
                },
                timeout=5
            )

        elif pair == "EURUSD":

            r = requests.get(
                url,
                params={
                    "from": "EUR",
                    "to": "USD"
                },
                timeout=5
            )

        else:
            return None


        data = r.json()

        return data["rates"]


    except:

        return None



def run(pair):

    data = get_candles(pair)


    if not data:
        return "❌ Нет данных Forex"


    return (
        "💱 Barry Forex Data\n\n"
        f"Пара: {pair}\n"
        f"Котировка: {data}\n\n"
        "⚙️ Следующий этап: свечи + индикаторы"
    )

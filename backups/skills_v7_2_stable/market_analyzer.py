import requests


SUPPORTED = [
    "btc",
    "bitcoin",
    "eur/usd",
    "aud/nzd",
    "gbp/usd",
    "usd/jpy"
]


def detect_asset(text):

    low = text.lower()

    for asset in SUPPORTED:
        if asset in low:
            return asset

    return None



def get_price(asset):

    # пока подключаем BTC
    if asset in ["btc", "bitcoin"]:

        try:
            url = (
                "https://api.coingecko.com/api/v3/"
                "simple/price"
                "?ids=bitcoin&vs_currencies=usd"
            )

            r = requests.get(
                url,
                timeout=10
            )

            data = r.json()

            return f"${data['bitcoin']['usd']}"

        except:
            return "нет данных"


    return "источник пока не подключён"



def run(text):

    if "анализ" not in text.lower():
        return None


    asset = detect_asset(text)


    if not asset:
        return None


    price = get_price(asset)


    return (
        "📊 Barry Market Analyzer\n\n"
        f"Инструмент: {asset.upper()}\n"
        f"Цена: {price}\n\n"
        "Следующий этап:\n"
        "MA / RSI / ADX анализ"
    )

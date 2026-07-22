import requests


SUPPORTED = [
    "EURUSD",
    "GBPUSD",
    "AUDUSD",
    "AUDNZD"
]


def get_rate(pair):
    try:
        url = (
            "https://open.er-api.com/v6/latest/USD"
        )

        r = requests.get(
            url,
            timeout=5
        )

        data = r.json()
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


def run(pair):

    pair = pair.upper().strip()

    # пропускаем чужие команды
    if pair not in SUPPORTED:
        return None

    price = get_rate(pair)

    if price is None:
        return "❌ Нет данных Forex"

    return (
        "💱 Barry Forex Market\n\n"
        f"Пара: {pair}\n"
        f"Цена: {price:.5f}"
    )

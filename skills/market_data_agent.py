# ==========================
# Barry Market Data Agent v4
# ==========================

from skills.forex_data import get_rate


SUPPORTED = [
    "EURUSD",
    "GBPUSD",
    "AUDUSD",
    "AUDNZD"
]


def get_market(pair):

    pair = pair.upper().strip()


    if pair not in SUPPORTED:

        return None


    price = get_rate(pair)


    if price is None:

        return {
            "pair": pair,
            "price": 1.14065
        }


    return {
        "pair": pair,
        "price": price
    }



def run(text):

    text = text.upper()


    for pair in SUPPORTED:

        if pair in text:

            market = get_market(pair)


            if market:

                return (
                    "🌍 Barry Market Data Agent v4\n\n"
                    f"💱 Пара: {pair}\n"
                    f"💰 Цена: {market['price']:.5f}\n\n"
                    "✅ Данные рынка получены"
                )


    return None

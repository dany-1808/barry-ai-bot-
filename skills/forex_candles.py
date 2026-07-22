# ==========================
# Barry Forex Candles v3.0
# ==========================

from datetime import datetime
from skills.forex_data import get_rate


SUPPORTED = [
    "EURUSD",
    "GBPUSD",
    "AUDUSD",
    "AUDNZD"
]


def get_candles(pair):

    pair = pair.upper().strip()


    if pair not in SUPPORTED:

        return None


    price = get_rate(pair)


    if price is None:

        return None



    candles = []


    # генерация рабочих свечей
    # позже заменим на API историю

    for i in range(60):

        if i < 40:

            open_price = price

            close_price = price

        else:

            open_price = price * 0.9995

            close_price = price * 1.0005


        high = max(
            open_price,
            close_price
        ) * 1.0005


        low = min(
            open_price,
            close_price
        ) * 0.9995


        candles.append(

            {
                "open": open_price,
                "high": high,
                "low": low,
                "close": close_price,
                "time": datetime.now().strftime(
                    "%d.%m.%Y %H:%M"
                )
            }

        )


    return candles



def run(pair):

    candles = get_candles(pair)


    if not candles:

        return "❌ Нет данных свечей"


    return (

        "💱 Barry Forex Candles v3\n\n"

        f"Пара: {pair}\n"

        f"Свечей: {len(candles)}\n"

        f"Цена: {candles[-1]['close']:.5f}"

    )

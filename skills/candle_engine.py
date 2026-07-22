import requests


def get_candles(symbol):

    try:

        if symbol != "BTCUSDT":
            return []


        # CoinGecko market chart
        url = (
            "https://api.coingecko.com/api/v3/"
            "coins/bitcoin/market_chart"
        )


        params = {
            "vs_currency": "usd",
            "days": "7",
            "interval": "hourly"
        }


        r = requests.get(
            url,
            params=params,
            timeout=10,
            headers={
                "User-Agent": "BarryAI/7.0"
            }
        )


        data = r.json()


        prices = data.get(
            "prices",
            []
        )


        closes = []


        for item in prices:

            closes.append(
                float(item[1])
            )


        return closes[-100:]


    except Exception as e:

        print(
            "CANDLE ERROR:",
            e
        )

        return []

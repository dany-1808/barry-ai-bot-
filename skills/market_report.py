import requests
import os


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
                "User-Agent": "BarryAI/6.0"
            }
        )

        data = r.json()

        return data["bitcoin"]["usd"]

    except:
        return None



def get_news():

    try:

        url = "https://news.google.com/rss/search"

        params = {
            "q": "Bitcoin",
            "hl": "ru",
            "gl": "RU",
            "ceid": "RU:ru"
        }


        r = requests.get(
            url,
            params=params,
            timeout=10
        )


        text = r.text


        count = text.count("<item>")


        return count


    except:

        return 0



def get_trade_stats():

    file = "data/trades.txt"


    if not os.path.exists(file):
        return "Нет данных"


    with open(file, "r", encoding="utf-8") as f:
        trades = [
            x.strip()
            for x in f
            if x.strip()
        ]


    wins = len([
        x for x in trades
        if "+"
        in x
    ])


    losses = len([
        x for x in trades
        if "-"
        in x
    ])


    total = wins + losses


    if total == 0:
        return "Нет сделок"


    winrate = wins / total * 100


    return f"WinRate {winrate:.1f}%"



def run(text):

    if text.lower().strip() != "анализ btc":
        return None


    price = get_price()

    news = get_news()

    stats = get_trade_stats()


    return (
        "📊 Barry BTC Analysis\n\n"

        f"₿ Цена Bitcoin:\n"
        f"${price}\n\n"

        f"📰 Новостей найдено:\n"
        f"{news}\n\n"

        f"📈 Статистика:\n"
        f"{stats}\n\n"

        "🧠 Анализ готов."
    )

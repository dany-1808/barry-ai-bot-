# ==========================
# Barry Pattern Agent v2.0
# Candle Pattern Recognition
# ==========================


def analyze(candles):

    if not candles or len(candles) < 3:

        return {
            "signal": "WAIT",
            "pattern": "Недостаточно свечей"
        }



    c1 = candles[-3]
    c2 = candles[-2]
    c3 = candles[-1]



    # три бычьи свечи подряд

    if (
        c1["close"] > c1["open"]
        and
        c2["close"] > c2["open"]
        and
        c3["close"] > c3["open"]
    ):

        return {
            "signal": "BUY",
            "pattern": "Три бычьи свечи"
        }



    # три медвежьи свечи подряд

    if (
        c1["close"] < c1["open"]
        and
        c2["close"] < c2["open"]
        and
        c3["close"] < c3["open"]
    ):

        return {
            "signal": "SELL",
            "pattern": "Три медвежьи свечи"
        }



    # бычье поглощение

    if (
        c2["close"] < c2["open"]
        and
        c3["close"] > c3["open"]
        and
        c3["close"] > c2["open"]
        and
        c3["open"] < c2["close"]
    ):

        return {
            "signal": "BUY",
            "pattern": "Бычье поглощение"
        }



    # медвежье поглощение

    if (
        c2["close"] > c2["open"]
        and
        c3["close"] < c3["open"]
        and
        c3["open"] > c2["close"]
        and
        c3["close"] < c2["open"]
    ):

        return {
            "signal": "SELL",
            "pattern": "Медвежье поглощение"
        }



    # обычная свеча

    if c3["close"] > c3["open"]:

        return {
            "signal": "BUY",
            "pattern": "Бычья свеча"
        }



    elif c3["close"] < c3["open"]:

        return {
            "signal": "SELL",
            "pattern": "Медвежья свеча"
        }



    return {
        "signal": "WAIT",
        "pattern": "Нет сигнала"
    }



def run(text):

    return None

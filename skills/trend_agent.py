# ==========================
# Barry Trend Agent v2.0
# EMA Trend Detection
# ==========================


def analyze(ema7, ema21):


    if ema7 > ema21:

        return {
            "trend": "Вверх",
            "signal": "BUY",
            "strength": 25
        }



    elif ema7 < ema21:

        return {
            "trend": "Вниз",
            "signal": "SELL",
            "strength": 25
        }



    else:

        return {
            "trend": "Флэт",
            "signal": "WAIT",
            "strength": 0
        }



def run(text):

    return None

# ==========================
# Barry Risk Agent v2.0
# Trade Safety Filter
# ==========================


def analyze(decision, score, rsi):


    warnings = []



    if rsi > 70:

        warnings.append(
            "RSI перегрет"
        )


    if rsi < 30:

        warnings.append(
            "RSI перепроданность"
        )



    if score < 60:

        warnings.append(
            "Низкое качество сигнала"
        )



    if decision == "WAIT":

        warnings.append(
            "Вход запрещён"
        )



    if len(warnings) == 0:

        status = "✅ Сигнал высокого качества"


    else:

        status = "⚠ Требуется осторожность"



    return {

        "status": status,

        "warnings": warnings

    }



def run(text):

    return None

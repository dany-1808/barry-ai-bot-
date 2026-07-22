from skills import technical_analysis
from skills import forex_technical


def run(text):

    text = text.lower()


    # крипто
    if "btc" in text or "bitcoin" in text:

        return technical_analysis.run(
            "тех анализ BTC"
        )


    # форекс
    if "audnzd" in text or "aud/nzd" in text:

        return forex_technical.run(
            "анализ AUDNZD"
        )


    if "eurusd" in text or "eur/usd" in text:

        return forex_technical.run(
            "анализ EURUSD"
        )


    return (
        "🧠 Barry Market Brain\n\n"
        "Инструмент не распознан."
    )

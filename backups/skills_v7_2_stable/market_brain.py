from skills import technical_analysis
from skills import forex_technical
from skills import decision_memory


def save_result(name, result):

    decision_memory.save_decision(
        name,
        result
    )


def run(text):

    text_lower = text.lower()


    # не забираем команды памяти
    if "запомни" in text_lower:
        return None

    if "история решений" in text_lower:
        return None


    # BTC

    if "btc" in text_lower or "bitcoin" in text_lower:

        result = technical_analysis.run(
            "тех анализ BTC"
        )

        if result:

            save_result(
                "BTCUSDT",
                result
            )


        return result



    # AUDNZD

    if "audnzd" in text_lower or "aud/nzd" in text_lower:

        result = forex_technical.run(
            "анализ AUDNZD"
        )

        if result:

            save_result(
                "AUDNZD",
                result
            )


        return result



    # EURUSD

    if "eurusd" in text_lower or "eur/usd" in text_lower:

        result = forex_technical.run(
            "анализ EURUSD"
        )

        if result:

            save_result(
                "EURUSD",
                result
            )


        return result



    return None

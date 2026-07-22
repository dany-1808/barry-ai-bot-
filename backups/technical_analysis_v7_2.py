from skills import candle_engine
from skills import indicator_engine
from skills import decision_engine
from skills import decision_memory


def run(text):

    text_lower = text.lower()

    if (
        "тех анализ" not in text_lower
        and "анализ btc" not in text_lower
    ):
        return None


    candles = candle_engine.get_candles(
        "BTCUSDT"
    )


    if not candles:

        return "❌ Нет данных BTC"


    data = indicator_engine.calculate(
        candles
    )


    ma20 = data["MA20"]
    ma50 = data["MA50"]
    rsi_value = data["RSI"]
    trend = data["Trend"]


    # временно, пока не подключили настоящий ADX
    adx_value = 2.5


    decision = decision_engine.analyze(
        trend,
        rsi_value,
        adx_value,
        ma20,
        ma50
    )


    result = (

        "📊 Barry Technical Analysis\n\n"

        "Инструмент: BTCUSDT\n"

        f"Цена: ${candles[-1]:.2f}\n\n"

        f"Тренд: 🟢 {trend}\n\n"

        f"MA20: {ma20:.2f}\n"

        f"MA50: {ma50:.2f}\n"

        f"RSI: {rsi_value:.1f}\n"

        f"ADX: {adx_value:.1f}\n\n"

        "🧠 Решение Barry:\n"

        f"{decision}"

    )


    try:

        decision_memory.save_decision(
            "BTCUSDT",
            result
        )

    except Exception:

        pass


    return result

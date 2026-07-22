from skills import candle_engine
from skills import indicator_engine
from skills import decision_engine
from skills.decision_tracker import save_decision
from skills.confidence_engine import calculate


def run(text):

    text_lower = text.lower()

    if (
        "тех анализ" not in text_lower
        and "анализ btc" not in text_lower
        and "технический анализ" not in text_lower
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

    adx_value = data.get(
        "ADX",
        2.5
    )


    confidence = calculate(
        trend,
        rsi_value,
        adx_value,
        ma20,
        ma50
    )


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
        f"Тренд: {trend}\n"
        f"MA20: {ma20:.2f}\n"
        f"MA50: {ma50:.2f}\n"
        f"RSI: {rsi_value:.1f}\n"
        f"ADX: {adx_value:.1f}\n\n"

        "🧠 Уверенность Barry:\n"
        f"{confidence['confidence']}%\n\n"

        + "\n".join(confidence["reasons"])

        + "\n\n🧠 Решение Barry:\n"
        + decision
    )


    # сохраняем опыт Barry
    try:
        save_decision(
            instrument="BTCUSDT",
            price=candles[-1],
            decision=decision,
            confidence=confidence["confidence"]
        )
    except Exception as e:
        print(
            "Ошибка записи решения:",
            e
        )


    return result

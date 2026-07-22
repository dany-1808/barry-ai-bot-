def run(text):
    text = text.lower().strip()

    if not text.startswith("риск"):
        return None

    try:
        parts = text.split()

        deposit = float(parts[1])
        percent = float(parts[2])

        risk = deposit * percent / 100

        daily = risk * 3
        target = risk * 2

        return (
            f"💰 Депозит: {deposit:.2f}\n"
            f"⚠ Риск на сделку: {percent:.1f}%\n"
            f"📉 Максимальный убыток: {risk:.2f}\n"
            f"🎯 Цель прибыли (1:2): {target:.2f}\n"
            f"🛑 Дневной лимит убытка: {daily:.2f}"
        )

    except:
        return "Пример: риск 1000 2"

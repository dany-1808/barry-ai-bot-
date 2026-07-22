import os
import re


FILE = "data/decisions.txt"


def run(text):

    if text.lower().strip() != "статистика решений":
        return None


    if not os.path.exists(FILE):
        return "📊 История решений пуста."


    with open(FILE, "r", encoding="utf-8") as f:
        data = f.read()


    total = data.count("Инструмент:")

    watch = data.count("наблюдать")

    wait = data.count("ждать откат")

    strong_wait = data.count("ждать сильный откат")


    confidence = re.findall(
        r"Уверенность Barry: (\d+)",
        data
    )


    avg = 0

    if confidence:
        nums = [
            int(x)
            for x in confidence
        ]

        avg = sum(nums) / len(nums)


    return (
        "📊 Barry Decision Statistics\n\n"
        f"Всего решений: {total}\n\n"
        f"👀 Наблюдать: {watch}\n"
        f"⏳ Ждать откат: {wait}\n"
        f"🔻 Ждать сильный откат: {strong_wait}\n\n"
        f"🧠 Средняя уверенность Barry: {avg:.1f}%"
    )

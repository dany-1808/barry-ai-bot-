PRODUCTS = {
    "яблоко": 52,
    "банан": 89,
    "курица": 165,
    "рис": 130,
    "яйцо": 155,
    "хлеб": 265
}


def run(text):

    low = text.lower()


    if "калории" not in low:
        return None


    for product, kcal in PRODUCTS.items():

        if product in low:

            parts = low.split()

            for part in parts:

                try:
                    grams = float(part)

                    result = kcal * grams / 100

                    return (
                        f"🍎 Продукт: {product}\n"
                        f"⚖ Вес: {grams} г\n"
                        f"🔥 Калории: {result:.0f} ккал"
                    )

                except:
                    pass


    return (
        "Пример:\n"
        "калории яблоко 200\n\n"
        "Продукты: яблоко, банан, курица, рис, яйцо, хлеб"
    )

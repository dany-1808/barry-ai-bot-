from difflib import get_close_matches


class Thinking:

    def analyze(self, text):

        text = text.lower().strip()


        intents = {

            "system": [
                "статус barry",
                "покажи журнал",
                "журнал",
                "анализ barry",
                "самоанализ",
                "проверка barry",
                "развитие barry",
                "покажи развитие",
                "отчёт развития",
                "отчет развития"
            ],


            "trading": [
                "рынок",
                "трейдинг",
                "торговля",
                "сделка",
                "риск"
            ],


            "memory": [
                "запомни",
                "кто я",
                "что ты помнишь"
            ],


            "chat": [
                "привет",
                "как дела",
                "кто ты"
            ]

        }


        # обычный поиск

        for intent, words in intents.items():

            for word in words:

                if word in text:
                    return intent


        # поиск похожей команды
        all_words = []

        for words in intents.values():
            all_words.extend(words)


        match = get_close_matches(
            text,
            all_words,
            n=1,
            cutoff=0.75
        )


        if match:

            for intent, words in intents.items():

                if match[0] in words:
                    return intent


        return "unknown"



thinking = Thinking()

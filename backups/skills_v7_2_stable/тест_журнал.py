
def run(text):
    if text.lower() == "провести тест":
        return "Тест успешно проведен!"
    elif text.lower() == "посмотреть журнал":
        return "Журнал тестов открыт."
    elif text.lower() == "удалить журнал":
        return "Журнал тестов удален."
    else:
        return None

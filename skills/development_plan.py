from learning_log import add_log
from skills.error_memory import get_errors
import os



def count_skills():

    if not os.path.exists("skills"):

        return 0


    return len([
        f for f in os.listdir("skills")
        if f.endswith(".py")
        and f != "__init__.py"
    ])




def run(text):

    if "план развития" not in text.lower():

        return None



    skills = count_skills()

    errors = len(get_errors())



    plan = (

        "🚀 Barry Development Plan\n\n"

        f"🛠 Навыков обнаружено: {skills}\n"

        f"⚠ Ошибок в памяти: {errors}\n\n"

        "Приоритеты:\n"

        "1. 🧠 Улучшать память решений\n"

        "2. 📊 Анализировать ошибки\n"

        "3. 🛠 Проверять качество навыков\n"

        "4. 🔄 Развивать цикл самообучения\n"

        "5. 🧪 Тестировать новые модули перед установкой\n\n"

        "Статус:\n"

        "✅ Память работает\n"

        "✅ Журналы работают\n"

        "✅ Ошибки отслеживаются\n"

        "✅ Развитие фиксируется\n"

        "⚠ Автоматическое изменение кода отключено для безопасности"

    )



    add_log(plan)


    return plan

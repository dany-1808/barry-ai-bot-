from action_log import add_action
from skill_manager import skill_manager
from task_memory import save_context, get_context
from skills.development_memory import save_development


class Executor:


    def execute(self, steps):

        result = []

        for step in steps:

            print(
                f"⚙ Выполняю: {step}"
            )

            add_action(
                f"Выполнение шага: {step}"
            )


            answer = self.run_step(step)


            save_context(
                step,
                answer
            )


            result.append(
                f"✅ {step}\n{answer}"
            )


            add_action(
                f"Шаг завершён: {step}"
            )


        final_result = "\n\n".join(result)


        if "развит" in str(steps).lower():

            save_development(
                final_result
            )


        add_action(
            "Задача полностью выполнена"
        )


        return final_result



    def run_step(self, step):

        text = step.lower()



        if "состояние системы" in text:

            return skill_manager.run(
                "анализ barry"
            )



        if "слабые места" in text:

            return skill_manager.run(
                "развивайся"
            )



        if "эффективность навыков" in text:

            return skill_manager.run(
                "эффективность навыков"
            )



        if "приоритет" in text:

            return skill_manager.run(
                "приоритет развития"
            )



        if "совет развития" in text:

            return skill_manager.run(
                "совет развития"
            )



        if "план изменения" in text:

            return skill_manager.run(
                "план развития"
            )



        if "сохранить результат" in text:

            return (
                "💾 Результат развития сохранён "
                "в Development Memory"
            )



        if "рынок" in text:

            return skill_manager.run(
                "анализ BTC"
            )



        if "индикатор" in text:

            previous = get_context(
                "Проверить рынок"
            )

            if previous:

                return (
                    "📌 Данные из памяти:\n\n"
                    + previous
                )

            return skill_manager.run(
                "анализ BTC"
            )



        if "риск" in text:

            return skill_manager.run(
                "анализ решений"
            )



        return ask_ai(
            f"Выполни шаг задачи Barry: {step}"
        )



executor = Executor()

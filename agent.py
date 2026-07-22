from thinking import thinking
from planner import planner
from executor import executor
from brain import think
from action_log import add_action


class Agent:


    def execute(self, command):

        intent = thinking.analyze(command)


        add_action(
            f"Команда: {command} | Намерение: {intent}"
        )


        print(
            f"🧠 Намерение: {intent}"
        )


        # =====================
        # Выполнение задач
        # =====================

        if command.lower().startswith("сделай "):

            task = command[7:].strip()


            add_action(
                f"Создание плана задачи: {task}"
            )


            steps = planner.make_plan(task)


            result = executor.execute(
                steps
            )


            add_action(
                "Задача выполнена через executor"
            )


            return result



        # =====================
        # Торговый режим
        # =====================

        if intent == "trading":

            add_action(
                "Запуск торгового режима"
            )


            result = think(
                "начинаем торговлю"
            )


            add_action(
                "Торговый ответ сформирован"
            )


            return result



        # =====================
        # Остальные команды
        # =====================

        result = think(
            command
        )


        add_action(
            "Ответ сформирован"
        )


        return result



agent = Agent()

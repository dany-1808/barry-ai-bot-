from thinking import thinking
from planner import planner
from executor import executor
from brain import think
from action_log import add_action


class Agent:

    def execute(self, command):

        intent = thinking.analyze(command)

        print(f"🧠 Намерение: {intent}")


        # записываем действие в журнал
        add_action(
            f"Команда: {command} | Намерение: {intent}"
        )


        # Выполнение задач через планировщик

        if command.lower().startswith("сделай "):

            task = command[7:]

            add_action(
                f"Создание плана задачи: {task}"
            )

            steps = planner.make_plan(task)

            result = executor.execute(steps)

            add_action(
                "Задача выполнена через executor"
            )

            return result



        # Торговый режим

        if intent == "trading":

            add_action(
                "Запуск торгового режима"
            )

            return think("начинаем торговлю")



        # Остальные команды

        result = think(command)


        add_action(
            "Ответ сформирован"
        )


        return result



agent = Agent()

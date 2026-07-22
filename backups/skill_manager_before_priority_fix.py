import os
import importlib


class SkillManager:

    def __init__(self):
        self.skills = []


    def load(self):

        self.skills.clear()


        if not os.path.exists("skills"):
            return


        priority = [

            # память и управление сначала
            "skills.decision_memory",

            # рынок после
            "skills.market_brain",

            "skills.info",
            "skills.self_improve",
            "skills.goals_manager",
            "skills.analyze_barry",
            "skills.status",
            "skills.development",
            "skills.development_report",
            "skills.updates",
            "skills.journal_view"
        ]


        loaded = {}


        for file in os.listdir("skills"):

            if not file.endswith(".py"):
                continue


            if file == "__init__.py":
                continue


            name = f"skills.{file[:-3]}"


            try:

                module = importlib.import_module(name)

                importlib.reload(module)

                loaded[name] = module


            except Exception as e:

                print(
                    "❌ Ошибка загрузки:",
                    name,
                    e
                )


        # строгий порядок
        for name in priority:

            if name in loaded:

                self.skills.append(
                    loaded[name]
                )


        # остальные навыки
        for name, module in loaded.items():

            if name not in priority:

                self.skills.append(module)



    def run(self, text):

        for skill in self.skills:

            try:

                answer = skill.run(text)

                if answer:

                    return answer


            except Exception as e:

                print(
                    "❌ Ошибка в навыке:",
                    skill.__name__,
                    e
                )


        return None



skill_manager = SkillManager()
skill_manager.load()

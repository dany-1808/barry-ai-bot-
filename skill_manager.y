# ==========================
# Barry Skill Manager v7.0
# Priority Trader First
# ==========================

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

            # =====================
            # TRADING FIRST
            # =====================

            "skills.trader_agent",
            "skills.decision_engine",
            "skills.risk_agent",
            "skills.pattern_agent",
            "skills.trend_agent",


            # =====================
            # MARKET DATA
            # =====================

            "skills.market_data_agent",
            "skills.forex_data",
            "skills.forex_candles",


            # =====================
            # INDICATORS
            # =====================

            "skills.indicator_engine",



            # =====================
            # MEMORY
            # =====================

            "skills.decision_memory",
            "skills.decision_tracker",
            "skills.decision_stats",



            # =====================
            # SYSTEM
            # =====================

            "skills.barry_status",
            "skills.status",
            "skills.system_check"

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



        # сначала важные

        for name in priority:


            if name in loaded:

                self.skills.append(
                    loaded[name]
                )



        # остальные

        for name, module in loaded.items():


            if name not in priority:

                self.skills.append(
                    module
                )




    def run(self, text):


        for skill in self.skills:


            try:


                if not hasattr(skill, "run"):

                    continue



                answer = skill.run(text)



                if answer:

                    return answer



            except Exception as e:


                print(
                    "❌ Ошибка навыка:",
                    skill.__name__,
                    e
                )



        return None




skill_manager = SkillManager()

skill_manager.load()

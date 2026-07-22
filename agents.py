import os
import json
from datetime import datetime


FILE = "data/agents.json"


class AgentManager:

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(FILE):
            with open(FILE, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)


    def load(self):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)


    def save(self, data):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )


    def create_agent(
        self,
        name,
        role
    ):

        agents = self.load()

        agent = {
            "name": name,
            "role": role,
            "created": datetime.now().strftime(
                "%d.%m.%Y %H:%M"
            ),
            "status": "active",
            "experience": 0
        }

        agents.append(agent)

        self.save(agents)

        return agent


    def list_agents(self):

        agents = self.load()

        if not agents:
            return "🤖 Агентов нет."

        result = "🤖 Barry Agent Registry\n\n"

        for a in agents:

            result += (
                f"• {a['name']}\n"
                f"  Роль: {a['role']}\n"
                f"  Статус: {a['status']}\n"
                f"  Опыт: {a['experience']}\n\n"
            )

        return result



agent_manager = AgentManager()



def run(text):

    text = text.lower()


    if text.startswith("создай агента"):

        data = text.replace(
            "создай агента",
            ""
        ).strip()


        parts = data.split(",")


        if len(parts) < 2:
            return (
                "Формат:\n"
                "создай агента имя, роль\n\n"
                "Пример:\n"
                "создай агента trader, форекс трейдер"
            )


        agent = agent_manager.create_agent(
            parts[0].strip(),
            parts[1].strip()
        )


        return (
            "✅ Агент создан\n\n"
            f"Имя: {agent['name']}\n"
            f"Роль: {agent['role']}"
        )


    if text.strip() == "список агентов":

        return agent_manager.list_agents()


    return None

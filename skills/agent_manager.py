from agents import agent_manager


def run(text):

    text = text.lower().strip()

    if text.startswith("создай агента"):

        data = text.replace(
            "создай агента",
            ""
        ).strip()

        parts = data.split(",")

        if len(parts) < 2:
            return (
                "Формат:\n"
                "создай агента имя, роль"
            )

        agent = agent_manager.create_agent(
            parts[0].strip(),
            parts[1].strip()
        )

        return (
            "🤖 Barry Agent System\n\n"
            "✅ Агент создан\n\n"
            f"Имя: {agent['name']}\n"
            f"Роль: {agent['role']}"
        )


    if text == "список агентов":

        return agent_manager.list_agents()


    return None

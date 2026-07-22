class CommandRouter:

    def __init__(self):
        self.commands = {}

    def register(self, name, func):
        self.commands[name.lower()] = func

    def execute(self, text):

        text = text.lower().strip()

        for command in self.commands:

            if text.startswith(command):
                return self.commands[command](text)

        return None


router = CommandRouter()

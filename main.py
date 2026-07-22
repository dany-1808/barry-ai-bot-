from agent import agent
from chat_memory import save_chat
from config import BARRY_NAME, BARRY_VERSION


print("=" * 40)
print(f"🤖 {BARRY_NAME} v{BARRY_VERSION}")
print("=" * 40)


while True:

    try:

        user = input("\nТы: ")


        if user.lower() in ["выход", "exit", "quit"]:

            print("Barry AI: До встречи!")
            break


        answer = agent.execute(user)


        print("\nBarry AI:", answer)


        save_chat(user, answer)


    except KeyboardInterrupt:

        print("\nBarry AI: До встречи!")
        break


    except Exception as e:

        print("Ошибка:", e)

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, BARRY_NAME, BARRY_VERSION
from agent import agent


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🤖 {BARRY_NAME} v{BARRY_VERSION}\n\n"
        "Barry AI запущен.\n"
        "Напиши любое сообщение."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_text = update.message.text

        print(f"📩 {user_text}")

        answer = agent.execute(user_text)

        await update.message.reply_text(str(answer))

    except Exception as e:
        print(e)
        await update.message.reply_text(f"❌ Ошибка:\n{e}")


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("🤖 Barry Telegram Bot Online")

    app.run_polling()


if __name__ == "__main__":
    main()

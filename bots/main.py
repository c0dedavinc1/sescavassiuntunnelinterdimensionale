import logging
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, Updater, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao Protagonista")
    time.sleep(2.6)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="sono io, ti ricordi di me...?")


def message_handler(update, context):
    message = update.message
    print(message.text)


if __name__ == '__main__':
    application = ApplicationBuilder().token('8498664237:AAH9bIO2aUuZqj4RGiRCmI1PbIftHrGwpME').build()
    updater = Updater('8498664237:AAH9bIO2aUuZqj4RGiRCmI1PbIftHrGwpME')

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add a message handler that will be called for any message
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    # Start the bot
    updater.start_polling()
    application.run_polling()   
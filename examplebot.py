from telegram.ext import Updater, CommandHandler
import logging
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    chat_id = update.message.chat_id
    text = '`me gustan las batadases y las DATA ESTRUCTURAS`'
    bot.send_message(chat_id, text, parse_mode='Markdown')


def main():
    start_handler = CommandHandler("start", start)

    updater = Updater(sys.argv[1])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
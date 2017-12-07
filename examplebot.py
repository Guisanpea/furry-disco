from telegram.ext import Updater, CommandHandler
import logging
import sys
from much_good.bot_actions import BotActions


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    updater = Updater(sys.argv[1])
    dispatcher = updater.dispatcher

    add_handlers(dispatcher)

    updater.start_polling()
    updater.idle()


def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", BotActions.start))
    dispatcher.add_handler(CommandHandler("send_memiyos", BotActions.send_memiyos))


if __name__ == '__main__':
    main()

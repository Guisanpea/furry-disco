from telegram.ext import Updater, CommandHandler
import logging
import sys
from much_good.bot_actions import BotActions

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename="debug.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    updater = Updater(sys.argv[1])
    dispatcher = updater.dispatcher

    add_handlers(dispatcher)

    updater.start_polling()
    updater.idle()


def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", BotActions.start))
    dispatcher.add_handler(CommandHandler("send_memiyos", BotActions.send_memiyos))
    dispatcher.add_handler(CommandHandler("gcd", BotActions.gcd, pass_args=True))
    dispatcher.add_handler(CommandHandler("mcd", BotActions.gcd, pass_args=True))

    dispatcher.add_error_handler(error)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == '__main__':
    main()

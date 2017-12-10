from os import listdir

from os.path import isfile, join
from random import randint


class BotActions:

    @staticmethod
    def start(bot, update):
        chat_id = update.message.chat_id
        text = '`me gustan las batadases y las DATA ESTRUCTURAS`'
        bot.send_message(chat_id, text, parse_mode='Markdown')

    @staticmethod
    def send_memiyos(bot, update):
        chat_id = update.message.chat_id
        meme = open(BotActions.random_file_name('/home/archie/Images/memiyos'), 'rb')
        bot.send_photo(photo=meme, chat_id=chat_id)

    @staticmethod
    def random_file_name(path):
        files = [file for file in listdir(path) if isfile(join(path, file))]
        return join(path, files[randint(0, len(files)-1)])

    @staticmethod
    def gcd(bot, update, args):
        chat_id = update.message.chat_id
        a = args[0]
        b = args[1]
        bot.send_message(chat_id, compute_gcd(a, b))

    @staticmethod
    def compute_gcd(a, b):
        return a if b == 0 else mcd(a, a % b)

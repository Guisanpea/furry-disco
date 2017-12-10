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
        try:
            a = int(args[0])
            b = int(args[1])
            message = "El mcd de " + str(a) + " y " + str(b) + " es " + str(BotActions.compute_gcd(a, b))
            bot.send_message(chat_id, message)
        except Exception:
            bot.send_message(chat_id, "Illo, ya las liao")

    @staticmethod
    def compute_gcd(a, b):
        return a if b == 0 else BotActions.compute_gcd(a, a % b)

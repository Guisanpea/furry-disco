from much_good import helpers


def start(bot, update):
        chat_id = update.message.chat_id
        text = '`me gustan las batadases y las DATA ESTRUCTURAS`'
        bot.send_message(chat_id, text, parse_mode='Markdown')


def send_memiyos(bot, update):
        chat_id = update.message.chat_id
        meme = open(helpers.random_file_name('/home/archie/Images/memiyos'), 'rb')
        bot.send_photo(photo=meme, chat_id=chat_id)


def gcd(bot, update, args):
    chat_id = update.message.chat_id
    try:
        a = int(args[0])
        b = int(args[1])
        message = "El mcd de `" + str(a) +\
                  "` y `" + str(b) +\
                  "` es `" + str(helpers.compute_gcd(a, b)) + "`"
        bot.send_message(chat_id, message, parse_mode='Markdown')
    except Exception:
        bot.send_message(chat_id, "`Illo, ya las liao`", parse_mode='Markdown')


def show_help(bot, update):
    chat_id = update.message.chat_id

    with open('help.txt', 'r') as file:
        text = file.read()

    bot.send_message(chat_id, text, parse_mode='Markdown')

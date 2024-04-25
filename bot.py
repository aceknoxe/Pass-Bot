import random
import string
import telegram
from telegram.ext import Updater, CommandHandler

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    return password

def start(update, context):
    password = generate_password()
    update.message.reply_text(f"Your random password is: {password}")

updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()

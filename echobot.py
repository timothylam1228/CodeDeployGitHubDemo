
"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Dice, InlineQuery , ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('DLLM!')


def help_command(update, context):

    bot = telegram.Bot('1357264168:AAGkNtefPbg4mO-f7j4lxsrN1-sk_TaVVRw')
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = 123

    """Send a message when the command /help is issued."""
    reply_keyboard = [['First','Second']]

    update.message.reply_text(
        'Send nude first. '
        'Send /cancel to stop talking to me.\n\n'
        'Are you a boy or a girl?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


def echo(update, context):
    """Echo the user message."""
    temp = 0
    temp = random.randint(1, 2)
    # update.message.reply_text(update.message.text)
    if((update.message.text).lower()  == 'girl'):
        update.message.reply_text('Fake girl detected')
        #bot.send_audio(chat_id=chat_id, audio=open('tests/test.mp3', 'rb'))
    elif((update.message.text).lower() == 'boy'):
        update.message.reply_text('Gay not allow here sorry')
    elif((update.message.text).lower() == 'dllm'):
        if(temp == 1):
            update.message.reply_text('DLLM!')
        else:
            update.message.reply_text('你好!')
    
def newmember(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('歡迎來到N號房 ')
    
    


def main():
    global update_id

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1357264168:AAGkNtefPbg4mO-f7j4lxsrN1-sk_TaVVRw", use_context=True)
    global update_id

    # Get the dispatcher to register handlers
    dp = updater.dispatcher


    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
  
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newmember))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    
    main()

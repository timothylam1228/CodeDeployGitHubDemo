
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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import InlineQuery , ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity, ForceReply, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.utils import helpers

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
REQUEST, PHOTO, LOCATION, BIO = range(4)
CHECK_THIS_OUT = 'check-this-out'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('here is the source link :'+
        'https://connectpolyu-my.sharepoint.com/:f:/g/personal/18022038d_connect_polyu_hk/EoftV3mXfn9Em_HTMLRGWwkBIJHySPhJrKfn237Z5T3rtA?e=sggDys')


def help_command(update, context):

    """Send a message when the command /help is issued."""
    reply_keyboard = [['Source','Question']]
    update.message.reply_text(
        'What can i help u?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return REQUEST


def question(update, context):
    if(update.message.text)== 'Question':
        update.message.reply_text('No Question are allowed',reply_markup=ReplyKeyboardRemove())
    elif(update.message.text)== 'Source':
        update.message.reply_text('No Source ar dllm',reply_markup=ReplyKeyboardRemove())
    # if ((update.message.text).lower()  == 'Source'):
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text('Bye!',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

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
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    text = "歡迎來到IT谷" 
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Continue here!', url=url)
    )
    update.message.reply_text(text, reply_markup=keyboard)
    
def main():
    global update_id

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1357264168:AAF-SEACMXD6DM9dBqvUV0NFySXVb5isb5s", use_context=True)
 
    # Get the dispatcher to register handlers
    dp = updater.dispatcher


    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start,filters=~Filters.group))
    
    '''
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('help', help_command)],

        states={
            REQUEST: [MessageHandler(Filters.regex('^(Source|Question)$'), question)]
            
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    '''
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

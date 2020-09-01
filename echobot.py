
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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
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
TEMP = 0
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('/source for Geting the source')


def help_command(update, context):
    return 
    
   
def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="Selected option: {}".format(query.data))
    path="https://github.com/timothylam1228/telegram_bot/raw/master/source/"
    file=str(query.data)
    pdf=".pdf"
    context.bot.sendDocument(chat_id=query.message.chat.id, document=path+file+pdf)

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
    
    if((update.message.text).lower() == 'dllm'):
        #context.bot.delete_message(update.message.message_id,update.message)
        context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)
        global TEMP
        TEMP = TEMP + 1
        if(TEMP%5==0):
            context.bot.sendMessage(chat_id=update.message.chat.id,text =  str(update.message.from_user.first_name) + ' Dont say dllm plz, you speaked '+str(TEMP)+' times ' )

def source(update, context):
    keyboard = [[InlineKeyboardButton("CCT", callback_data='CCT'),
                 InlineKeyboardButton("Diagnostic Test", callback_data='Diagnostic Test')],

                [InlineKeyboardButton("Calculus review", callback_data='Calculus review')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    # file="source/CCT.pdf"
    # # send the pdf doc
    # bot.sendDocument(chat_id=update.message.chat.id, document=open(file, 'rb'))
      
    
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
    dp.add_handler(CommandHandler("help",help_command))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(CommandHandler("Source", source,filters=~Filters.group))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newmember))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    
    main()

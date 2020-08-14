from telegram.ext import Updater, CommandHandler


def hello(update, context):
    update.message.reply_text('{}'.format(update.message.text))


updater = Updater('YOUR_TOKEN', use_context=True)

updater.dispatcher.add_handler(CommandHandler('12_21', hello))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()


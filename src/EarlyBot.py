from telegram.ext import Updater, CommandHandler
from src.DeepSteffen.DeepSteffen import DeepSteffen


class EarlyBot:

    deep_steffen = DeepSteffen()

    def __init__(self, api_key: str):

        updater = Updater(api_key, use_context=True)
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("ds", self.generate))

        # on noncommand i.e message - echo the message on Telegram
        # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()

    def generate(self, update, context):

        temperature = None
        output = ""
        prefix = ""

        print(f"Args: {context.args}")

        for index, arg in enumerate(context.args):

            # Has the user passed a float as the first arg. If so - it's temperature!
            if index == 0 and '.' in arg and arg.replace('.', '', 1).isdigit():
                temperature = float(arg)
            elif index == 0:
                prefix += arg + " "

            # The rest of the args make up the beginning of the sentence.
            if index != 0:
                prefix += arg + " "

        prefix = prefix.strip()

        while not output:
            output = self.deep_steffen.generate(prefix, temperature)[0]

        print(f"Output: {output}")
        update.message.reply_text(output, quote=False)


if __name__ == "__main__":
    EarlyBot("")

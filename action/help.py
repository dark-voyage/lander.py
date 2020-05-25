from core import bot


def _help():
    @bot.message_handler(commands=['help'])
    def __help(message):
        _from = message.from_user.id
        bot.send_message(_from, "Help message activated")
        bot.register_next_step_handler()
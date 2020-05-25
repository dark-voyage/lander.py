from core import *


def _start():
    @bot.message_handler(commands=['start'])
    def __start(message):
        _from = message.from_user.id
        bot.send_message(_from, "Start command activated")
    pass

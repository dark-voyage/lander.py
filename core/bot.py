import telebot
import logging

from config import token

bot = telebot.AsyncTeleBot(token)
logger = telebot.logger


def launch():
    try:
        bot.polling(True)
        logger(logging.DEBUG)
    except ConnectionRefusedError:
        print("Error occurred while starting app...")
    pass

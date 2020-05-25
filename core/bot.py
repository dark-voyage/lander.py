import telebot
import logging

from config import token

bot = telebot.AsyncTeleBot(token)
logger = telebot.logger


def launch():
    bot.polling(True)
    logger.setLevel(logging.DEBUG)
    pass

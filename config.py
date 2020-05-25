# Some instances require some packages
# To initialize the project I used keys
# Environments - export usable variables
import os

# This is the token for Telegram Bot API
# Please be carefull while publishing your
# own Telegram Bot API. Others might use it
token = os.environ.get("BOT_TOKEN")

# This is the link of live database json file
# bot will download the file and proceed with
# operations given on bot's program.
url = os.environ.get("URL")

# Some instances require some packages
# To initialize the project I used keys
# Environments - export usable variables
import os

# This is the token for Telegram Bot API
# Please be carefull while publishing your
# own Telegram Bot API. Others might use it
token = os.environ.get("BOT_TOKEN") or "1281040995:AAHxeRiZsH2TQ3VLo0ZyZSC1sBS3RIwWYGs"

# This is the link of live database json file
# bot will download the file and proceed with
# operations given on bot's program.
url = os.environ.get("URL") or "https://raw.githubusercontent.com/denoland/deno_website2/master/database.json"

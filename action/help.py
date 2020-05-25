from telebot import types
from core import bot


def _help():
    @bot.message_handler(commands=['help'])
    def __help(message):
        _from = message.from_user.id
        buttons = [
            types.InlineKeyboardButton(
                text="Website",
                url="https://deno.land/"
            ),
            types.InlineKeyboardButton(
                text="Documentation",
                url="https://doc.deno.land/"
            ),
            types.InlineKeyboardButton(
                text="Start searching packages",
                switch_inline_query_current_chat=""
            )
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=len(buttons))
        for button in buttons:
            keyboard.add(button)
        helper = \
            f"<b>This is the available command list:</b> \n" \
            f"/help - to show this menu \n" \
            f"\n" \
            f"<i>In order to use package search engine, press 'start searching packages' button below...</i>"

        bot.send_message(_from, helper, reply_markup=keyboard, parse_mode="HTML")

from difflib import get_close_matches
from telebot import types
from core import *


def _inline():
    @bot.inline_handler(func=lambda query: True)
    def __inline(query):
        similarities = get_close_matches(query.query, dataset_keys())
        poster = 1
        results = []
        for key in similarities:
            data = dataset(key)
            name = key
            repo = data.get("repo")
            desc = data.get("desc")
            auth = data.get("owner")
            host = data.get("type")
            deno = f"https://deno.land/x/{name}"
            github = f"https://github.com/{auth}/{repo}"

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            github_keyboard = types.InlineKeyboardButton(
                text="GitHub",
                url=github
            )
            package_keyboard = types.InlineKeyboardButton(
                text="Deno",
                url=deno
            )
            browse = types.InlineKeyboardButton(
                text="Packages",
                url="https://deno.land/x/"
            )
            keyboard.add(github_keyboard, package_keyboard, browse)

            module = types.InlineQueryResultArticle(
                id=++poster,
                title=name,
                description=desc,
                url=deno,
                input_message_content=types.InputTextMessageContent(
                    message_text=f"<b>Deno:</b> Third Party Module 📦\n\n"
                                 f"<b>Name:</b> {repo}\n"
                                 f"<b>Host:</b> {host}\n"
                                 f"<b>Description:</b> {desc}\n",
                    parse_mode="HTML",
                ),
                reply_markup=keyboard
            )
            poster += 1
            results.append(module)
        bot.answer_inline_query(query.id, results, cache_time=10)
        del results[:]
        poster = 1

    pass

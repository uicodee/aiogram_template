from aiogram import types

from tgbot.callback_data.callback_datas import cb_language
from tgbot.data.data import languages


def language_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for language_code, language_name in languages.items():
        keyboard.insert(
            types.InlineKeyboardButton(
                text=language_name,
                callback_data=cb_language.new(language_code=language_code)
            )
        )
    return keyboard

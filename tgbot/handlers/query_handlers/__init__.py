from aiogram import Dispatcher

from .language_handler import language_handler

from tgbot.callback_data.callback_datas import cb_language


def register_query_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(language_handler, cb_language.filter(), state="*")

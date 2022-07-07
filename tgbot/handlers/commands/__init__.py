from aiogram import Dispatcher

from .start import cmd_start


def register_commands(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands=["start"], state="*")

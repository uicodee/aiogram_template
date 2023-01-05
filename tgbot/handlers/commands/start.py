from aiogram import types

from tgbot.db.dao.holder import HolderDao


async def cmd_start(
        message: types.Message,
        dao: HolderDao
) -> None:
    await message.answer(text='Salom')


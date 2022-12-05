from aiogram import types
from tgbot.service.repo.repository import SQLAlchemyRepos


async def cmd_start(message: types.Message, repo: SQLAlchemyRepos) -> None:
    await message.answer(text='Salom')


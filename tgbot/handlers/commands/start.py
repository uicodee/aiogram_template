from aiogram import types
from tgbot.keyboards.inline.language import language_markup
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo
from tgbot.data.data import i18n

_ = i18n.gettext


async def cmd_start(message: types.Message, repo: SQLAlchemyRepos) -> None:
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=message.from_user.id) is None:
        await message.answer(
            text='Assalomu Alaykum! Kerakli tilni tanlang\n'
                 'Здравствуйте! Выберите необходимый язык',
            reply_markup=language_markup()
        )
    else:
        await message.answer(
            text=_('Asosiy menu')
        )


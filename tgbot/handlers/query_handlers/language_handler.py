from typing import Dict

from aiogram import types

from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo
from tgbot.data.data import i18n

_ = i18n.gettext


async def language_handler(query: types.CallbackQuery, callback_data: Dict[str, str], repo: SQLAlchemyRepos) -> None:
    language_code = callback_data.get('language_code')
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=query.from_user.id) is None:
        await user.add_user(
            user_id=query.from_user.id,
            name=query.from_user.full_name,
            language=language_code
        )
    else:
        await user.update_language(user_id=query.from_user.id, language=language_code)
    await query.message.edit_text(
        text=_('Asosiy menu')
    )

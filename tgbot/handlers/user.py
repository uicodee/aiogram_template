from aiogram import Dispatcher
from aiogram.types import Message
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.models.user import User


async def user_start(m: Message, session: AsyncSession):
    if (await session.execute(select(User).filter(User.user_id == m.from_user.id))).scalar() is None:
        await session.execute(insert(User).values(
            user_id=m.from_user.id,
            name=m.from_user.full_name,
            username=m.from_user.full_name
        ))
        await session.commit()
        await m.answer("Hello, you added to my Database!")
    else:
        await m.answer("Hello, you already in my Database!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

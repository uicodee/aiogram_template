from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.dao.rdb import BaseDAO
from tgbot.db.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user(
            self,
            user_id: int,
            name: str,
            username: str | None
    ):
        await self.session.execute(
            insert(User).values(
                user_id=user_id,
                name=name,
                username=username
            )
        )
        await self.session.commit()

    async def get_user(self, user_id: int) -> User:
        result = await self.session.execute(
            select(User).filter(
                User.user_id == user_id
            )
        )
        return result.scalar()

    async def get_all_users(self) -> list[User]:
        result = await self.session.execute(
            select(User)
        )
        return result.scalars().all()
    
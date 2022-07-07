from sqlalchemy import insert, select, update

from tgbot.models.user import User
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class UserRepo(BaseSQLAlchemyRepo):
    model = User

    async def add_user(self, user_id: int, name: str, language: str) -> None:
        sql = insert(self.model).values(user_id=user_id, name=name, language=language)
        await self._session.execute(sql)
        await self._session.commit()

    async def get_user(self, user_id: int) -> model | None:
        sql = select(self.model).where(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        user = request.scalar()
        return user

    async def get_language(self, user_id: int) -> model.language:
        sql = select(self.model.language).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def get_users(self) -> list[model]:
        sql = select(self.model)
        request = await self._session.execute(sql)
        user = request.scalars().all()
        return user

    async def update_status(self, user_id: int, subscribed: bool) -> None:
        sql = update(self.model).where(self.model.user_id == user_id).values({'subscribed': subscribed})
        await self._session.execute(sql)
        await self._session.commit()

    async def update_language(self, user_id: int, language: str) -> None:
        sql = update(self.model).where(self.model.user_id == user_id).values({'language': language})
        await self._session.execute(sql)
        await self._session.commit()

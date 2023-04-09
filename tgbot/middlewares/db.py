from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from sqlalchemy.orm import sessionmaker

from tgbot.db.dao.holder import HolderDao


class DbSessionMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, session_pool: sessionmaker):
        super().__init__()
        self.session_pool = session_pool

    async def pre_process(self, obj, data, *args):
        session = self.session_pool()
        dao: HolderDao = HolderDao(session=session)
        data['dao'] = dao

    async def post_process(self, obj, data, *args):
        session = data.get("session")
        if session:
            await session.close()
            del data["dao"]

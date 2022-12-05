from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker
from .db import DbSessionMiddleware


def register_middlewares(dp: Dispatcher, session_fabric: sessionmaker) -> None:
    dp.middleware.setup(DbSessionMiddleware(session_pool=session_fabric))

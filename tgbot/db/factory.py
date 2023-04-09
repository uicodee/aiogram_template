import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from tgbot.config import Config


logger = logging.getLogger(__name__)


def create_pool(config: Config) -> sessionmaker:
    url = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}?async_fallback=True".format(
        user=config.db.user,
        password=config.db.password,
        host=config.db.host,
        port=config.db.port,
        database=config.db.database
    )
    engine = create_async_engine(url=url, echo=False)
    pool = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False
    )
    return pool

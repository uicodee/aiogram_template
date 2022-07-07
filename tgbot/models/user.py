from sqlalchemy import Column, BigInteger, String

from tgbot.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    name = Column(String(length=60), nullable=False)
    username = Column(String(length=100), nullable=True)
    language = Column(String(length=10), nullable=False)

    def __repr__(self):
        return f'{self.user_id} | {self.name} | {self.username} | {self.language}'

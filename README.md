# Aiogram bot template
This is a simple aiogram bot template using PostgreSQL as database
```
⚠️ Make sure you have a Postgresql database installed
```
1. Rename `bot.ini.example` to `bot.ini`
2. Install requirements using: 
```
pip install -r requirements.txt
```
3. Make migrations using Alembic
```
alembic revision --autogenerate -m "init"
```
```
alembic upgrade head
```
4. Add your logic to own bot


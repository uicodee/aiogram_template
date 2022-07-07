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
3. Create database in psql
4. Make migrations using Alembic
```
alembic revision --autogenerate -m "init"
```
```
alembic upgrade head
```
5. To add new language - add language key in ```tgbot/data/data.py```
6. Add your logic to own bot


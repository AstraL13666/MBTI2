import os
from dotenv import load_dotenv, find_dotenv
from aiogram.types import BotCommand

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("bot_token")
ADMIN_ID = int(os.getenv("admins_id"))

DEFAULT_COMMANDS = [
    BotCommand("start", "Запустить бота")
]

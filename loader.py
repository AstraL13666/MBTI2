from aiogram import Bot, Dispatcher

from config_data import BOT_TOKEN
from utils import on_startup_notify, on_shutdown_notify
from utils import set_default_commands

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def bot_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)


async def bot_shutdown(dp):
    await on_shutdown_notify(dp)

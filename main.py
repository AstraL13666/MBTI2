from aiogram import executor

from handlers import register_message_handlers, register_callback_query_handler
from loader import dp, bot_startup, bot_shutdown
from utils import setup_logger

register_callback_query_handler(dp)
register_message_handlers(dp)


if __name__ == '__main__':
    setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=bot_startup,
                           on_shutdown=bot_shutdown
                           )

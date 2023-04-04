import logging

from config_data import ADMIN_ID
from .misc import txt


async def on_startup_notify(dp):
    try:
        await dp.bot.send_message(chat_id=ADMIN_ID,
                                  text=txt.notify(key='on_startup'))

    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp):
    try:
        await dp.bot.send_message(chat_id=ADMIN_ID,
                                  text=txt.notify(key='on_shutdown'))

    except Exception as err:
        logging.exception(err)

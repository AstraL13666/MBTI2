from aiogram.types import Message

from config_data import ADMIN_ID
from loader import bot
from utils import txt


async def admin_notify(mes: Message):
    await bot.send_message(
        chat_id=ADMIN_ID,
        text=txt.notify('new_user').format(
            mes.from_user.id,
            mes.from_user.first_name,
            mes.from_user.last_name)
    )  # ID, F-name, L-name'

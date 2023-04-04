from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from .admins import admin_notify
from loader import bot
from utils import txt

from keyboards import keyboard


async def start_command(mes: Message):
    await admin_notify(mes)
    await bot.send_message(
        chat_id=mes.from_user.id,
        text=txt.user('CommandStart').format(mes.from_user.first_name),
        reply_markup=keyboard.menu()
    )


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, CommandStart())

import asyncio

from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from utils import txt
from keyboards import keyboard
from data_temp import Answer, Question
from test import data, quest_iter
from test_calc import User


async def callback_start(call: CallbackQuery):
    await call.message.edit_text(
        text=txt.user('CallbackMenu'),
        reply_markup=keyboard.help_general()
    )


async def callback_description(call: CallbackQuery):
    await call.message.edit_text(
        text=txt.mbti('description'),
        reply_markup=keyboard.back()
    )


async def callback_test_description(call: CallbackQuery):
    await call.message.edit_text(
        text=txt.mbti('test_desc'),
        reply_markup=keyboard.back()
    )


async def callback_back(call: CallbackQuery):
    await call.message.edit_text(
        text=txt.user('CallbackMenu'),
        reply_markup=keyboard.help_general()
    )


async def callback_exit(call: CallbackQuery):
    await call.message.edit_text(
        text=txt.user('Thanks'),
        reply_markup=None
    )


async def pre_testing(call: CallbackQuery):
    Answer.value = {}
    Question.quest = 0

    await call.message.edit_text(
        text=txt.mbti('test_rule'),
        reply_markup=keyboard.test_rule()
    )


async def testing(call: CallbackQuery):
    index = quest_iter.__next__()

    Question.quest = index

    quests = data[index][0]

    res_a = data[index][1]
    res_b = data[index][2]

    text_answer = txt.mbti('quest')

    if len(Answer.value.keys()) < 35:
        kbrd_answer = keyboard.create_test_button(
            pos_a=res_a,
            pos_b=res_b,
            index=index)
    else:
        kbrd_answer = keyboard.create_test_button_ne(
            pos_a=res_a,
            pos_b=res_b,
            index=index)

    await call.message.edit_text(
        text=text_answer.format(index, quests),
        reply_markup=kbrd_answer
    )


async def test_hole(call: CallbackQuery):
    if call.data[0] == 'a':
        Answer.value[int(call.data[1:])] = data[Question.quest][1]

    elif call.data[0] == 'b':
        Answer.value[int(call.data[1:])] = data[Question.quest][2]

    else:
        pass

    if len(Answer.value.keys()) == 70:
        await call.message.edit_text(
            text=txt.mbti('complete'),
            reply_markup=None
        )

        calc = User(Answer.value)
        res = calc.calculate(res_data=Answer.value)

        await asyncio.sleep(2)
        await call.message.edit_text(
            text=res,
            reply_markup=keyboard.exit()
        )

    else:
        asyncio.create_task(testing(call))


def register_callback_query_handler(dp: Dispatcher):
    dp.register_callback_query_handler(callback_start, text='menu')
    dp.register_callback_query_handler(callback_description, text='help_desc')
    dp.register_callback_query_handler(callback_test_description, text='help_test_desc')
    dp.register_callback_query_handler(pre_testing, text='start')
    dp.register_callback_query_handler(testing, text='test_start')
    dp.register_callback_query_handler(callback_back, text='return')
    dp.register_callback_query_handler(callback_exit, text='all_exit')
    dp.register_callback_query_handler(test_hole)

from utils import txt
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove


class CreateKeyboard:

    def __init__(self):
        self.kbrd_start = InlineKeyboardButton(text=txt.button('start'), callback_data='start')
        self.kbrd_test_start = InlineKeyboardButton(text=txt.button('start'), callback_data='test_start')
        self.kbrd_stop = InlineKeyboardButton(text=txt.button('stop'), callback_data='stop')
        self.kbrd_exit = InlineKeyboardButton(text=txt.button('exit'), callback_data='all_exit')
        self.kbrd_return = InlineKeyboardButton(text=txt.button('return'), callback_data='return')
        self.kbrd_menu = InlineKeyboardButton(text=txt.button('menu'), callback_data='menu')

    def help_general(self):
        button_1 = InlineKeyboardButton(text=txt.button('description'), callback_data='help_desc')
        button_2 = InlineKeyboardButton(text=txt.button('test_desc'), callback_data='help_test_desc')

        return InlineKeyboardMarkup().add(self.kbrd_start, button_1).add(button_2, self.kbrd_exit)

    def menu(self):
        return InlineKeyboardMarkup().add(self.kbrd_menu)

    def back(self):
        return InlineKeyboardMarkup().add(self.kbrd_return)

    def test_rule(self):
        return InlineKeyboardMarkup().add(self.kbrd_test_start, self.kbrd_return)

    def exit(self):
        return InlineKeyboardMarkup().add(self.kbrd_exit)

    def create_test_button(self, pos_a, pos_b, index):
        but_a = InlineKeyboardButton(text=pos_a, callback_data=f'a{index}')
        but_b = InlineKeyboardButton(text=pos_b, callback_data=f'b{index}')

        return InlineKeyboardMarkup().add(but_a).add(but_b).add(self.kbrd_exit)

    def create_test_button_ne(self, pos_a, pos_b, index):
        but_a = InlineKeyboardButton(text=pos_a, callback_data=f'a{index}')
        but_b = InlineKeyboardButton(text=pos_b, callback_data=f'b{index}')

        return InlineKeyboardMarkup().add(but_a).add(but_b)


keyboard = CreateKeyboard()

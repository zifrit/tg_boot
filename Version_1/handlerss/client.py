import random

from Version_1.keyboards.inlinekeyboard import create_day_actions_keyboard, create_days_keyboard, list_exist_game
from Version_1.main import dp, bot
from aiogram.types import Message, CallbackQuery
from Version_1.keyboards.keyboard import kb_menu, kb_some
from Version_1.keyboards import keyboard
import requests

users = {}
players = {}
play = False

BASE_URL = 'http://127.0.0.1:8000/'


def who_win(players: dict):
    pass


@dp.message_handler(commands=['start'])
async def start(message: Message):
    text = f'Добро пожаловать {message.from_user.full_name}'
    user = {
        'tg_id': message.from_user.id,
        'username': 'NoneUsername' if message.from_user.username == None else message.from_user.username,
    }
    requests.post(f"{BASE_URL}/tg/", json=user)
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=kb_menu)


@dp.message_handler(commands=['menu'])
async def menu(message: Message):
    await message.answer(text='Кнопки изменены', reply_markup=kb_menu)


@dp.message_handler(commands=['some'])
async def somecommand(message: Message):
    await message.answer(text='Кнопки изменены', reply_markup=keyboard.kb_list_game)


@dp.message_handler(commands=['games'])
async def start_game(message: Message):
    await message.answer(text='Кнопки изменены', reply_markup=keyboard.kb_list_game)


@dp.message_handler(commands=['list_game'])
async def start_game(message: Message):
    await message.answer(text='Список игр:\n'
                              '/kmn камень ножницы бумага')
    # await message.delete()


# @dp.message_handler()
# async def commands(message: Message):
#     if play:
#         pl = message.text.split()
#         global players
#         u = [value['username'] for key, value in users.items()]
#         for p in pl:
#             if p in u:
#                 players[message.from_user.id] = [p]
#             else:
#                 await message.answer(text=f'такого пользователя нет {p}')
#     else:
#         text_message = message.text
#         await bot.send_message(chat_id=message.chat.id, text=text_message)
#         await message.delete()

#
# #     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
# #             .intersection(set(json.load(open('json файл')))) != set():
# #         await message.reply('маты запрещены')
# #         await message.delete()


# создаем клавиатуру для выбора дня недели


# обработчик старта диалога
@dp.message_handler(commands=['startt'])
async def start_message_handler(message):
    await bot.send_message(chat_id=message.chat.id, text='Выберите день недели', reply_markup=create_days_keyboard)


# обработчик нажатия кнопок выбора дня недели
@dp.callback_query_handler(
    lambda call: call.data in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
async def day_callback_handler(call: CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'Выбран {call.data}',
                                reply_markup=create_day_actions_keyboard)


# обработчик нажатия кнопки Назад
@dp.callback_query_handler(lambda call: call.data == 'back')
async def back_callback_handler(call: CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Выберите день недели',
                                reply_markup=create_days_keyboard)


# обработчик текстовых сообщений
# @dp.message_handler(content_types=['text'])
# async def text_message_handler(message):
#     await bot.send_message(chat_id=message.chat.id, text='Выберите день недели', reply_markup=create_days_keyboard)

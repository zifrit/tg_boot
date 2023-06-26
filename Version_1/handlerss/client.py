import random

from Version_1.main import dp, bot
from aiogram.types import Message
from Version_1.keyboards.keyboard import kb_menu, kb_some

users = {}
players = {}


def who_win(players: dict):
    pass


async def start(message: Message):
    global users
    text = f'Добро пожаловать {message.from_user.full_name}'
    users[message.from_user.id] = {
        'id': message.from_user.id,
        'username': message.from_user.username
    }
    print(users)
    print(message.from_user)
    print(message.chat)
    await bot.send_message(chat_id=message.chat.id, text=text)


async def game(message: Message):
    await message.answer(text='Выберите игроков!!')
    await message.answer(text='Старт игры.\n'
                              'Напишите в лс боту вам выбор:\n'
                              'к - камень\n'
                              'н - ножницы\n'
                              'б - бумага')


async def menu(message: Message):
    await message.answer(text='выбор', reply_markup=kb_menu)


async def somecommand(message: Message):
    await message.answer(text='выбор', reply_markup=kb_some)


async def commands(message: Message):
    text_message = message.text
    await bot.send_message(chat_id=message.chat.id, text=text_message)
    await message.delete()

#
# #     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
# #             .intersection(set(json.load(open('json файл')))) != set():
# #         await message.reply('маты запрещены')
# #         await message.delete()

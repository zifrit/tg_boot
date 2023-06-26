import random

from Version_1.main import dp, bot
from aiogram.types import Message
from Version_1.keyboards.keyboard import kb_menu, kb_some

users = {}
players = {}
play = False


def who_win(players: dict):
    pass


@dp.message_handler(commands=['start'])
async def start(message: Message):
    global users
    text = f'Добро пожаловать {message.from_user.full_name}'
    users[message.from_user.id] = {
        'id': message.from_user.id,
        'username': message.from_user.username
    }
    # print(users)
    # print(message.from_user)
    # print(message.chat)
    print(players)
    await bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(commands=['menu'])
async def menu(message: Message):
    await message.answer(text='выбор', reply_markup=kb_menu)


@dp.message_handler(commands=['some'])
async def somecommand(message: Message):
    await message.answer(text='выбор', reply_markup=kb_some)


@dp.message_handler()
async def commands(message: Message):
    if play:
        pl = message.text.split()
        global players
        u = [value['username'] for key, value in users.items()]
        for p in pl:
            if p in u:
                players[message.from_user.id] = [p]
            else:
                await message.answer(text=f'такого пользователя нет {p}')
    else:
        text_message = message.text
        await bot.send_message(chat_id=message.chat.id, text=text_message)
        await message.delete()

#
# #     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
# #             .intersection(set(json.load(open('json файл')))) != set():
# #         await message.reply('маты запрещены')
# #         await message.delete()

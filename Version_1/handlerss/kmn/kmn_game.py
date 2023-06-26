from Version_1.main import dp, bot
from aiogram.types import Message
from Version_1.keyboards.keyboard import kb_menu, kb_some

users = {}
players = {}
play = False


@dp.message_handler(commands=['kmn'])
async def game(message: Message):
    global play
    play = True
    await message.answer(text='Выберите игроков!!')


@dp.message_handler(commands=['play'])
async def choice(message: Message):
    global play
    if not play:
        await message.answer(text='игра еще не началась')
    await message.answer(text='игра началась')
    await message.answer(text='выберите что ответить:\n'
                              'к - камень\n'
                              'н - ножницы\n'
                              'б - бумага')
    text = message.text
    if text not in ['к', 'н', 'б']:
        await message.answer(text='такого ответ нет. \n'
                                  'нажмите /play и выберите еще раз')
    else:
        global players
        players[message.from_user.id].append(text)


@dp.message_handler(commands=['win'])
async def who_win(message: Message):
    pass

from Version_1.main import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from .states import Register
import requests

users = {}
players = {}
play = False
BASE_URL = 'http://127.0.0.1:8000/'


@dp.message_handler(commands=['kmn'])
async def game(message: Message):
    await message.answer(text='Введите название комнаты.\n'
                              'И Один из вариантов ответа:\n'
                              'к - камень\n'
                              'н - ножницы\n'
                              'б - бумага\n'
                              'Шаблон: \n "название комнаты" "выбранный вами ответ"')
    # \n
    # '
    # 'И Один из вариантов ответа:\n'
    # 'к - камень\n'
    # 'н - ножницы\n'
    # 'б - бумага\n'
    # 'Шаблон: <название комнаты> <к>
    await Register.game_name.set()


@dp.message_handler(state=Register.game_name)
async def name_game(message: Message, state: FSMContext):
    answer = message.text.split()
    print(answer)
    await state.update_data(game_name=answer[0])
    st = await state.get_data('game_name')
    requests_tg = {
        'user': message.from_user.id,
        'answer': answer[1],
        'game_name': st['game_name']
    }
    response = requests.post(f'{BASE_URL}/start_kmn/', json=requests_tg)
    print(response.json())
    await message.reply(text='игра создана')
    await state.finish()


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

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
    await message.answer(text='Придумайте название комнаты.\n'
                              'И Один из вариантов ответа:\n'
                              'к - камень\n'
                              'н - ножницы\n'
                              'б - бумага\n'
                              'Шаблон: \n "название комнаты" "выбранный вами ответ"')
    await Register.game_name.set()


@dp.message_handler(state=Register.game_name)
async def name_game(message: Message, state: FSMContext):
    answer = message.text.split()
    await state.update_data(game_name=answer[0])
    st = await state.get_data('game_name')
    requests_tg = {
        'user': message.from_user.id,
        'answer': answer[1],
        'game_name': st['game_name']
    }
    response = requests.post(f'{BASE_URL}/start_kmn/', json=requests_tg)
    if response.json()['status']:
        await message.reply(text=response.json()['message'])
        await state.finish()
    else:
        await message.reply(text=response.json()['message'])
        await message.answer(text='Начните создавать игру заново')
        await state.finish()


@dp.message_handler(commands=['join_game'])
async def choice_room(message: Message):
    await message.answer(text='Введите название комнаты.\n')
    await Register.join_in_game.set()


@dp.message_handler(state=Register.join_in_game)
async def join_game(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(join_in_game=answer)
    st = await state.get_data('join_in_game')
    requests_tg = {
        'user': message.from_user.id,
        'room_name': st['join_in_game']
    }
    response = requests.post(f'{BASE_URL}/join_kmn/', json=requests_tg)
    if response.json()['message'] == 'Вы уже в комнате':
        await message.reply(text=response.json()['message'])
        await message.answer(text='Ожидайте окончания игры')
        await state.finish()
    elif response.json()['message'] == 'Вы присоединились к комнате':
        await message.reply(text=response.json()['message'])
        await message.answer(text='Выберите один из вариантов: \n'
                                  'к - камень\n'
                                  'н - ножницы\n'
                                  'б - бумага\n')
        await Register.answer.set()

    elif not response.json()['status']:
        await message.reply(text=response.json()['message'])
        await message.answer(text='Присоединитесь заново /join_game')
        await state.finish()


@dp.message_handler(state=Register.answer)
async def join_game(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    st_1 = await state.get_data('answer')
    st_2 = await state.get_data('join_in_game')
    requests_tg = {
        'user': message.from_user.id,
        'room_name': st_2['join_in_game'],
        'answer': st_1['answer']
    }
    response = requests.post(f'{BASE_URL}/answer_kmn/', json=requests_tg)
    if response.json()['status']:
        await message.reply(text=response.json()['message'])
        await state.finish()
    else:
        await message.reply(text=response.json()['message'])
        await message.answer(text='Присоединитесь заново /join_game')
        await state.finish()

    # global play
    # if not play:
    #     await message.answer(text='игра еще не началась')
    # await message.answer(text='игра началась')
    # await message.answer(text='выберите что ответить:\n'
    #                           'к - камень\n'
    #                           'н - ножницы\n'
    #                           'б - бумага')
    # text = message.text
    # if text not in ['к', 'н', 'б']:
    #     await message.answer(text='такого ответ нет. \n'
    #                               'нажмите /play и выберите еще раз')
    # else:
    #     global players
    #     players[message.from_user.id].append(text)


@dp.message_handler(commands=['win'])
async def who_win(message: Message):
    pass

from Version_1.main import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from .states import Register
import requests

users = {}
players = {}
play = False
BASE_URL = 'http://127.0.0.1:8000/kmn'


@dp.message_handler(commands=['kmn'])
async def game(message: Message):
    await message.answer(text='Придумайте название комнаты.\n'
                              'И Один из вариантов ответа:\n'
                              'к - камень\n'
                              'н - ножницы\n'
                              'б - бумага\n'
                              'Шаблон: \n "название комнаты" "выбранный вами ответ"\n'
                              'Примечание: название комнаты должно быть одним словом')
    await Register.game_name.set()


@dp.message_handler(state=Register.game_name)
async def name_game(message: Message, state: FSMContext):
    answer = message.text.split()
    if len(answer) == 1:
        await message.reply(text='Не корректная форма ввода \n'
                                 'Проверьте правильность ввода сверившись с шаблоном')
    else:
        await state.update_data(game_name=answer[0])
        st = await state.get_data('game_name')
        requests_tg = {
            'user': message.from_user.id,
            'answer': answer[1],
            'game_name': st['game_name']
        }
        response = requests.post(f'{BASE_URL}/start/', json=requests_tg)
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
    response = requests.get(f'{BASE_URL}/search_join/', json=requests_tg)
    if response.json()['message'] == 'Вы уже в комнате':
        await message.reply(text=response.json()['message'])
        await message.answer(text='Ожидайте окончания игры')
        await state.finish()
    elif response.json()['message'] == 'Вы присоединились к комнате':
        await message.reply(text=response.json()['message'])
        await message.answer(text='Выберите один из вариантов ответа: \n'
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
    response = requests.post(f'{BASE_URL}/search_join/', json=requests_tg)
    if response.json()['status']:
        await message.reply(text=response.json()['message'])
        await state.finish()
    else:
        await message.reply(text=response.json()['message'])
        await message.answer(text='Присоединитесь заново /join_game')
        await state.finish()


@dp.message_handler(commands=['end_game'])
async def choice_room(message: Message):
    await message.answer(text='Введите название комнаты.\n')
    await Register.end_game.set()


@dp.message_handler(state=Register.end_game)
async def end_game(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(end_game=answer)
    st = await state.get_data('end_game')
    requests_tg = {
        'user': message.from_user.id,
        'room_name': st['end_game']
    }
    response = requests.post(f'{BASE_URL}/end_game/', json=requests_tg)
    if response.json()['status'] == 'D':
        for otvet in response.json()['message']:
            await bot.send_message(chat_id=otvet[0], text=f'Игра окончилась. \n'
                                                          f'В комнате {st["end_game"]} у вас {otvet[1]}')
        await state.finish()
    elif response.json()['status']:
        for otvet in response.json()['message']:
            await bot.send_message(chat_id=otvet[0], text=f'Игра окончилась. \n'
                                                          f'В комнате {st["end_game"]} вы {otvet[1]}')
        await state.finish()
    else:
        await message.reply(text=response.json()['message'])
        await state.finish()

    requests.delete(f'{BASE_URL}/list_games/{response.json()["room_id"]}')

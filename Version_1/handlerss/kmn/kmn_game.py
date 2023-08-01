import random

import requests

from Version_1.keyboards import inlinekeyboard
from Version_1.main import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from Version_1.keyboards import keyboard
from .states import Register

users = {}
players = {}
play = False
# BASE_URL = 'http://127.0.0.1:8000/kmn' #без докера
BASE_URL = 'http://dj_app:8000/kmn' #с докером


@dp.message_handler(commands=['start_kmn'])
async def game(message: Message):
    await message.answer(text='Придумайте название комнаты.\n'
                              'И Один из вариантов ответа:\n'
                              'к - камень\n'
                              'н - ножницы\n'
                              'б - бумага\n'
                              'Шаблон: \n "название комнаты" "выбранный вами ответ"\n'
                              'Пример: \n черная-комната к\n'
                              'Примечание: название комнаты должно быть одним словом\n')
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


@dp.message_handler(commands=['join_kmn'])
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
        for otvet in response.json()['notification']:
            await bot.send_message(chat_id=otvet[0], text=otvet[1])

    else:
        await message.reply(text=response.json()['message'])
        await message.answer(text='Присоединитесь заново /join_game')
        await state.finish()


@dp.message_handler(commands=['end_kmn'])
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
        requests.delete(f'{BASE_URL}/list_games/{response.json()["room_id"]}')
        await state.finish()
    elif response.json()['status']:
        for otvet in response.json()['message']:
            await bot.send_message(chat_id=otvet[0], text=f'Игра окончилась. \n'
                                                          f'В комнате {st["end_game"]} вы {otvet[1]}')
        requests.delete(f'{BASE_URL}/list_games/{response.json()["room_id"]}')
        await state.finish()
    else:
        await message.reply(text=response.json()['message'])
        await state.finish()


previous_page: str = ''
next_page: str = ''


async def get_page_data(action: str):
    global previous_page, next_page
    if action == 'previous':
        response = requests.get(previous_page).json()
        list_games = '\n'.join(
            [
                f'{number}) {game["administrator"]} создал комнату {game["game_name"]} ' for number, game in
                enumerate(response['results'], 1)
            ])
        next_page = response['next'] if response['next'] else ''
        previous_page = response['previous'] if response['previous'] else ''
        return list_games, inlinekeyboard.list_exist_game if response['previous'] else inlinekeyboard.next_game
    elif action == 'next':
        response = requests.get(next_page).json()
        list_games = '\n'.join(
            [
                f'{number}) {game["administrator"]} создал комнату {game["game_name"]} ' for number, game in
                enumerate(response['results'], 1)
            ])
        next_page = response['next'] if response['next'] else ''
        previous_page = response['previous'] if response['previous'] else ''
        return list_games, inlinekeyboard.list_exist_game if response['next'] else inlinekeyboard.previous_game


@dp.message_handler(commands=['list_kmn'])
async def back(message: Message):
    response = requests.get(f'{BASE_URL}/games/').json()
    if response['count'] > 4:
        global next_page
        next_page = response['next']
        print(next_page)
        list_games = '\n'.join(
            [
                f'{number}) {game["administrator"]} создал комнату {game["game_name"]} ' for number, game in
                enumerate(response['results'], 1)
            ])
        await message.answer(text=f'<b>Список созданных комнат:</b> \n{list_games}',
                             reply_markup=inlinekeyboard.next_game)
    else:
        list_games = '\n'.join(
            [
                f'{number}) {game["administrator"]} создал комнату {game["game_name"]} ' for number, game in
                enumerate(response['results'], 1)
            ])
        await message.answer(text=f'<b>Список созданных комнат:</b> \n{list_games}')


@dp.callback_query_handler(lambda call: call.data in ['previous', 'next'])
async def previous_list(call: CallbackQuery):
    list_games, inline = await get_page_data(call.data)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'✍️<b>Список созданных комнат:</b> \n {list_games}',
                                reply_markup=inline)


@dp.message_handler(commands=['back'])
async def back(message: Message):
    await message.answer(text='🔄', reply_markup=keyboard.kb_menu)


@dp.message_handler(commands=['manual_kmn'])
async def back(message: Message):
    await message.answer(text='Правила: \n'
                              'Игру может закончить только тот кто его создал. \n'
                              'Ограничение количество игроков в комнате: 2. \n'
                              '\n\n\n'
                              '<b> 🕹 Команды бота: </b>\n'
                              '👉 /start_kmn - запуская создание комнаты где будет проходить игра \n'
                              '👉 /join_kmn - присоединение к комнате \n'
                              '👉 /end_kmn -  завершить игру в комнате \n'
                              '👉 /list_kmn - список существующих комнат с игрой \n')

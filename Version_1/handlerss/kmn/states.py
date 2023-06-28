from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    game_name = State()
    join_in_game = State()
    answer = State()
    end_game = State()

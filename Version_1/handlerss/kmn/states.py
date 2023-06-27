from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    game_name = State()
    state2 = State()

from aiogram import types

list_exist_game = types.InlineKeyboardMarkup(row_width=2)
list_exist_game.add(
    types.InlineKeyboardButton(text='<<<', callback_data='previous'),
    types.InlineKeyboardButton(text='>>>', callback_data='next'),
)
previous_game = types.InlineKeyboardMarkup(row_width=1)
previous_game.add(
    types.InlineKeyboardButton(text='<<<', callback_data='previous'),
)
next_game = types.InlineKeyboardMarkup(row_width=1)
next_game.add(
    types.InlineKeyboardButton(text='>>>', callback_data='next'),
)

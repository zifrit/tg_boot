from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/some'),
            KeyboardButton(text='/kmn'),
        ],
        [
            KeyboardButton(text='112')
        ],
        [
            KeyboardButton(text='/games'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
        ]
    ],
    resize_keyboard=True
)
kb_some = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/menu'),
        ],
    ],
    resize_keyboard=True
)

kb_list_game = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start_game'),
            KeyboardButton(text='/join_game'),
            KeyboardButton(text='/end_game'),
        ],
    ],
    resize_keyboard=True
)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/some'),
        ],
        [
            KeyboardButton(text='112')
        ],
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
        ]
    ],
    resize_keyboard=True
)
kb_some = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
        ],
    ],
    resize_keyboard=True
)
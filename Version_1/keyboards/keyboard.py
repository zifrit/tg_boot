from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/games'),
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
            KeyboardButton(text='/list_kmn'),
            KeyboardButton(text='/start_kmn'),
            KeyboardButton(text='/join_kmn'),
            KeyboardButton(text='/end_kmn'),
        ],
        [
            KeyboardButton(text='/back'),
            KeyboardButton(text='/manual_kmn'),
        ]

    ],
    resize_keyboard=True
)
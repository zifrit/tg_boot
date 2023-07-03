from aiogram import types

create_days_keyboard = types.InlineKeyboardMarkup(row_width=2)
create_days_keyboard.add(types.InlineKeyboardButton(text='Понедельник', callback_data='monday'),
                         types.InlineKeyboardButton(text='Вторник', callback_data='tuesday'),
                         types.InlineKeyboardButton(text='Среда', callback_data='wednesday'),
                         types.InlineKeyboardButton(text='Четверг', callback_data='thursday'),
                         types.InlineKeyboardButton(text='Пятница', callback_data='friday'),
                         types.InlineKeyboardButton(text='Суббота', callback_data='saturday'),
                         types.InlineKeyboardButton(text='Воскресенье', callback_data='sunday'))

# создаем клавиатуру для выбора действий
# async def create_day_actions_keyboard():
create_day_actions_keyboard = types.InlineKeyboardMarkup(row_width=2)
create_day_actions_keyboard.add(types.InlineKeyboardButton(text='Добавить задание', callback_data='add_task'),
                                types.InlineKeyboardButton(text='Удалить задание', callback_data='delete_task'),
                                types.InlineKeyboardButton(text='Назад', callback_data='back'))

list_exist_game = types.InlineKeyboardMarkup(row_width=2)
list_exist_game.add(
    types.InlineKeyboardButton(text='<<<', callback_data='previous'),
    types.InlineKeyboardButton(text='>>>', callback_data='next'),
)

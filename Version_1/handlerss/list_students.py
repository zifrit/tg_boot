from Version_1.main import dp, bot
from aiogram.types import Message
from Version_1.keyboards.keyboard import kb_menu, kb_some


# @dp.message_handler(commands=['start'])
# async def start(message: Message):
#     text = f'вы отправили {message.from_user.full_name}'
#     await bot.send_message(chat_id=message.chat.id, text=text)
#
#
# @dp.message_handler(commands=['menu'])
# async def menu(message: Message):
#     await message.answer(text='выбор', reply_markup=kb_menu)
#
#
# @dp.message_handler(commands=['some'])
# async def somecommand(message: Message):
#     await message.answer(text='выбор', reply_markup=kb_some)
#
#
# @dp.message_handler(commands=['100'])
# async def somecommand(message: Message):
#     await message.answer(text='gjitk')
#
#
# @dp.message_handler()
# async def commands(message: Message):
#     text_message = message.text
#     await bot.send_message(chat_id=message.chat.id, text=text_message)
#     await message.delete()

#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
#             .intersection(set(json.load(open('json файл')))) != set():
#         await message.reply('маты запрещены')
#         await message.delete()

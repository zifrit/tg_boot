# # import string, json
# import json
# import string
#
# from Version_1.main import dp, bot
# from aiogram.types import Message
# from Version_1.config import admins_id
#
#
# async def answer(dp):
#     await bot.send_message(chat_id=admins_id[0], text='раз')
#     await bot.send_message(chat_id=admins_id[0], text='два')
#     await bot.send_message(chat_id=admins_id[0], text='три')
#
#
# # @dp.message_handler(commands=['start'])
# # async def start(message: Message):
# #     text = f'вы отправили {message.from_user.full_name}'
# #     await bot.send_message(chat_id=message.from_user.id, text=text)
# #     # await message.answer(text=text)
#
#
# # @dp.message_handler(Command('menu'))
# # async def commands(message: Message):
# #     await message.answer(text='выбор', reply_markup=kb_menu)
# #
# #
# # @dp.message_handler(Command('some'))
# # async def commands(message: Message):
# #     await message.answer(text='выбор', reply_markup=kb_some)
#
#
# @dp.message_handler()
# async def commands(message: Message):
#     await message.answer(message.text)
#
#
# @dp.message_handler()
# async def commands(message: Message):
#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
#             .intersection(set(json.load(open('json файл')))) != set():
#         await message.reply('маты запрещены')
#         await message.delete()

#

for i in range(3):
    print(i)
    print('sd')
    for j in range(10):
        if j % 2 == 0:
            break
        print('да', j)

# print(6 //2)
# print(6 % 2)
a = []
a.append()
from aiogram.dispatcher.filters import Command

from Version_1.main import dp, bot
from aiogram.types import Message
from aiogram import Dispatcher
from Version_1.keyboards.keyboard import kb_menu, kb_some


@dp.message_handler(commands=['start'])
async def start(message: Message):
    text = f'вы отправили {message.from_user.full_name}'
    await bot.send_message(chat_id=message.from_user.id, text=text)
    # await message.answer(text=text)


@dp.message_handler(commands=['menu'])
async def menu(message: Message):
    await message.answer(text='выбор', reply_markup=kb_menu)


@dp.message_handler(commands=['some'])
async def somecommand(message: Message):
    await message.answer(text='выбор', reply_markup=kb_some)


def register_command_from_bot(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(menu, commands=['menu'])
    dp.register_message_handler(somecommand, commands=['some'])
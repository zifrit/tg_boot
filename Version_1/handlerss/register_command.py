from Version_1.handlerss import client, list_students

from aiogram import Dispatcher


def register_command_from_bot(dp: Dispatcher):
    dp.register_message_handler(client.start, commands=['start'])
    dp.register_message_handler(client.game, commands=['kmn'])
    dp.register_message_handler(client.menu, commands=['menu'])
    dp.register_message_handler(client.somecommand, commands=['some'])
    dp.register_message_handler(client.commands)

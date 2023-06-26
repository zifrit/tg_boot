import asyncio
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from Version_1.config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from Version_1.handlerss.client import *
    # from handlerss import register_command
    #
    # register_command.register_command_from_bot(dp)
    executor.start_polling(dp)

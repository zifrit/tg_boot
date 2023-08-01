import asyncio
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN

storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop, storage=storage)

if __name__ == '__main__':
    # from Version_1.handlerss.client import *
    from handlerss.register_command import *
    #
    # register_command.register_command_from_bot(dp)
    executor.start_polling(dp, skip_updates=True)

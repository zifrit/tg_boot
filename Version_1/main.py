from aiogram import Bot, Dispatcher, executor
import asyncio
from date.config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlerss.start_main import dp, answer
    from handlerss import admin, client

    client.register_command_from_bot(dp)

    executor.start_polling(dp, on_startup=answer, skip_updates=True)

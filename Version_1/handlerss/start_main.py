from Version_1.main import dp, bot
from Version_1.date.config import admins_id

async def answer(dp):
    await bot.send_message(chat_id=admins_id[0], text='раз')
    await bot.send_message(chat_id=admins_id[0], text='два')
    await bot.send_message(chat_id=admins_id[0], text='три')
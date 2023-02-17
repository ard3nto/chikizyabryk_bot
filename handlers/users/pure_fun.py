from aiogram import types
from loader import bot, dp, translator

import datetime
from asyncio import sleep
import random

@dp.message_handler(commands=['do_not_click', 'ban_me_please'], commands_prefix="/", chat_type=["group", "supergroup"], is_not_admin=True)
async def rand_mute(msg: types.Message):
    rand_time = random.randint(1, 60)
    seconds = (60 - int(datetime.datetime.now().strftime('%S')))-60
    if seconds <= -30:
        seconds=seconds+(-30-seconds)
    try:
        await bot.restrict_chat_member(msg.chat.id, msg.from_user.id, types.ChatPermissions(False), until_date=datetime.timedelta(minutes=rand_time, seconds=seconds+1))
        status = True
    except Exception as e:
        e = translator.translate(str(e))
        new_msg = await msg.reply(e)
        status = False
    if status:
        new_msg = await msg.answer(f'Ви виграли мут на {rand_time}хв.\nЦе повідомлення видалиться секунд через 5.')
    if random.randint(0, 3) == 1:
        rand_time2 = random.randint(5, 25)
        await sleep(rand_time2)
        await new_msg.delete()
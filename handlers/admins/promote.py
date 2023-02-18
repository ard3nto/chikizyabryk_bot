from aiogram import types
from aiogram.types import ChatMember
from loader import bot, dp, translator

from functions import promote

from functions.reply_checker import check_for_reply as is_reply

@dp.message_handler(commands=['promote'], commands_prefix='!', chat_type=["group", "supergroup"], is_admin=True)
async def promote_someone(msg: types.Message):
    if not await is_reply(msg):
        return
    role = msg.text.split(' ', maxsplit=1)[1]
    if role == 'admin':
        await promote.admin(msg)
    elif role == 'high moder':
        await promote.high_moder(msg)
    elif role == 'moder':
        await promote.moder(msg)
    else:
        await msg.reply(text='Будь-ласка, напиши одну команду з:\n<code>!promote admin</code>\n<code>!promote high moder</code>\n<code>!promote moder</code>')
from aiogram import types
from loader import bot, dp, translator

import config

import datetime

from functions import restrict_command_processors as cmd_proc_func

@dp.message_handler(commands=['ban'], commands_prefix="!", chat_type=["group", "supergroup"], reply=True, is_admin=True)
async def ban(msg: types.Message):
    until_date = await cmd_proc_func.restrict_command_processor(msg)
    if not until_date:
        return
    try:
        await bot.kick_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, until_date=until_date)
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        return
    if until_date.seconds == 1:
        await msg.answer(f'Користувача <a href="tg://user?id={msg.reply_to_message.from_user.id}">{msg.reply_to_message.from_user.first_name}</a> заблоковано назавжди')
        return
    await msg.answer(f'Користувача <a href="tg://user?id={msg.reply_to_message.from_user.id}">{msg.reply_to_message.from_user.first_name}</a> заблоковано до {(datetime.datetime.now() + until_date).strftime("%m/%d/%Y, %H:%M")}')
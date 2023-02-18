from aiogram import types
from loader import bot, dp, translator

import config

import datetime

from functions import restrict_command_processors as cmd_proc_func
from functions.reply_checker import check_for_reply as is_reply
from functions.check_permission import check_permission

@dp.message_handler(commands=['mute'], commands_prefix="!", chat_type=["group", "supergroup"], is_admin=True)
async def mute(msg: types.Message):
    if not await is_reply(msg):
        return
    if not await check_permission(msg):
        return
    until_date = await cmd_proc_func.restrict_command_processor(msg)
    if not until_date:
        return
    try:
        await bot.restrict_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=until_date)
        status = True
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        #logging.warning(f'| {msg.from_user.first_name} | {msg.from_user.language_code} | {msg.chat.type} | {e}')
    if until_date.seconds == 1:
        await msg.answer(f'Користувачеві <a href="tg://user?id={msg.reply_to_message.from_user.id}">{msg.reply_to_message.from_user.first_name}</a> заборонено надсилати повідомлення назавжди')
        return
    await msg.answer(f'Користувачеві <a href="tg://user?id={msg.reply_to_message.from_user.id}">{msg.reply_to_message.from_user.first_name}</a> заборонено надсилати повідомлення до {(datetime.datetime.now() + until_date).strftime("%m/%d/%Y, %H:%M")}')
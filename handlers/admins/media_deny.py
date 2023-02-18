from aiogram import types
from loader import bot, dp, translator

import config

import datetime

from functions import restrict_command_processors as cmd_proc_func
from functions.reply_checker import check_for_reply as is_reply
from functions.check_permission import check_permission

#media
@dp.message_handler(commands=['media'], commands_prefix="!", chat_type=["group", "supergroup"], is_admin=True)
async def mute(msg: types.Message):
    if not await is_reply(msg):
        return
    if not await check_permission(msg):
        return
    until_date = await cmd_proc_func.restrict_command_processor(msg)
    if not until_date:
        return
    try:
        await bot.restrict_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            permissions = types.ChatPermissions(
                can_send_messages=True, 
                can_send_media_messages=False, 
                can_send_polls=True,  
                can_send_other_messages=False, 
                can_add_web_page_previews=False, 
                can_change_info=True, 
                can_invite_users=True, 
                can_pin_messages=True
            ), 
            until_date=until_date
        )
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        return
    if until_date.seconds == 1:
        await msg.answer(f'Користувачеві <a href="tg://user?id={msg.reply_to_message.from_user.id}">{msg.reply_to_message.from_user.first_name}</a> заборонено надсилати медіа назавжди')
        return
    await msg.answer(f'Користувачеві <a href="tg://user?id={msg.reply_to_message.from_user.id}">{msg.reply_to_message.from_user.first_name}</a> заборонено надсилати медіа до {(datetime.datetime.now() + until_date).strftime("%m/%d/%Y, %H:%M")}')
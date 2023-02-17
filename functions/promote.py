from aiogram import types
from loader import bot, translator

async def admin(msg: types.Message):
    try:
        await bot.promote_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            can_manage_chat=True, 
            can_change_info=True, 
            can_delete_messages=True, 
            can_invite_users=True, 
            can_restrict_members=True, 
            can_pin_messages=True, 
            can_promote_members=True, 
            can_manage_video_chats=True
        )
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        return
    await msg.answer(f'[+] Користувача <code>{msg.reply_to_message.from_user.full_name.replace(">", "").replace("<", "")}</code> призначено адміністратором')

async def high_moder(msg: types.Message):
    try:
        await bot.promote_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            can_manage_chat=True, 
            can_change_info=True, 
            can_delete_messages=True, 
            can_invite_users=True, 
            can_restrict_members=True, 
            can_pin_messages=True, 
            can_manage_video_chats=True, 
        )
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        return
    await msg.answer(f'[+] Користувача <code>{msg.reply_to_message.from_user.full_name.replace(">", "").replace("<", "")}</code> призначено старшим модератором')

async def moder(msg: types.Message):
    try:
        await bot.promote_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            can_delete_messages=True, 
            can_restrict_members=True, 
            can_pin_messages=True, 
            can_manage_video_chats=True, 
        )
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        return
    await msg.answer(f'[+] Користувача <code>{msg.reply_to_message.from_user.full_name.replace(">", "").replace("<", "")}</code> призначено модератором')
from aiogram import types
from loader import bot, dp, translator

from functions.reply_checker import check_for_reply as is_reply

@dp.message_handler(commands=['unmute', 'unban', 'pardon'], chat_type=["group", "supergroup"], commands_prefix='!', is_admin=True)
async def unmute(msg: types.Message):
    if not await is_reply(msg):
        return
    try:
        await bot.restrict_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True, True, True, True, True, True))
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        return
    await msg.answer(f'З користувача <a href="tg://user?id={msg.reply_to_message.from_user.id}">{msg.reply_to_message.from_user.first_name}</a> знято усі обмеження!')
from aiogram import types

async def check_for_reply(msg: types.Message) -> bool:
    if not msg.reply_to_message:
        await msg.reply("Команда повинна бути відповіддю на повідомлення!")
        return False
    if msg.from_user.id == msg.reply_to_message.from_user.id:
        await msg.reply("Команда не може бути відповіддю на твоє ж повідомлення!")
        return False
    if msg.reply_to_message.from_user.id == msg.bot.id:
        await msg.reply('Команда не може бути відповіддю на моє повідомлення!')
        return False
    return True
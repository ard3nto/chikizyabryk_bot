from aiogram import types

async def check_permission(msg: types.Message) -> bool:
    member = await msg.bot.get_chat_member(msg.chat.id, msg.from_user.id)
    second_member = await msg.bot.get_chat_member(msg.reply_to_message.chat.id, msg.reply_to_message.from_user.id)
    if second_member.status not in ['creator', 'administrator']:
        return True
    elif (member.status == 'administrator' and member.can_restrict_members) and (second_member.can_restrict_members):
        await msg.reply('У тебе недостатньо прав для виконання цієї дії')
        return False
    return True
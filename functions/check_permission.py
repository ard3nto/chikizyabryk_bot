from aiogram import types

async def check_permission(msg: types.Message) -> bool:
    member = await msg.bot.get_chat_member(msg.chat.id, msg.from_user.id)
    second_member = await msg.bot.get_chat_member(msg.reply_to_message.chat.id, msg.reply_to_message.from_user.id)
    if second_member.status not in ['creator', 'administrator']:
        return True
    promoter_rights = 0
    target_user_rights = 0
    for key in dict(member).keys():
        if dict(member)[key] == True:
            promoter_rights += 1
    for key in dict(second_member).keys():
        if dict(second_member)[key] == True:
            target_user_rights += 1
    if promoter_rights <= target_user_rights:
        await msg.reply('У тебе недостатньо прав для виконання цієї дії')
        return False
    return True
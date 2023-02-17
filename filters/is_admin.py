from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import dp

class IsAdminFilter(BoundFilter):
    key = "is_admin"
    
    def __init__(self, is_admin):
        self.is_admin = is_admin
    
    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'creator':
            return True
        if member.status in ["administrator"]:
            if message.reply_to_message:
                if message.reply_to_message.from_user.id:
                    member2 = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                    if member2.status in ["administrator"]:
                        member1 = dict(member)
                        member2 = dict(member2)
                        member1_rights = 0
                        member2_rights = 0
                        for key in member1.keys():
                            if str(member1[key]) == 'True':
                                member1_rights += 1
                        for key in member2.keys():
                            if str(member2[key]) == 'True':
                                member2_rights += 1
                        if member1_rights <= member2_rights:
                            await message.reply(text='У тебе недостатньо прав для виконання цієї дії')
                            return False
            return member.can_restrict_members
        else:
            return False

dp.filters_factory.bind(IsAdminFilter)
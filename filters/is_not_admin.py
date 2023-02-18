from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import dp

class IsNotAdminFilter(BoundFilter):
    key = "is_not_admin"
    
    def __init__(self, is_not_admin):
        self.is_not_admin = is_not_admin
        
    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'creator':
            return False
        elif member.status == 'administrator':
            if member.can_restrict_members:
                return False
        return True

dp.filters_factory.bind(IsNotAdminFilter)
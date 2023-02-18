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
        elif member.status == 'administrator':
            if member.can_restrict_members:
                return True
        return False

dp.filters_factory.bind(IsAdminFilter)
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import dp

class CustomTitleLimitFilter(BoundFilter):
    key = "custom_title"
    
    def __init__(self, custom_title):
        self.custom_title = custom_title
        
    async def check(self, msg: types.Message):
        if msg.get_args() == None:
            return True
        if len(msg.get_args()) > 16:
            await msg.answer(text='Довжина ролі повинна бути не більше 16 символів у довжину')
            return False
        return True

dp.filters_factory.bind(CustomTitleLimitFilter)
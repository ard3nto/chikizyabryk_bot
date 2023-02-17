from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import dp

class IsReplyFilter(BoundFilter):
    key = "reply"
    
    def __init__(self, reply):
        self.reply = reply
        
    async def check(self, msg: types.Message):
        if not msg.reply_to_message:
            await msg.reply("Команда повинна бути відповіддю на повідомлення!")
            return False
        if msg.from_user.id == msg.reply_to_message.from_user.id:
            await msg.reply("Команда не може бути відповіддю на твоє ж повідомлення!")
            return False
        return True

dp.filters_factory.bind(IsReplyFilter)
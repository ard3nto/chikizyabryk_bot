import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher.handler import CancelHandler, current_handler

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 0):
        BaseMiddleware.__init__(self)
        self.rate_limit = limit

    async def on_process_message(self, msg: types.Message, data: dict):
        dp = Dispatcher.get_current()
        handler = current_handler.get()
        if handler:
            limit = getattr(handler, 'rate_limit', self.rate_limit)
        else:
            limit = self.rate_limit
        self.limit = limit
        try:
            await dp.throttle(key='antiflood_message', rate=limit)
        except Throttled as _t:
            await self.message_throttled(msg, _t)
            raise CancelHandler()
    
    async def message_throttled(self, msg: types.Message, throttled: Throttled):
        delta = throttled.rate - throttled.delta
        if throttled.exceeded_count <= 2:
            await msg.reply(f'⛔️ <b>Занадто часто</b>\nЗачекай {self.limit} секунд перед наступним повідомленням')
        elif throttled.exceeded_count > 2:
            await msg.delete()
        # await asyncio.sleep(delta)

def antiflood(limit: int = 0, key=None):
    def decorator(func):
        setattr(func, 'rate_limit', limit)
        return func
    return decorator
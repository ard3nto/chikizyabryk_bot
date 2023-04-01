from aiogram import types
from aiogram.utils import executor
import datetime
from loader import bot, dp, logging, scheduler
import handlers, filters

import config, middlewares

async def on_startup(x):
    logging.warning('Bot started')
    await bot.set_my_commands(config.commands)

async def on_shutdown(x):
    logging.warning('Bot stopped')


if __name__ == '__main__':
    scheduler.start()
    dp.middleware.setup(middlewares.antiflood.ThrottlingMiddleware())
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
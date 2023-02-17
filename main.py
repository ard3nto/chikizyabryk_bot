from aiogram import types
from aiogram.utils import executor
import datetime
from loader import bot, dp, logging
import handlers, filters

from translate import Translator
translator= Translator(to_lang="uk")

async def main(x):
    logging.warning('Bot started')
    await bot.set_my_commands([
        types.BotCommand("do_not_click", "Не натискати!"),
        types.BotCommand("ban_me_please", "Чисте задоволення")
    ])

async def shutdown(x):
    logging.warning('Bot stopped')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=main, on_shutdown=shutdown)
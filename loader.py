from aiogram import Bot, Dispatcher
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

from config import bot_token

bot = Bot(token=bot_token, parse_mode='HTML', disable_web_page_preview=True)
dp = Dispatcher(bot)

from translate import Translator
translator= Translator(to_lang="uk")
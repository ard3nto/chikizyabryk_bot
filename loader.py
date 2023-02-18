from aiogram import Bot, Dispatcher
from config import bot_token
import logging

from translate import Translator

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

bot = Bot(token=bot_token, parse_mode='HTML', disable_web_page_preview=True)
dp = Dispatcher(bot)

translator= Translator(to_lang="uk")
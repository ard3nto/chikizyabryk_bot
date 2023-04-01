from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from translate import Translator
from config import bot_token
import logging, asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.getLogger('apscheduler').setLevel(logging.CRITICAL)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

storage = MemoryStorage()
bot = Bot(token=bot_token, parse_mode='HTML', disable_web_page_preview=True)
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")

translator= Translator(to_lang="uk")
from aiogram import types
from loader import bot, dp, logging

import datetime
from asyncio import sleep
import random

from middlewares.antiflood import antiflood

@antiflood(5)
@dp.message_handler(commands=['roll'], commands_prefix="/.!")
async def roll(msg: types.Message):
    # random.randint(1, 60)
    args = msg.text.split(' ')[1:]
    args = [arg for arg in args if arg != '']
    args = [arg for arg in args if arg.isdigit()]
    args = sorted(args, key=lambda x: int(x))
    text_template = '🎲 Число від {} до {}'
    if args == []:
        try:
            rand_num = random.randint(0, 200)
        except ValueError:
            return
        text = text_template.format(0, 200)
    elif len(args) == 1 and args[0].isdigit():
        try:
            rand_num = random.randint(0, int(args[0]))
        except ValueError:
            return
        text = text_template.format(0, args[0])
    elif len(args) >= 2 and args[0].isdigit() and args[1].isdigit():
        try:
            rand_num = random.randint(int(args[0]), int(args[1]))
        except ValueError:
            return
        text = text_template.format(int(args[0]), args[1])
    await msg.answer(f'<b>{text}</b>: <tg-spoiler>{rand_num}</tg-spoiler>')
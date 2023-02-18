from aiogram import types
import datetime

async def restrict_command_processor(msg: types.Message) -> datetime.timedelta:
    splited = (msg.text+' 1s').split(' ')
    until_date = await get_time(splited=splited)
    if int(until_date.days) > 366:
        await msg.reply('Час обмеження не може бути більшим ніж 366дн')
        return False
    return until_date

async def get_time(splited: list[str]):
    if splited[1].endswith("m") and splited[1][:-1].isdigit():
        return datetime.timedelta(minutes=int(splited[1][:-1]))
    elif splited[1].endswith("h") and splited[1][:-1].isdigit():
        return datetime.timedelta(hours=int(splited[1][:-1]))
    elif splited[1].endswith("d") and splited[1][:-1].isdigit():
        return datetime.timedelta(days=int(splited[1][:-1]))
    return datetime.timedelta(seconds=1)
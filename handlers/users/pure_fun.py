from aiogram import types
from loader import bot, dp, logging

from aiogram.utils.exceptions import (
    ChatAdminRequired, 
    MethodNotAvailableInPrivateChats, 
    CantDemoteChatCreator,
    CantRestrictSelf, 
    NotEnoughRightsToRestrict,
    MethodIsNotAvailable
)

import datetime
from asyncio import sleep
import random

@dp.message_handler(commands=['do_not_click', 'ban_me_please'], commands_prefix="/", chat_type=["group", "supergroup"], is_not_admin=True)
async def rand_mute(msg: types.Message):
    rand_time = random.randint(1, 60)
    seconds = (60 - int(datetime.datetime.now().strftime('%S')))-60
    if seconds <= -30:
        seconds=seconds+(-30-seconds)
    try:
        await bot.restrict_chat_member(msg.chat.id, msg.from_user.id, types.ChatPermissions(False), until_date=datetime.timedelta(minutes=rand_time, seconds=seconds+1))
        status = True
    except ChatAdminRequired:
        await msg.reply('Я буду дуже радий, якщо мені видадуть права адмнітсратора, щоб я зміг виконати цю команду 😅')
        return
    except MethodIsNotAvailable:
        await msg.reply('👮 Ця команда доступна лише для груп з 2+ адміністраторами')
        return
    except MethodNotAvailableInPrivateChats:
        await msg.reply('😳 Я не знаю як вам вдалося використати цю команду у приватних повідомленнях, але такого робити неможна')
        return
    except CantDemoteChatCreator:
        await msg.reply('Мені дуже шкода, але, на жаль, я не можу робити будь-які дії з власником чату\nУ мене немає прав... 😝')
        return
    except CantRestrictSelf:
        await msg.reply('🤔 Хм, накласти обмеження на власника чату...\nЩось новеньке..')
        return
    except NotEnoughRightsToRestrict:
        await msg.reply('🤭 У мене немає достатньо прав щоб обмежити цього користувача')
        return
    except Exception as e:
        # e = translator.translate(str(e))
        logging.error(f'While random muting the user an error occurred: {e}')
        return
    new_msg = await msg.answer(f'Ви виграли мут на {rand_time}хв.\nЦе повідомлення видалиться секунд через 5.')
    if random.randint(0, 3) == 1:
        rand_time2 = random.randint(5, 25)
        await sleep(rand_time2)
        await new_msg.delete()
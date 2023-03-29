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

import html

import datetime

from functions import restrict_command_processors as cmd_proc_func
from functions.reply_checker import check_for_reply as is_reply
from functions.check_permission import check_permission

@dp.message_handler(commands=['mute', 'мут', 'заглушити'], commands_prefix="!.", chat_type=["group", "supergroup"], is_admin=True)
async def mute(msg: types.Message):
    if not await is_reply(msg):
        return
    if not await check_permission(msg):
        return
    until_date = await cmd_proc_func.restrict_command_processor(msg)
    if not until_date:
        return
    try:
        await bot.restrict_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=until_date)
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
        await msg.reply('🤔 Хм, накласти обмеження на власника чату...\nЩось новеньке..')
        return
    except CantRestrictSelf:
        await msg.reply('Сам себе обмежити я не зможу, доведеться зробити це власноруч\n¯\_(ツ)_/¯')
        return
    except NotEnoughRightsToRestrict:
        await msg.reply('🤭 У мене немає достатньо прав щоб обмежити цього користувача')
        return
    except Exception as e:
        # e = translator.translate(str(e))
        logging.error(f'While muting the user an error occurred: {e}')
        return
    if until_date.seconds == 1:
        await msg.answer(f'Користувачеві <a href="tg://user?id={msg.reply_to_message.from_user.id}">{html.escape(msg.reply_to_message.from_user.full_name)}</a> заборонено надсилати повідомлення назавжди')
        return
    await msg.answer(f'Користувачеві <a href="tg://user?id={msg.reply_to_message.from_user.id}">{html.escape(msg.reply_to_message.from_user.full_name)}</a> заборонено надсилати повідомлення до {(datetime.datetime.now() + until_date).strftime("%m/%d/%Y, %H:%M")}')
from aiogram import types
from loader import bot, dp, logging

import html

from aiogram.utils.exceptions import (
    ChatAdminRequired, 
    MethodNotAvailableInPrivateChats, 
    CantDemoteChatCreator,
    CantRestrictSelf, 
    NotEnoughRightsToRestrict,
    MethodIsNotAvailable
)

from functions.reply_checker import check_for_reply as is_reply

@dp.message_handler(commands=['unmute', 'unban', 'pardon', 'пардон', 'розбан'], chat_type=["group", "supergroup"], commands_prefix='!.', is_admin=True)
async def unmute(msg: types.Message):
    if not await is_reply(msg):
        return
    member = await bot.get_chat_member(chat_id=msg.chat.id, user_id=msg.reply_to_message.from_user.id)
    if not member.status in ['restricted', 'kicked', 'left']:
        return
    try:
        await bot.restrict_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True, True, True, True, True, True, True, True))
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
        logging.error(f'While blocking the user an error occurred: {e}')
        return
    await msg.answer(f'З користувача <a href="tg://user?id={msg.reply_to_message.from_user.id}">{html.escape(msg.reply_to_message.from_user.full_name)}</a> знято усі обмеження!')
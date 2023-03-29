from aiogram import types
from aiogram.types import ChatMember
from loader import bot, dp, translator
import html

from functions import promote

from functions.reply_checker import check_for_reply as is_reply

from aiogram.utils.exceptions import (
    ChatAdminRequired, 
    MethodNotAvailableInPrivateChats, 
    CantDemoteChatCreator,
    CantRestrictSelf, 
    NotEnoughRightsToRestrict,
    MethodIsNotAvailable
)

@dp.message_handler(commands=['promote'], commands_prefix='!.', chat_type=["group", "supergroup"], is_admin=True)
async def promote_someone(msg: types.Message):
    if not await is_reply(msg):
        return
    role = msg.text.split(' ', maxsplit=1)[1]
    if role == 'admin':
        await promote.admin(msg)
    elif role == 'high moder':
        await promote.high_moder(msg)
    elif role == 'moder':
        await promote.moder(msg)
    else:
        await msg.reply(text='Будь-ласка, напиши одну команду з:\n<code>!promote admin</code>\n<code>!promote high moder</code>\n<code>!promote moder</code>')

@dp.message_handler(commands=['demote', 'попустити'], commands_prefix='!.', chat_type=["group", "supergroup"], is_admin=True)
async def promote_someone(msg: types.Message):
    if not await is_reply(msg):
        return
    try:
        await bot.promote_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            can_manage_chat=False, 
            can_change_info=False, 
            can_delete_messages=False, 
            can_invite_users=False, 
            can_restrict_members=False, 
            can_pin_messages=False, 
            can_manage_video_chats=False, 
            can_promote_members=False, 
            can_manage_topics=False, 
            can_manage_voice_chats=False,
            is_anonymous=False
        )
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
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        return
    await msg.answer(f'[-] Користувача <code>{html.escape(msg.reply_to_message.from_user.full_name)}</code> видалено з адміністраторів')
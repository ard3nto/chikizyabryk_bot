from aiogram import types
from loader import bot, translator

import html

from aiogram.utils.exceptions import (
    ChatAdminRequired, 
    MethodNotAvailableInPrivateChats, 
    CantDemoteChatCreator,
    CantRestrictSelf, 
    NotEnoughRightsToRestrict,
    MethodIsNotAvailable
)

async def admin(msg: types.Message):
    try:
        await bot.promote_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            can_manage_chat=True, 
            can_change_info=True, 
            can_delete_messages=True, 
            can_invite_users=True, 
            can_restrict_members=True, 
            can_pin_messages=True, 
            can_promote_members=True, 
            can_manage_video_chats=True
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
    await msg.answer(f'[+] Користувача <code>{html.escape(msg.reply_to_message.from_user.full_name)}</code> призначено адміністратором')

async def high_moder(msg: types.Message):
    try:
        await bot.promote_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            can_manage_chat=True, 
            can_change_info=True, 
            can_delete_messages=True, 
            can_invite_users=True, 
            can_restrict_members=True, 
            can_pin_messages=True, 
            can_manage_video_chats=True, 
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
    await msg.answer(f'[+] Користувача <code>{html.escape(msg.reply_to_message.from_user.full_name)}</code> призначено старшим модератором')

async def moder(msg: types.Message):
    try:
        await bot.promote_chat_member(
            chat_id=msg.chat.id, 
            user_id=msg.reply_to_message.from_user.id, 
            can_delete_messages=True, 
            can_restrict_members=True, 
            can_pin_messages=True, 
            can_manage_video_chats=True, 
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
    await msg.answer(f'[+] Користувача <code>{html.escape(msg.reply_to_message.from_user.full_name)}</code> призначено модератором')
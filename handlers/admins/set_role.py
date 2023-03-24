from aiogram import types
from loader import bot, dp, logging, translator

import html

from aiogram.utils.exceptions import (
    ChatAdminRequired, 
    MethodNotAvailableInPrivateChats, 
    MethodIsNotAvailable, 
    BadRequest
)

from functions.reply_checker import check_for_reply as is_reply

@dp.message_handler(commands=['set_role'], commands_prefix='!', chat_type=["group", "supergroup"], is_chat_admin=True, custom_title=True)
async def set_someone(msg: types.Message):
    if not await is_reply(msg):
        return
    role = msg.text.split(' ', maxsplit=1)[1]
    member = await bot.get_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
    if member.status not in ["creator", "administrator"]:
        try:
            await bot.promote_chat_member(
                chat_id=msg.chat.id, 
                user_id=msg.reply_to_message.from_user.id, 
                can_manage_chat=True
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
        except Exception as e:
            # e = translator.translate(str(e))
            logging.error(f'While promoting the user (!set_role) an error occurred: {e}')
            return
    try:
        await bot.set_chat_administrator_custom_title(chat_id=msg.chat.id, user_id=msg.reply_to_message.from_user.id, custom_title=role)
    except ChatAdminRequired:
        await msg.reply('Я буду дуже радий, якщо мені видадуть права адмнітсратора, щоб я зміг виконати цю команду 😅')
        return
    except MethodIsNotAvailable:
        await msg.reply('👮 Ця команда доступна лише для груп з 2+ адміністраторами')
        return
    except MethodNotAvailableInPrivateChats:
        await msg.reply('😳 Я не знаю як вам вдалося використати цю команду у приватних повідомленнях, але такого робити неможна')
        return
    except BadRequest as e:
        e = translator.translate(str(e))
        await msg.reply(e)
        return
    except Exception as e:
        # e = translator.translate(str(e))
        logging.error(f'While setting custom title for the user an error occurred: {e}')
        return
    await msg.answer(f'💬 Користувачу <code>{html.escape(msg.reply_to_message.from_user.full_name)}</code> встановлено роль [{role}]')
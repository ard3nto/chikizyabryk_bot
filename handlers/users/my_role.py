from aiogram import types
from loader import bot, dp, logging, translator

import html

from aiogram.utils.exceptions import (
    ChatAdminRequired, 
    MethodNotAvailableInPrivateChats, 
    CantDemoteChatCreator,
    CantRestrictSelf, 
    NotEnoughRightsToRestrict,
    MethodIsNotAvailable,
    BadRequest
)

@dp.message_handler(commands=['my_role'], commands_prefix='!', chat_type=["group", "supergroup"], custom_title=True)
async def set_my(msg: types.Message):
    role = msg.text.split(' ', maxsplit=1)[1]
    member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if member.status not in ["creator", "administrator"]:
        try:
            await bot.promote_chat_member(
                chat_id=msg.chat.id, 
                user_id=msg.from_user.id, 
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
            logging.error(f'While promoting the user (!my_role) an error occurred: {e}')
            return
    try:
        await bot.set_chat_administrator_custom_title(chat_id=msg.chat.id, user_id=msg.from_user.id, custom_title=role)
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
    except BadRequest as e:
        e = translator.translate(str(e))
        await msg.reply(e)
        return
    except Exception as e:
        e = translator.translate(str(e))
        logging.error(f'While setting custom title for the user an error occurred: {e}')
        return
    await msg.answer(f'💬 Користувачу <code>{html.escape(msg.from_user.full_name)}</code> встановлено роль [{role}]')
import aiogram
from aiogram import types
from datetime import datetime, timedelta

from loader import bot, dp, scheduler, translator

async def unpin_message(chat_id: int, message_id: int):
    try:
        await bot.unpin_chat_message(chat_id=chat_id, message_id=message_id)
    except:
        return

@dp.message_handler(text_startswith=['закреп ', 'закріпити ', 'пін '])
async def pin_message_handler(msg: types.Message):
    if not msg.reply_to_message:
        return
    user = await bot.get_chat_member(chat_id=msg.chat.id, user_id=msg.from_user.id)
    if not user.can_pin_messages:
        return
    args = msg.text.replace('на ', '').split()
    if not args[1].isdigit():
        return
    if args[2].lower().startswith('сек'):
        time = timedelta(seconds=int(args[1]))
    elif args[2].lower().startswith('хв'):
        time = timedelta(minutes=int(args[1]))
    elif args[2].lower().startswith('год'):
        time = timedelta(hours=int(args[1]))
    elif args[2].lower().startswith(('дн', 'ден')):
        time = timedelta(days=int(args[1]))
    else:
        return
    if time.days > 365:
        return
    disable_notification = False
    if len(args) > 3:
        if args[3] == '-':
            disable_notification = True
    text_time = f'{args[1]} {args[2]}'
    # Pin the message
    try:
        pinned_message = await msg.reply_to_message.pin(disable_notification)
    except Exception as e:
        e = translator.translate(e)
        await msg.reply(f'🫣 <b>Виникла помилка:</b> <code>{e}</code>')
    await msg.reply_to_message.reply(f'📌 | Повідомлення успішно закріплено на {text_time}')
    # Schedule message unpinning
    scheduler.add_job(unpin_message, 'date', run_date=(datetime.now() + time), args=[msg.chat.id, msg.reply_to_message.message_id])
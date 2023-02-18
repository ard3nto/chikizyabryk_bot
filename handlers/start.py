from aiogram import types
from loader import dp, logging, bot

from aiogram.utils.exceptions import RetryAfter

timemarks = '<code>m</code> - Для хвилин\n<code>h</code> - Для годин\n<code>d</code> - Для днів'

start_msg = f'''👋 Привіт!

💬 Я - бот модератор з мінімальним функціоналом створений для максимальної зручності

👌 Жодних налаштувань, просто додай мене до групи як адміністратора і використовуй доступні команди (обов\'язково відповіддю на повідомлення)

📎 Ось перелік основних команд:
• <code>!mute</code> - забороняє користувачу надсилати повідомлення
• <code>!ban</code> - блокує і видаляє користувача з групи
• <code>!pardon</code> - знімає усі обмеження з користувача
• <code>!media</code> - забороняє користувачу надсилати медіа

⏰ Ти також можеш встановити обмеження на певний час, напрклад 30хв:
• <code>!mute 30m</code>
  ।  30 - будь-яке число
  ↳ m - часова позначка

📌 Доступні такі часові позначки:

{timemarks}

👀 Повний список команд дивися <a href="https://telegra.ph/CH%D1%96k%D1%96zyabrik--Komandi-02-01">тут</a>'''

@dp.errors_handler(exception=RetryAfter)
async def handling_an_error(update, error):
    return True

@dp.message_handler(commands=['start'], commands_prefix="/", chat_type=["private"])
async def start_cmd(msg: types.Message):
    print(msg.get_args())
    await msg.answer(start_msg, disable_web_page_preview=True)
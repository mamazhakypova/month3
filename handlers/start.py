from aiogram import types, Dispatcher
from config import bot

async def start_button(massage: types.Message):
    print(massage)

    await bot.send_message(
        chat_id=massage.from_user.id,
        text=f'Hello {massage.from_user.first_name}'
    )



def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )
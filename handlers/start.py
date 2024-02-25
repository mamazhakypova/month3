from aiogram import types, Dispatcher
from config import bot
from database import bot_db
from keyboards import inline_buttons
import const

async def start_button(massage: types.Message):
    print(massage)
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=massage.from_user.id,
        username=massage.from_user.username,
        first_name=massage.from_user.first_name,
        last_name=massage.from_user.last_name
        )

    await bot.send_message(
        chat_id=massage.from_user.id,
        text=const.START_MENU_TEXT.format(
            user=massage.from_user.first_name
        ),
        reply_markup=await inline_buttons.start_keyboard()
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )
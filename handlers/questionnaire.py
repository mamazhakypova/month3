from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_keyboard

async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='а и б',
        reply_markup=await questionnaire_keyboard()
    )

async def first_card(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='You are ONE 👑',
    )

async def second_card(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='You are TWO 🦊',
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_message_handler(
        questionnaire_start,
        lambda call: call.data == 'start_questionnaire'
    )
    dp.register_callback_query_handler(first_card,
                                       lambda call: call.data == 'first')
    dp.register_callback_query_handler(second_card,
                                       lambda call: call.data == 'second')

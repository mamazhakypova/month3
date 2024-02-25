from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_keyboard

async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='а и б',
        reply_markup=await questionnaire_keyboard()
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_message_handler(
        questionnaire_start,
        lambda call: call.data == 'start_questionnaire'
    )
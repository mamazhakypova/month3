from aiogram.types import (
InlineKeyboardButton,
InlineKeyboardMarkup
)

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        'Questionnaire',
        callback_data='start_questionnaire'
    )
    markup.add(questionnaire_button)
    return markup

async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    first_button = InlineKeyboardButton(
        'ONE',
        callback_data='first'
    )
    second_button = InlineKeyboardButton(
        'TWO',
        callback_data='second'
    )
    markup.add(first_button)
    markup.add(second_button)
    return markup
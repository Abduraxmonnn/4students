# Python
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Project
from telegram_bot.messages.button_message import ButtonMessages

button_message = ButtonMessages()

is_anonymous_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=button_message.yes_anonymous_message()),
        KeyboardButton(text=button_message.no_anonymous_message()),
    ],
], resize_keyboard=True, one_time_keyboard=True)

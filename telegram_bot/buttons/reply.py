# Python
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Project
from telegram_bot.messages.button_message import ButtonMessages
from main.models import Faculty

button_message = ButtonMessages()

is_anonymous_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=button_message.yes_anonymous_message()),
        KeyboardButton(text=button_message.no_anonymous_message()),
    ],
], resize_keyboard=True, one_time_keyboard=True)

# Fetch all faculty names
faculty_names = [item.name for item in Faculty.objects.all()]

# Create the keyboard with buttons for each faculty name
faculties_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=faculty_names[i + j]) for j in range(3) if i + j < len(faculty_names)]
        for i in range(0, len(faculty_names), 3)
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Fetch all faculty names
faculty_short_names = [item.short_name for item in Faculty.objects.all()]

# Create the keyboard with buttons for each faculty name
faculties_shorts_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=faculty_short_names[i + j]) for j in range(3) if i + j < len(faculty_short_names)]
        for i in range(0, len(faculty_short_names), 3)
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

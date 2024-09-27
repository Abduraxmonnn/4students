# Python
from time import sleep

# Aiogram
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Project
from telegram_bot.messages import ChatMessages

chat_message = ChatMessages()

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    try:
        msg = [chat_message.hello_message(message.from_user.username), chat_message.ask_upload_file_message()]
        for i in msg:
            await message.answer(i)
            sleep(1)
    except RuntimeError as e:
        print(f"Error creating user: {e}")
        await message.answer("There was an error creating your account.")

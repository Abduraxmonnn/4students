# Python
import asyncio

# Aiogram
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Project
from telegram_bot.messages import ChatMessages
from telegram_bot.orm.user import create_user

chat_message = ChatMessages()

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    try:
        user = await create_user(user_id=message.from_user.id, username=message.from_user.username,
                                 first_name=message.from_user.first_name)
        if user:
            msg = [
                chat_message.hello_message(message.from_user.username),
                chat_message.ask_upload_file_message()
            ]
            for i in msg:
                await message.answer(i)
                await asyncio.sleep(1)
        else:
            await message.answer("There was an error starting BOT.")
    except RuntimeError as e:
        print(f"Error creating user: {e}")
        await message.answer("There was an error creating your account.")

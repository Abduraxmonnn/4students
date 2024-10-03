# Python
import asyncio

# Aiogram
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Project
from telegram_bot.messages import ChatMessages
from telegram_bot.orm.user import create_user
from telegram_bot.images.image_ids import hello_banner

chat_message = ChatMessages()

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    try:
        user = await create_user(user_id=message.from_user.id, username=message.from_user.username,
                                 first_name=message.from_user.first_name)
        if user:
            await message.answer_photo(photo=hello_banner,
                                       caption=chat_message.hello_message(message.from_user.username))

            await asyncio.sleep(1 / 2)
            await message.answer(chat_message.ask_upload_file_message())
        else:
            await message.answer("There was an error starting BOT.")
    except RuntimeError as e:
        print(f"Error creating user: {e}")
        await message.answer("There was an error creating your account.")

# Aiogram
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Project
from telegram_bot.messages.chat_message import ChatMessages

chat_message = ChatMessages()
router = Router()


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(chat_message.help_message())

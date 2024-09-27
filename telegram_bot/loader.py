# Python
import os
from dotenv import load_dotenv

# Aiogram
from aiogram import Bot, Dispatcher, types

# Project
from telegram_bot.handlers import start_handler

load_dotenv()

TOKEN = os.getenv("TOKEN")

# Global bot and dispatcher
bot = None
dp = None


async def main():
    global bot, dp
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start_handler.router)

    bot_commands = [
        types.BotCommand(command="/start", description="Start bot for subscribe"),
        types.BotCommand(command="/help", description="Get info about bot"),
        types.BotCommand(command="/me", description="Information about User"),
    ]

    await bot.set_my_commands(bot_commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def start_bot():
    await main()

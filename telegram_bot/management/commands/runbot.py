import os
import asyncio
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

from telegram_bot.loader import start_bot

load_dotenv()

TOKEN = os.getenv("TOKEN")


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        # Create an event loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())

    async def run(self):
        await start_bot()

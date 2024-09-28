# Project
from asgiref.sync import sync_to_async, async_to_sync

from telegram_bot.models import TGUser


@sync_to_async
def create_user(user_id: int, username: str, first_name: str) -> TGUser | None:
    user, created = TGUser.objects.get_or_create(
        user_id=user_id,
        defaults={
            'username': username,
            'first_name': first_name
        }
    )
    return user

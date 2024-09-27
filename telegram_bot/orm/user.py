# Project
from asgiref.sync import sync_to_async

from telegram_bot.models import TGUser


@sync_to_async
def create_user(user_id: int, username: str, first_name: str) -> TGUser | None:
    try:
        new_user = TGUser(user_id=user_id, username=username, first_name=first_name)
        new_user.save()  # Save the user synchronously
        return new_user
    except Exception as e:
        print(e)
        return None

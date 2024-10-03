# Python
from asgiref.sync import sync_to_async, async_to_sync

# Project
from main.models import FeedBack
from telegram_bot.models import TGUser


@sync_to_async
def create_feedback(subject: str, message: str, user_id: int) -> FeedBack | None:
    user = TGUser.objects.get(user_id=user_id)

    feedback = FeedBack.objects.create(
        subject=subject,
        message=message,
        owner=user,
    ).save()
    return feedback

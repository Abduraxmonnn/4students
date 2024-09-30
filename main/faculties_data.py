# Project
from asgiref.sync import sync_to_async, async_to_sync

from main.models import Faculty


@sync_to_async
def get_faculty_name(short_name: str, faculty: str) -> dict:
    result = {}

    for item in Faculty.objects.filter(name=faculty, short_name=short_name):
        result = {
            "direction": item.direction,
            "faculty": item.name,
        }

    return result


@sync_to_async
def check_faculty_correction(short_name: str, faculty: str) -> bool:
    check_faculty = Faculty.objects.filter(name=faculty, short_name=short_name)

    if check_faculty.exists():
        return True

    return False

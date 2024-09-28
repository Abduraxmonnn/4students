# Python
import os
from asgiref.sync import sync_to_async

from main.faculties_data import get_faculty_name
from main.models import Faculty, Subject, Answer
from telegram_bot.models import TGUser


@sync_to_async
def get_or_create_faculty(direction, name, short_name):
    return Faculty.objects.get_or_create(
        direction=direction,
        name=name,
        short_name=short_name,
    )


@sync_to_async
def get_or_create_subject(name, faculty):
    return Subject.objects.get_or_create(
        name=name,
        faculty=faculty,
    )


@sync_to_async
def get_or_create_user(user_id, username, first_name):
    return TGUser.objects.get_or_create(
        user_id=user_id,
        username=username,
        first_name=first_name,
    )


@sync_to_async
def create_answer_in_db(subject, file, file_name, file_type, user, is_anonymous, year, semester, pages, answers):
    answer = Answer.objects.create(
        subject=subject,
        file=file,
        file_name=file_name,
        file_type=file_type,
        by=user,
        is_anonymous=is_anonymous,
        year=year,
        semester=semester,
        pages=pages,
        answers=answers
    )
    return answer


async def create_answer(
        file,  # This should be a ContentFile
        faculty: str,
        short_name: str,
        subject: str,
        year: int,
        semester: int,
        is_anonymous: bool,
        uploaded_by,
        pages: int,
        answers: int
):
    direction_faculty = await get_faculty_name(short_name=short_name, obj=Faculty)

    faculty_obj, created_faculty = await get_or_create_faculty(
        direction=direction_faculty['direction'],
        name=direction_faculty['faculty'],
        short_name=short_name
    )

    subject_obj, created_subject = await get_or_create_subject(
        name=subject,
        faculty=faculty_obj
    )

    user_obj, created_user = await get_or_create_user(
        user_id=uploaded_by.id,
        username=uploaded_by.username,
        first_name=uploaded_by.first_name
    )

    # Use the name attribute of the ContentFile
    file_name = file.name  # Get the file name from ContentFile
    file_type = os.path.splitext(file_name)[1][1:]  # Get file extension
    await create_answer_in_db(
        subject=subject_obj,
        file=file,
        file_name=file_name,
        file_type=file_type,
        user=user_obj,
        is_anonymous=is_anonymous,
        year=year,
        semester=semester,
        pages=pages,
        answers=answers
    )
    return

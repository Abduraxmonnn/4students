# Python
import os
import requests

# Django
from django.core.files.base import ContentFile

# Aiogram
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# Project
from telegram_bot.buttons import reply as btn
from telegram_bot.orm.answer import create_answer
from telegram_bot.states.upload_file_state import UploadFileStates
from telegram_bot.messages import ChatMessages, ButtonMessages
from main.faculties_data import check_faculty_correction

chat_message = ChatMessages()
btn_message = ButtonMessages()

router = Router()


@router.message(F.document)
async def get_file(message: Message, state: FSMContext):
    if message.document:
        await state.update_data(file=message.document)
        await state.set_state(UploadFileStates.faculty)
        await message.answer(chat_message.ask_faculty_message(), reply_markup=btn.faculties_btn)
    else:
        await message.answer("Please upload a valid document.")


@router.message(UploadFileStates.faculty)
async def get_faculty(message: Message, state: FSMContext):
    await state.update_data(faculty=message.text)
    await state.set_state(UploadFileStates.short_name)
    await message.answer(chat_message.ask_short_name_message())


@router.message(UploadFileStates.short_name)
async def get_faculty(message: Message, state: FSMContext):
    data = await state.get_data()

    if await check_faculty_correction(short_name=message.text.upper(), faculty=data['faculty']):
        await state.update_data(short_name=message.text)
        await state.set_state(UploadFileStates.subject)
        await message.answer(chat_message.ask_subject_message())
    else:
        await message.answer(chat_message.invalid_short_name_message())


@router.message(UploadFileStates.subject)
async def get_subject(message: Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await state.set_state(UploadFileStates.year)
    await message.answer(chat_message.ask_year_message())


@router.message(UploadFileStates.year)
async def get_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(UploadFileStates.semester)
    await message.answer(chat_message.ask_semester_message())


@router.message(UploadFileStates.semester)
async def get_semester(message: Message, state: FSMContext):
    await state.update_data(semester=message.text)
    await state.set_state(UploadFileStates.is_anonymous)
    await message.answer(chat_message.ask_is_anonymous_message(), reply_markup=btn.is_anonymous_btn)


@router.message(UploadFileStates.is_anonymous)
async def get_anonymous(message: Message, state: FSMContext):
    if message.text.lower() == btn_message.yes_anonymous_message().lower():
        await state.update_data(is_anonymous=True)
        await state.update_data(by=message.from_user.id)
    else:
        await state.update_data(is_anonymous=False)
        await state.update_data(by=message.from_user.id)

    data = await state.get_data()
    file = data['file']

    # Step 1: Download the file
    file_info = await message.bot.get_file(file.file_id)
    file_path = file_info.file_path
    file_url = f"https://api.telegram.org/file/bot{message.bot.token}/{file_path}"

    # Step 2: Fetch the file content
    response = requests.get(file_url)
    if response.status_code == 200:
        file_name = os.path.basename(file_url)

        content_file = ContentFile(response.content, name=file_name)

        await create_answer(
            faculty=str(data['faculty']).upper(),
            file=content_file,
            short_name=str(data['short_name']).upper(),
            subject=str(data['subject']).upper(),
            year=data['year'],
            semester=data['semester'],
            is_anonymous=data['is_anonymous'],
            uploaded_by=message.from_user,
            pages=1000,
            answers=100
        )
    await state.clear()
    await message.answer(chat_message.answer_uploaded_message())

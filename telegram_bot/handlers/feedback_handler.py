# Aiogram
import asyncio

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# Project
from telegram_bot.messages.chat_message import ChatMessages
from telegram_bot.orm.feedback import create_feedback
from telegram_bot.states.base_state import FeedbackStates

chat_message = ChatMessages()
router = Router()


@router.message(Command("feedback"))
async def feedback_command(message: Message, state: FSMContext):
    await state.set_state(FeedbackStates.subject)
    msg = [
        chat_message.feedback_message(),
        chat_message.feedback_subject_message()
    ]
    for i in msg:
        await message.answer(i)
        await asyncio.sleep(1/2)


@router.message(FeedbackStates.subject)
async def saving_feedback(message: Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await state.set_state(FeedbackStates.text)
    await message.answer(chat_message.feedback_text_message())


@router.message(FeedbackStates.text)
async def saving_feedback(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await create_feedback(subject=data['subject'], message=data['text'], user_id=message.from_user.id)
    await state.clear()
    await message.answer(chat_message.thanks_feedback_message())

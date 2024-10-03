# Aiogram
from aiogram.fsm.state import State, StatesGroup


class UploadFileStates(StatesGroup):
    file = State()
    faculty = State()
    short_name = State()
    subject = State()
    year = State()
    semester = State()
    page = State()
    answer_count = State()
    is_anonymous = State()
    by = State()


class FeedbackStates(StatesGroup):
    subject = State()
    text = State()

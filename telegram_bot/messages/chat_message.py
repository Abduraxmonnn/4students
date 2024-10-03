class ChatMessages:
    def __init__(self, language: str = 'ru'):
        self.language = language
        self.message = None

    def hello_message(self, username: str) -> str:
        self.message = {
            'uz': f'{username} Xush kelibsiz 😊!\n\nFayllarni yuborish ketma-ketligi o\'rganib chiqish uchun /help',
            'ru': f'{username} Добро пожаловать 😊!\n\nУзнать правила отправки файлов /help',
            'en': f'{username} Welcome 😊!\n\nLearn the rules for sending files /help'
        }
        return self.message[self.language]

    def ask_upload_file_message(self) -> str:
        self.message = {
            'uz': 'Iltimos Javoblarga ega faylni yuklang.',
            'ru': 'Загрузите, пожалуйста, файл с ответами.',
            'en': 'Please upload the file with answers.'
        }
        return self.message[self.language]

    def ask_faculty_message(self) -> str:
        self.message = {
            'uz': 'Fakultetni kiriting',
            'ru': 'Введите факультет',
            'en': 'Enter the faculty'
        }
        return self.message[self.language]

    def ask_short_name_message(self) -> str:
        self.message = {
            'uz': 'Fakultetning qisqartmasinni kiriting. masalan: BAN, ACC, ISE ...',
            'ru': 'Введите аббревиатуру факультета, например: BAN, ACC, ISE ...',
            'en': 'Enter the Faculty Abbreviation. for example: BAN, ACC, ISE ...'
        }
        return self.message[self.language]

    def invalid_short_name_message(self) -> str:
        self.message = {
            'uz': 'Fakultet qisqartmasi yaroqsiz. Iltimos, tekshiring va qayta urinib ko\'ring',
            'ru': 'Неверная аббревиатура факультета. Проверьте и попробуйте еще раз',
            'en': 'Invalid Faculty Abbreviation. Please check and again try'
        }
        return self.message[self.language]

    def ask_subject_message(self) -> str:
        self.message = {
            'uz': 'Fani kiriting',
            'ru': 'Введите предмета',
            'en': 'Enter the subject'
        }
        return self.message[self.language]

    def ask_year_message(self) -> str:
        self.message = {
            'uz': 'Fani o\'qitilgan yilni kiriting',
            'ru': 'Введите год преподавания предмета',
            'en': 'Enter the year the subject was studied'
        }
        return self.message[self.language]

    def ask_semester_message(self) -> str:
        self.message = {
            'uz': 'Fani o\'qitilgan semester kiriting',
            'ru': 'Введите семестр преподавания предмета',
            'en': 'Enter the semester the subject was studied'
        }
        return self.message[self.language]

    def ask_page_message(self) -> str:
        self.message = {
            'uz': 'Yuklangan fayl nechi betli',
            'ru': 'Сколько страниц имеет загруженный файл',
            'en': 'How many pages does the uploaded file have'
        }
        return self.message[self.language]

    def ask_answer_count_message(self) -> str:
        self.message = {
            'uz': 'Yuklangan fayl nechta javoblarni o\'z ichiga oladi',
            'ru': 'сколько ответов содержит загруженный файл',
            'en': 'how many answers does the uploaded file contain'
        }
        return self.message[self.language]

    def ask_is_anonymous_message(self) -> str:
        self.message = {
            'uz': 'Gruppaga file egasi ko\'rsatishga rozimisiz',
            'ru': 'Вы соглашаетесь показать группе владельца файла',
            'en': 'You agree to show the owner of the file to the group'
        }
        return self.message[self.language]

    def answer_uploaded_message(self) -> str:
        self.message = {
            'uz': 'Sizning javobingiz qabul qilindi. Tez orada guruhga yuklanadi',
            'ru': 'Ваш ответ принят. Скоро он будет загружен в группу',
            'en': 'Your reply has been accepted. It will be uploaded to the group soon.'
        }
        return self.message[self.language]

    def feedback_subject_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, feedback mavzusini kiriting',
            'ru': 'Пожалуйста, введите тему отзыва',
            'en': 'Please, enter the subject of feedback'
        }
        return self.message[self.language]

    def feedback_text_message(self) -> str:
        self.message = {
            'uz': 'Iltimos, feedback xabarini kiriting',
            'ru': 'Пожалуйста, введите сообщение обратной связи',
            'en': 'Please, enter the message of feedback'
        }
        return self.message[self.language]

    def thanks_feedback_message(self) -> str:
        self.message = {
            'uz': 'Qo\'llab-quvvatlaganingiz uchun tashakkur, loyihani yaxshilash bo\'yicha ishingizni qadrlaymiz',
            'ru': 'Спасибо за вашу поддержку, мы ценим вашу работу по улучшению проекта.',
            'en': 'Thank you for your support, we appreciate your work to improve the project'
        }
        return self.message[self.language]

    def feedback_message(self) -> str:
        self.message = {
            'uz': """Biz har doim botimizni yaxshilash va uni sizlar uchun foydaliroq qilishga intilamiz. Iltimos, o'z takliflaringiz, fikrlaringiz yoki yaxshilash bo'yicha g'oyalaringizni qoldiring.

Sizning fikringiz biz uchun juda muhim, va biz albatta uni inobatga olamiz. Hissa qo'shganingiz uchun rahmat!""",
            'ru': """Мы всегда стремимся улучшить наш бот и сделать его более полезным для вас. Пожалуйста, оставьте свои предложения, замечания или идеи по улучшению.

Ваше мнение очень важно для нас, и мы обязательно его рассмотрим. Спасибо за ваш вклад!""",
            'en': """We always strive to improve our bot and make it more useful for you. Please leave your suggestions, comments, or ideas for improvement.

Your feedback is very important to us, and we will definitely take it into account. Thank you for your contribution!"""
        }
        return self.message[self.language]

    def help_message(self) -> str:
        self.message = {
            'uz': """Assalomu Aleykom, hurmatli talaba va foydalanuvchilar. Bu bot KIUT (Kimyo International University in Tashkent) da tahsil oluvchi talabar qayta topshirish (retake) imtihonlariga yengilik yaratish maqsadida ish yuritadi.

Bot dan foydalanish tarting:

1. Javoblarga ega fayl yuklaysiz.
2. Bot sizdan so’ragan qo’shimcha ma’lumotlarga jovob berasiz.
3. Bot javobni qabul qilgach gruppaga yuklash bosqichga o’tadi.

Bot rivojlanishga o’z hisnagizni qo’shing:

1. /feedback buyruq foydalanib o’z fikiringizni qoldirib. Admin albatta o’qib chiqadi.

Qo’shimcha sovolaringiz bolsa gruppa qolganlardan so’rab olshingiz mumkin yoki Admin kirib jovob berishini kuting.

Etiboringiz uchun rahmat.""",
            'ru': """Ассалому Алейкум, уважаемые студенты и пользователи. Этот бот работает с целью создания нововведений для студентов, сдающих пересдачу (ретейк) экзаменов в KIUT (Международный университет химии в Ташкенте).

Правила использования бота:

1. Вы загружаете файл с ответами.
2. Вы отвечаете на дополнительные вопросы, которые задаст бот.
3. После того, как бот примет ответ, он перейдет к этапу загрузки в группу.

Ваши идеи по улучшению бота:

1. Оставьте свое мнение, используя команду /feedback. Администратор обязательно прочитает его.

Если у вас есть дополнительные вопросы, вы можете спросить других в группе или дождаться ответа от администратора.

Спасибо за ваше внимание.""",
            'en': """Hello, dear students and users. This bot operates with the aim of innovating the retake exams for students at KIUT (Kimyo International University in Tashkent).

How to use the bot:

1. You upload a file with the answers.
2. You respond to the additional information the bot asks for.
3. Once the bot accepts your answer, it moves on to the upload stage for the group.

Contribute to the bot's development:

1. Use the /feedback command to leave your thoughts. The admin will definitely read it.

If you have additional questions, you can ask others in the group or wait for the admin to respond.

Thank you for your attention."""
        }
        return self.message[self.language]

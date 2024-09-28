class ChatMessages:
    def __init__(self, language: str = 'ru'):
        self.language = language
        self.message = None

    def hello_message(self, username: str) -> str:
        self.message = {
            'uz': f'{username} Xush kelibsiz 😊!\n\nIltimos, fayllarni yuborish qoidalarini qayta o\'qib chiqin.',
            'ru': f'{username} Добро пожаловать 😊!\n\nПожалуйста, перечитайте правила подачи файлов.',
            'en': f'{username} Welcome 😊!\n\nPlease reread the rules for submitting files.'
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

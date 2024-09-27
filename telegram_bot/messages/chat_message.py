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

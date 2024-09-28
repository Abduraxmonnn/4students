class ButtonMessages:
    def __init__(self, language: str = 'ru'):
        self.language = language
        self.message = None

    def yes_anonymous_message(self) -> str:
        self.message = {
            'uz': 'Roziman',
            'ru': 'Согласен',
            'en': 'Agree'
        }
        return self.message[self.language]

    def no_anonymous_message(self) -> str:
        self.message = {
            'uz': 'Rozi emasman',
            'ru': 'Не согласен',
            'en': 'Not agree'
        }
        return self.message[self.language]

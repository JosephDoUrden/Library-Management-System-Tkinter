import json

class LanguageManager:
    def __init__(self, language_code="en"):
        self.language_code = language_code
        self.load_language()

    def load_language(self):
        try:
            with open(f"lang/{self.language_code}.json", "r", encoding="utf-8") as file:
                self.language_data = json.load(file)
        except FileNotFoundError:
            print(f"Language file not found: {self.language_code}.json")
            self.language_data = {}

    def change_language(self, language_code):
        self.language_code = language_code
        self.load_language()

import tkinter as tk
from screens.login_screen import LoginScreen
from components.centerscreen import center_screen_geometry

class LibraryManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        # Set the window to center of the screen
        self.geometry(center_screen_geometry(
            screen_width=self.winfo_screenwidth(), 
            screen_height=self.winfo_screenheight(), 
            win_width=800, 
            win_height=600
            ))

        # Dil seçeneği (varsayılan İngilizce)
        self.language = "en"
        
        # Dil seçeneğini yükle
        self.load_language()

        # Başlangıç ekranı
        self.login_screen = LoginScreen(self)
        self.login_screen.pack(expand=True, fill="both")

    def load_language(self):
        # Dil dosyasını yükle
        try:
            with open(f"lang/{self.language}.json", "r", encoding="utf-8") as file:
                self.language_data = json.load(file)
        except FileNotFoundError:
            print(f"Language file not found: {self.language}.json")
            self.language_data = {}

    def change_language(self, language_code):
        self.language = language_code
        self.load_language()

if __name__ == "__main__":
    app = LibraryManagementApp()
    app.mainloop()

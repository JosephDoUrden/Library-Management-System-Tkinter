import tkinter as tk
from utils.language import LanguageManager 
from tkinter import ttk

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.language_manager = LanguageManager(master.language)
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TFrame", background="#ececec")
        style.configure("TLabel", background="#ececec", font=("Helvetica", 12))
        style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))

        self.label_username = ttk.Label(self, text=self.language_manager.language_data.get("username_label", "Username"))
        self.entry_username = ttk.Entry(self)

        self.label_password = ttk.Label(self, text=self.language_manager.language_data.get("password_label", "Password"))
        self.entry_password = ttk.Entry(self, show="*")

        self.button_login = ttk.Button(self, text=self.language_manager.language_data.get("login_button", "Login"), command=self.login)
        self.button_create_account = ttk.Button(self, text=self.language_manager.language_data.get("create_account_button", "Create an Account"), command=self.create_account)

        self.label_username.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_username.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

        self.label_password.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.entry_password.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        self.button_login.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        self.button_create_account.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    def login(self):
        # Giriş işlemleri burada yapılacak
        pass

    def create_account(self):
        # Yeni hesap oluşturma ekranına geçiş yapılacak
        pass

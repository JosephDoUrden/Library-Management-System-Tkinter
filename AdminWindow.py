import tkinter as tk
from tkinter import ttk
from userlist import UserList
from booklist import BookList
import AdminBookWindow
import AdminUserWindow

class AdminWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Admin")
        self.geometry("250x100+710+290")
        self.iconbitmap("python.ico")

        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        btn_user_data = ttk.Button(self, text="User Data", width=15, command=self.show_user_data_window)
        btn_book_data = ttk.Button(self, text="Book Data", width=15, command=self.show_book_data_window)

        btn_user_data.pack(pady=(20, 0))
        btn_book_data.pack(pady=(10, 0))

    def show_user_data_window(self):
        self.withdraw()
        self.win2 = AdminUserWindow.AdminUserWindow(self)
        self.win2.grab_set()

    def show_book_data_window(self):
        self.withdraw()
        self.win2 = AdminBookWindow.AdminBookWindow(self)
        self.win2.grab_set()

    def close_window(self):
        self.destroy()
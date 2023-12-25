import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import bookdb
import addnewbook
import booklist
import langpack

class AdminBookWindow(tk.Toplevel):
    def __init__(self, parent, selected_language):
        super().__init__()
        self.parent = parent
        self.selected_language = selected_language
        self.i18n = langpack.I18N(self.selected_language)
        self.title("Admin")
        self.geometry("250x210+710+290")
        self.iconbitmap("python.ico")
        
        self.db = bookdb.BookManager()
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        self.btn_create_database = ttk.Button(self, text=self.i18n.text_create_database_button, width=30, command=self.create_db)
        self.btn_fill_database = ttk.Button(self, text=self.i18n.text_fill_database_button, width=30, command=self.fill_db)
        self.btn_clear_database = ttk.Button(self, text=self.i18n.text_clear_database_button, width=30, command=self.clear_db)
        self.btn_add_new = ttk.Button(self, text=self.i18n.text_add_new_button_book, width=30, command=self.show_add_new_window)
        self.btn_show_list = ttk.Button(self, text=self.i18n.text_show_list_button, width=30, command=self.show_book_list_window)

        self.btn_create_database.pack(pady=(20, 0))
        self.btn_fill_database.pack(pady=(10, 0))
        self.btn_clear_database.pack(pady=(10, 0))
        self.btn_add_new.pack(pady=(10, 0))
        self.btn_show_list.pack(pady=(10, 0))

    def create_db(self):
        try:
            self.db.create_database()
            msg.showinfo(title=self.title, message=self.i18n.message_database_create_success)
        except sqlite3.Error as err:
            msg.showerror(title=self.title, message=self.i18n.message_database_create_error + "\n" + str(err))

    def fill_db(self):
        try:
            self.db.fill_database()
            msg.showinfo(title=self.title, message=self.i18n.message_database_fill_success)
        except sqlite3.Error as err:
            msg.showerror(title=self.title, message=self.i18n.message_database_fill_error + "\n" + str(err))

    def clear_db(self):
        try:
            self.db.clear_database()
            msg.showinfo(title=self.title, message=self.i18n.message_database_clear_success)
        except sqlite3.Error as err:
            msg.showerror(title=self.title, message=self.i18n.message_database_clear_error + "\n" + str(err))

    def show_add_new_window(self):
        self.withdraw()
        self.add_new = addnewbook.AddNewBook(self, self.selected_language)
        self.add_new.grab_set()

    def show_book_list_window(self):
        self.withdraw()
        self.book_list = booklist.BookList(self, self.selected_language)
        self.book_list.grab_set()

    def close_window(self):
        self.destroy()



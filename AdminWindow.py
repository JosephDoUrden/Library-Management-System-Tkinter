import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import dblib
import addnew
import gradelist

class AdminWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Admin")
        self.geometry("250x210+710+290")
        self.iconbitmap("python.ico")
        self.resizable(False, False)
        
        self.db = dblib.GradeBookManager()
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        self.btn_create_database = ttk.Button(self, text="Create Database", width=30, command=self.create_db)
        self.btn_fill_database = ttk.Button(self, text="Fill Database", width=30, command=self.fill_db)
        self.btn_clear_database = ttk.Button(self, text="Clear Database", width=30, command=self.clear_db)
        self.btn_add_new = ttk.Button(self, text="Add New", width=30, command=self.show_add_new_window)
        self.btn_show_list = ttk.Button(self, text="Show List", width=30, command=self.show_grade_list_window)

        self.btn_create_database.pack(pady=(20, 0))
        self.btn_fill_database.pack(pady=(10, 0))
        self.btn_clear_database.pack(pady=(10, 0))
        self.btn_add_new.pack(pady=(10, 0))
        self.btn_show_list.pack(pady=(10, 0))

    def create_db(self):
        try:
            self.db.create_database()
            msg.showinfo(title=self.title, message="Database created.")
        except sqlite3.Error as err:
            msg.showerror(title=self.title, message="Failed to create the database.\n" + str(err))

    def fill_db(self):
        try:
            self.db.fill_database()
            msg.showinfo(title=self.title, message="Database populated.")
        except sqlite3.Error as err:
            msg.showerror(title=self.title, message="Failed to populate the database.\n" + str(err))

    def clear_db(self):
        try:
            self.db.clear_database()
            msg.showinfo(title=self.title, message="Database cleared.")
        except sqlite3.Error as err:
            msg.showerror(title=self.title, message="Failed to clear the database.\n" + str(err))

    def show_add_new_window(self):
        self.withdraw()
        self.add_new = addnew.AddNew(parent=self)
        self.add_new.grab_set()

    def show_grade_list_window(self):
        self.withdraw()
        self.grade_list = gradelist.GradeList(parent=self)
        self.grade_list.grab_set()

    def close_window(self):
        print("Close Window")
        self.destroy()



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import dblib


class AddNew(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.db = dblib.GradeBookManager()
        self.parent = parent
        self.geometry("330x165+710+290")
        self.title(parent.window_title)
        self.iconbitmap("python.ico")
        self.resizable(False, False)

        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()

        self.create_widgets()
        self.txt_fname.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def save_grade(self):
        try:
            self.db.add_grade(fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())
            msg.showinfo("Done", "Grade saved.")
            self.clear_text_boxes()
            self.txt_fname.focus_set()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title=self.parent.window_title, message="Failed to save new grade.\n" + str(err))

    def clear_text_boxes(self):
        self.txt_fname.delete(0, "end")
        self.txt_lname.delete(0, "end")
        self.txt_grade.delete(0, "end")

    def create_widgets(self):
        self.lbl_fname = ttk.Label(self, text="First Name")
        self.lbl_fname.grid(column=0, row=0, padx=15, pady=15)

        self.lbl_lname = ttk.Label(self, text="Last Name")
        self.lbl_lname.grid(column=0, row=1, padx=15, pady=(0, 15))

        self.lbl_grade = ttk.Label(self, text="Grade")
        self.lbl_grade.grid(column=0, row=2, padx=15, pady=(0, 15))

        self.txt_fname = ttk.Entry(self, textvariable=self.fname, width=35)
        self.txt_fname.grid(column=1, row=0, padx=(0, 15), pady=15)

        self.txt_lname = ttk.Entry(self, textvariable=self.lname, width=35)
        self.txt_lname.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        
        self.txt_grade = ttk.Entry(self, textvariable=self.grade, width=35)
        self.txt_grade.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))

        self.btn_save = ttk.Button(self, text="Save Grade", command=self.save_grade)
        self.btn_save.grid(column=0, row=3, columnspan=2, pady=(0, 15))

    def close_window(self):
        self.parent.win.deiconify()
        self.destroy()

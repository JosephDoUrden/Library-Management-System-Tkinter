import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import dblib


class EditGrade(tk.Toplevel):
    def __init__(self, parent, rowid, gid, fname, lname, grade):
        super().__init__()
        self.db = dblib.GradeBookManager()
        self.parent = parent
        self.geometry("330x165+710+290")
        self.title(f"{fname} {lname}")
        self.iconbitmap("python.ico")
        self.resizable(False, False)

        self.fname = tk.StringVar(value=fname)
        self.lname = tk.StringVar(value=lname)
        self.grade = tk.IntVar(value=grade)

        self.gid = gid
        self.rowid = rowid  # ID of the Treeview item that is currently being edited.

        self.create_widgets()
        self.txt_fname.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        try:
            # Update the recorded values in the database.
            self.db.edit_grade(gid=self.gid, fname=self.fname.get(), lname=self.lname.get(), grade=self.grade.get())
            # Update the values of the selected Treeview row that is in the parent window.
            self.parent.tv.item(self.rowid, values=(self.gid, self.fname.get(), self.lname.get(), self.grade.get()))
            self.close_window()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title="Error", message="Failed to update changes.\n" + str(err))

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

        self.btn_update = ttk.Button(self, text="Update", command=self.update_values)
        self.btn_update.grid(column=0, row=3, columnspan=2, pady=(0, 15))

    def close_window(self):
        self.destroy()

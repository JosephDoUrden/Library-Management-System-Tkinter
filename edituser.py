import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import dblib
import langpack


class EditUser(tk.Toplevel):
    def __init__(self, parent, rowid, id, role, username, password, email, phone, selected_language):
        super().__init__()
        self.db = dblib.UserDataManager()
        self.parent = parent
        self.selected_language = selected_language
        self.i18n = langpack.I18N(self.selected_language)
        self.geometry("400x280+710+290")
        self.title(f"{role} - {username}")
        self.iconbitmap("python.ico")
        self.resizable(False, False)

        self.username = tk.StringVar(value=username)
        self.password = tk.StringVar(value=password)
        self.role = tk.StringVar(value=role)
        self.email = tk.StringVar(value=email)
        self.phone = tk.IntVar(value=phone)
        self.id = id
        self.rowid = rowid

        self.create_widgets()
        self.txt_username.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        try:
            # Update the recorded values in the database.
            self.db.edit_user(
                id=self.id, 
                role=self.role.get(), 
                username=self.username.get(), 
                password=self.password.get(), 
                email=self.email.get(), 
                phone=self.phone.get()
            )
            
            # Update the values of the selected Treeview row that is in the parent window.
            self.parent.tv.item(self.rowid, values=(
                self.id, 
                self.role.get(), 
                self.username.get(), 
                self.password.get(), 
                self.email.get(), 
                self.phone.get())
            )

            msg.showinfo("Success", self.i18n.message_save_success_user)
            self.close_window()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title="Error", message=self.i18n.message_confirm_change_fail + " \n" + str(err))

    def create_widgets(self):
        self.lbl_username = ttk.Label(self, text=self.i18n.text_username)
        self.lbl_username.grid(column=0, row=0, padx=15, pady=15, sticky="w")

        self.lbl_password = ttk.Label(self, text=self.i18n.text_password)
        self.lbl_password.grid(column=0, row=1, padx=15, pady=(0, 15), sticky="w")

        self.lbl_role = ttk.Label(self, text=self.i18n.text_role)
        self.lbl_role.grid(column=0, row=2, padx=15, pady=(0, 15), sticky="w")

        self.lbl_email = ttk.Label(self, text="Email")
        self.lbl_email.grid(column=0, row=3, padx=15, pady=(0, 15), sticky="w")

        self.lbl_phone = ttk.Label(self, text=self.i18n.text_phone)
        self.lbl_phone.grid(column=0, row=4, padx=15, pady=(0, 15), sticky="w")

        self.txt_username = ttk.Entry(self, textvariable=self.username, width=35)
        self.txt_username.grid(column=1, row=0, padx=(0, 15), pady=15)

        self.txt_password = ttk.Entry(self, textvariable=self.password, width=35)
        self.txt_password.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        
        self.txt_role = ttk.Entry(self, textvariable=self.role, width=35)
        self.txt_role.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))

        self.txt_email = ttk.Entry(self, textvariable=self.email, width=35)
        self.txt_email.grid(column=1, row=3, padx=(0, 15), pady=(0, 15))

        self.txt_phone = ttk.Entry(self, textvariable=self.phone, width=35)
        self.txt_phone.grid(column=1, row=4, padx=(0, 15), pady=(0, 15))

        self.btn_update = ttk.Button(self, text=self.i18n.text_update_user, command=self.update_values)
        self.btn_update.grid(column=0, row=5, columnspan=2, pady=(0, 15), sticky="e")

    def close_window(self):
        self.destroy()

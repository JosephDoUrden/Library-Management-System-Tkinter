import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib
import langpack

class ChangePasswordWindow(tk.Toplevel):
    def __init__(self, parent, current_username, selected_language):
        super().__init__()
        self.parent = parent
        self.current_username = current_username
        self.selected_language = selected_language 
        self.i18n = langpack.I18N(self.selected_language)
        self.title("Change Password")
        self.geometry("250x150+710+290")
        self.iconbitmap("python.ico")

        self.old_password_var = tk.StringVar()
        self.new_password_var = tk.StringVar()

        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.grab_set()  # Set the grab on the ChangePasswordWindow

    def create_widgets(self):
        # Old Password
        lbl_old_password = ttk.Label(self, text=self.i18n.text_old_password)
        lbl_old_password.grid(column=0, row=0, padx=10, pady=5, sticky="w")

        entry_old_password = ttk.Entry(self, textvariable=self.old_password_var, show="*")
        entry_old_password.grid(column=1, row=0, padx=10, pady=5)

        # New Password
        lbl_new_password = ttk.Label(self, text=self.i18n.text_new_password)
        lbl_new_password.grid(column=0, row=1, padx=10, pady=5, sticky="w")

        entry_new_password = ttk.Entry(self, textvariable=self.new_password_var, show="*")
        entry_new_password.grid(column=1, row=1, padx=10, pady=5)

        # Change Password Button
        btn_change_password = ttk.Button(self, text=self.i18n.title_change_password, command=self.change_password)
        btn_change_password.grid(column=1, row=2, pady=10, sticky="e")

    def change_password(self):
        old_password = self.old_password_var.get()
        new_password = self.new_password_var.get()

        if not old_password or not new_password:
            msg.showerror("Error", self.i18n.message_confirm_change_password)
            return

        # Check the old password
        user_manager = dblib.UserDataManager()
        user = user_manager.user_check(self.current_username, old_password)

        if user:
            # Change the password
            success = user_manager.change_password(self.current_username, new_password)
            if success:
                msg.showinfo("Success", self.i18n.message_confirm_change_password_success)
                self.close_window()
            else:
                msg.showerror("Error", self.i18n.message_confirm_change_password_fail)
        else:
            msg.showerror("Error", self.i18n.message_confirm_change_password_incorrect_old)

    def close_window(self):
        self.grab_release()  # Release the grab
        self.destroy()

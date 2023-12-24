import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib

class ChangePasswordWindow(tk.Toplevel):
    def __init__(self, parent, current_username):
        super().__init__()
        self.parent = parent
        self.current_username = current_username
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
        lbl_old_password = ttk.Label(self, text="Old Password:")
        lbl_old_password.grid(column=0, row=0, padx=10, pady=5, sticky="w")

        entry_old_password = ttk.Entry(self, textvariable=self.old_password_var, show="*")
        entry_old_password.grid(column=1, row=0, padx=10, pady=5)

        # New Password
        lbl_new_password = ttk.Label(self, text="New Password:")
        lbl_new_password.grid(column=0, row=1, padx=10, pady=5, sticky="w")

        entry_new_password = ttk.Entry(self, textvariable=self.new_password_var, show="*")
        entry_new_password.grid(column=1, row=1, padx=10, pady=5)

        # Change Password Button
        btn_change_password = ttk.Button(self, text="Change Password", command=self.change_password)
        btn_change_password.grid(column=1, row=2, pady=10, sticky="e")

    def change_password(self):
        old_password = self.old_password_var.get()
        new_password = self.new_password_var.get()

        if not old_password or not new_password:
            msg.showerror("Error", "Please enter both old and new passwords.")
            return

        # Check the old password
        user_manager = dblib.UserDataManager()
        user = user_manager.user_check(self.current_username, old_password)

        if user:
            # Change the password
            success = user_manager.change_password(self.current_username, new_password)
            if success:
                msg.showinfo("Success", "Password changed successfully.")
                self.close_window()
            else:
                msg.showerror("Error", "Failed to change password.")
        else:
            msg.showerror("Error", "Incorrect old password.")

    def close_window(self):
        self.grab_release()  # Release the grab
        self.destroy()

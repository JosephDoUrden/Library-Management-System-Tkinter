import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib
import edituser
import langpack


class UserList(tk.Toplevel):
    def __init__(self, parent, selected_language):
        super().__init__()
        self.db = dblib.UserDataManager()
        self.parent = parent
        self.selected_language = selected_language
        self.i18n = langpack.I18N(self.selected_language)
        self.geometry("600x200+710+290")
        self.title("User List")
        self.iconbitmap("python.ico")
        
        self.create_widgets()
        self.bind_widgets()
        self.list_users()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def list_users(self):
        for g in self.db.list_users():
            self.tv.insert(parent="", index="end", values=g)

    def delete_user(self, event):
        answer = msg.askyesno(title="Confirm Delete", message=self.i18n.message_confirm_delete)
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_user(selected_row[0])
                self.tv.delete(i)

    def show_edit_window(self, event):
        # Find the region that is double-clicked.
        # If the region is not a cell, do nothing.
        region = self.tv.identify("region", event.x, event.y)
        if region != "cell":
            return

        selected_row_id = self.tv.selection()[0]
        selected_user_row = self.tv.item(selected_row_id)["values"]
        self.edit_selected = edituser.EditUser(parent=self,
                                                 rowid=selected_row_id,
                                                 gid=selected_user_row[0],
                                                 role=selected_user_row[1],
                                                 username=selected_user_row[2],
                                                 password=selected_user_row[3],                                                 
                                                 email=selected_user_row[4],
                                                 phone=selected_user_row[5],
                                                 selected_language=self.selected_language)
        self.edit_selected.grab_set()

    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none
        self.tv = ttk.Treeview(self, height=10, show="headings", selectmode="extended")
        self.tv["columns"] = ("id", "role", "username", "password", "email", "phone")
        self.tv.pack(fill="both", expand=True)

        # Add headings for each column.
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("role", text=self.i18n.text_role, anchor="center")
        self.tv.heading("username", text=self.i18n.text_username, anchor="center")
        self.tv.heading("password", text=self.i18n.text_password, anchor="center")
        self.tv.heading("email", text="Email", anchor="center")
        self.tv.heading("phone", text=self.i18n.text_phone, anchor="center")

        # Configure each column.
        self.tv.column("id", anchor="w", width=45, stretch="no")
        self.tv.column("role", anchor="w", width=45)
        self.tv.column("username", anchor="w", width=45)
        self.tv.column("password", anchor="w", width=45)
        self.tv.column("email", anchor="w", width=45)
        self.tv.column("phone", anchor="center", width=45)

        # Add a vertical scrollbar to the Treeview.
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def bind_widgets(self):
        self.tv.bind("<Delete>", self.delete_user)  # Delete the selected Treeview item.
        self.tv.bind("<Double-1>", self.show_edit_window)  # Open the edit window for the selected item.

    def close_window(self):
        self.parent.deiconify()
        self.destroy()

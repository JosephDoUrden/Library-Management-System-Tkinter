import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import AdminWindow
import UserWindow
import dblib
import langpack

class MainWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.selected_language = tk.StringVar(value="en")
        self.i18n = langpack.I18N(self.selected_language.get())
        self.win.title("LMS - Library Management System")
        self.win.geometry("300x300+400+200")
        self.win.iconbitmap("python.ico")

        self.win2 = None
        self.lbl1 = None
        self.btn1 = None
        self.btn2 = None

        self.db = dblib.UserDataManager()
        self.create_widgets()
        self.bind_widgets()

    def reload_gui_text(self, language):
        self.i18n = langpack.I18N(language)
        self.lbl1.config(text=self.i18n.title_login_window)
        self.lbl2.config(text=self.i18n.text_username)
        self.lbl3.config(text=self.i18n.text_password)
        self.btn1.config(text=self.i18n.text_login)
        self.btn2.config(text=self.i18n.text_close)

    def create_widgets(self):
        self.lbl1 = ttk.Label(self.win, text=self.i18n.text_login, font=("Calibri", 16))
        self.lbl1.grid(row=0, column=0)

        self.lbl2 = ttk.Label(self.win, text=self.i18n.text_username)
        self.lbl3 = ttk.Label(self.win, text=self.i18n.text_password)
        self.entryUsername = ttk.Entry(self.win, width=25)
        self.entryPassword = ttk.Entry(self.win, width=25, show="*")
        self.lbl2.grid(row=1, column=0, padx=20, pady=20)
        self.lbl3.grid(row=2, column=0)

        self.entryUsername.grid(row=1, column=1)
        self.entryPassword.grid(row=2, column=1)

        self.btn1 = ttk.Button(self.win, text=self.i18n.text_login, command=self.open_new_window)
        self.btn1.grid(row=3, column=0, pady=10, columnspan=2, sticky="e")

        self.btn2 = ttk.Button(self.win, text=self.i18n.text_close, command=self.win.destroy)
        self.btn2.grid(row=4, column=0, pady=10, columnspan=2, sticky="e")

        # Add a context menu
        self.context_menu = tk.Menu(self.win, tearoff=False)
        self.context_menu.add_radiobutton(label="English", variable=self.selected_language, value="en",
                                          command=lambda: self.reload_gui_text("en"))
        self.context_menu.add_radiobutton(label="Türkçe", variable=self.selected_language, value="tr",
                                          command=lambda: self.reload_gui_text("tr"))

    def show_context_menu(self, event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def bind_widgets(self):
        self.entryPassword.bind("<Return>", self.open_new_window_bind)
        self.win.bind("<Button-3>", self.show_context_menu)

    def open_new_window_bind(self, event):
        self.open_new_window()

    def open_new_window(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()

        user = self.db.user_check(username, password)

        if user:  # user[0] = role, user[1]=uname, user[2]=password
            if str(user[0]) == 'user':
                self.shared_var = tk.StringVar()
                self.shared_var = user[1]
                self.win2 = UserWindow.UserWindow(self, self.shared_var, self.selected_language.get())
            elif str(user[0]) == 'admin':
                self.win2 = AdminWindow.AdminWindow(self, self.selected_language.get())

            self.win2.grab_set()
        else:
            msg.showerror(title=self.i18n.message_error, message=self.i18n.message_error_text)

app = MainWindow()
app.win.mainloop()

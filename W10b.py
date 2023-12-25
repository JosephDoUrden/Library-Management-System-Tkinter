# I18N - Change the active language at runtime

import tkinter as tk
from tkinter import ttk
import langpack


class W10b:
    def __init__(self):
        self.win = tk.Tk()
        self.selected_language = tk.StringVar(value="en")
        self.i18n = langpack.I18N(self.selected_language.get())
        self.win.geometry("330x165+710+290")
        self.win.title(self.i18n.title)
        self.win.iconbitmap("python.ico")
        self.win.resizable(False, False)
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()
        self.create_widgets()
        self.bind_widgets()
        self.txt_fname.focus_set()
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        pass

    def reload_gui_text(self, language):
        self.i18n = langpack.I18N(language)
        self.win.title(self.i18n.title)
        self.lbl_fname.configure(text=self.i18n.fname)
        self.lbl_lname.configure(text=self.i18n.lname)
        self.lbl_grade.configure(text=self.i18n.grade)
        self.btn_update.configure(text=self.i18n.update)

    def create_widgets(self):
        self.lbl_fname = ttk.Label(self.win, text=self.i18n.fname, width=10, anchor="center")
        self.lbl_fname.grid(column=0, row=0, padx=15, pady=15)
        self.lbl_lname = ttk.Label(self.win, text=self.i18n.lname, width=10, anchor="center")
        self.lbl_lname.grid(column=0, row=1, padx=15, pady=(0, 15))
        self.lbl_grade = ttk.Label(self.win, text=self.i18n.grade, width=10, anchor="center")
        self.lbl_grade.grid(column=0, row=2, padx=15, pady=(0, 15))

        self.txt_fname = ttk.Entry(self.win, textvariable=self.fname, width=35)
        self.txt_fname.grid(column=1, row=0, padx=(0, 15), pady=15)
        self.txt_lname = ttk.Entry(self.win, textvariable=self.lname, width=35)
        self.txt_lname.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        self.txt_grade = ttk.Entry(self.win, textvariable=self.grade, width=35)
        self.txt_grade.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))

        self.btn_update = ttk.Button(self.win, text=self.i18n.update, command=self.update_values)
        self.btn_update.grid(column=0, row=3, columnspan=2, pady=(0, 15))

        # Add a context menu
        self.context_menu = tk.Menu(self.win, tearoff=False)
        self.context_menu.add_radiobutton(label="English", variable=self.selected_language, value="en",
                                          command=lambda: self.reload_gui_text("en"))
        self.context_menu.add_radiobutton(label="Türkçe", variable=self.selected_language, value="tr",
                                          command=lambda: self.reload_gui_text("tr"))

    def bind_widgets(self):
        self.win.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        self.context_menu.tk_popup(x=event.x_root, y=event.y_root)

    def close_window(self):
        self.win.destroy()


app = W10b()
app.win.mainloop()

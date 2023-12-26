import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import bookdb
import datetime
import langpack


class AddNewBook(tk.Toplevel):
    def __init__(self, parent, selected_language):
        super().__init__()
        self.db = bookdb.BookManager()
        self.parent = parent
        self.selected_language = selected_language
        self.i18n = langpack.I18N(self.selected_language)
        self.geometry("400x300+710+200")
        self.title("Admin - " + self.i18n.text_add_new_button_book)
        self.iconbitmap("python.ico")

        self.title = tk.StringVar()
        self.author = tk.StringVar()
        self.genre = tk.StringVar()
        self.publication_year = tk.IntVar()
        self.isbn = tk.StringVar()
        self.status = tk.StringVar()
        self.user_id = tk.IntVar()

        self.create_widgets()
        self.bind_widgets()
        self.txt_title.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def is_valid_isbn_13(self, isbn):
        if not isbn.isdigit() or len(isbn) != 13:
            return False

        # ISBN-13 algoritması
        total = 0
        for i in range(12):
            digit = int(isbn[i])
            total += digit * (1 if i % 2 == 0 else 3)

        check_digit = (10 - (total % 10)) % 10
        return int(isbn[12]) == check_digit

    def save_book(self):        
        today = datetime.date.today()
        year = today.year

        try:
            if len(self.title.get()) == 0:
                msg.showerror(title="Error", message=self.i18n.message_title_error)
            elif len(self.author.get()) == 0:
                msg.showerror(title="Error", message=self.i18n.message_author_error)
            elif len(self.genre.get()) == 0:
                msg.showerror(title="Error", message=self.i18n.message_genre_error)
            elif isinstance(self.publication_year.get(), str) or int(self.publication_year.get()) > year or int(self.publication_year.get()) < 0:
                msg.showerror(title="Error", message=self.i18n.message_publication_year_error)
            elif not self.is_valid_isbn_13(self.isbn.get()):
                msg.showerror(title="Error", message=self.i18n.message_isbn_error)
            elif len(self.status.get()) == 0 and (self.status.get() != "Issued" or self.status.get() != "Available"):
                msg.showerror(title="Error", message=self.i18n.message_status_error)
            else:
                self.db.add_book(title=self.title.get(), author=self.author.get(), genre=self.genre.get(), publication_year=self.publication_year.get(), isbn=self.isbn.get(), status=self.status.get(), user_id=self.user_id.get())
                msg.showinfo("Done", self.i18n.message_save_success_book)
                self.clear_text_boxes()
                self.txt_title.focus_set()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title="Error", message=self.i18n.message_save_error_book + "\n" + str(err))

    def clear_text_boxes(self):
        self.txt_title.delete(0, "end")
        self.txt_author.delete(0, "end")
        self.txt_genre.delete(0, "end")
        self.txt_publication_year.delete(0, "end")
        self.txt_isbn.delete(0, "end")
        self.txt_status.delete(0, "end")

    def create_widgets(self):
        self.lbl_title = ttk.Label(self, text=self.i18n.text_title)
        self.lbl_title.grid(column=0, row=0, padx=15, pady=15, sticky="w")

        self.lbl_author = ttk.Label(self, text=self.i18n.text_author)
        self.lbl_author.grid(column=0, row=1, padx=15, pady=(0, 15), sticky="w")

        self.lbl_genre = ttk.Label(self, text=self.i18n.text_genre)
        self.lbl_genre.grid(column=0, row=2, padx=15, pady=(0, 15), sticky="w")

        self.lbl_publication_year = ttk.Label(self, text=self.i18n.text_publication_year)
        self.lbl_publication_year.grid(column=0, row=3, padx=15, pady=(0, 15), sticky="w")

        self.lbl_isbn = ttk.Label(self, text="ISBN")
        self.lbl_isbn.grid(column=0, row=4, padx=15, pady=(0, 15), sticky="w")

        self.lbl_isbn = ttk.Label(self, text=self.i18n.text_status)
        self.lbl_isbn.grid(column=0, row=5, padx=15, pady=(0, 15), sticky="w")

        self.txt_title = ttk.Entry(self, textvariable=self.title, width=35)
        self.txt_title.grid(column=1, row=0, padx=(0, 15), pady=15)

        self.txt_author = ttk.Entry(self, textvariable=self.author, width=35)
        self.txt_author.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        
        self.txt_genre = ttk.Entry(self, textvariable=self.genre, width=35)
        self.txt_genre.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))

        self.txt_publication_year = ttk.Entry(self, textvariable=self.publication_year, width=35)
        self.txt_publication_year.grid(column=1, row=3, padx=(0, 15), pady=(0, 15))

        self.txt_isbn = ttk.Entry(self, textvariable=self.isbn, width=35)
        self.txt_isbn.grid(column=1, row=4, padx=(0, 15), pady=(0, 15))

        self.txt_status = ttk.Entry(self, textvariable=self.status, width=35)
        self.txt_status.grid(column=1, row=5, padx=(0, 15), pady=(0, 15))

        self.btn_save = ttk.Button(self, text="Save Book", command=self.save_book)
        self.btn_save.grid(column=0, row=7, columnspan=2, pady=(0, 15), sticky="e")

    def bind_widgets(self):
        self.txt_status.bind("<Return>", self.save_book)

    def close_window(self):
        self.parent.deiconify()
        self.destroy()

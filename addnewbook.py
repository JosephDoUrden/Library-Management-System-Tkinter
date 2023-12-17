import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import bookdb
import datetime


class AddNewBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.db = bookdb.BookManager()
        self.parent = parent
        self.geometry("400x300+710+200")
        self.title("Add New Book")
        self.iconbitmap("python.ico")

        self.title = tk.StringVar()
        self.author = tk.StringVar()
        self.genre = tk.StringVar()
        self.publication_year = tk.IntVar()
        self.isbn = tk.StringVar()
        self.available_copies = tk.IntVar()
        self.total_copies = tk.IntVar()

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
                msg.showerror(title="Error", message="Please enter a valid title.")
            elif len(self.author.get()) == 0:
                msg.showerror(title="Error", message="Please enter a valid author.")
            elif len(self.genre.get()) == 0:
                msg.showerror(title="Error", message="Please enter a valid genre.")
            elif isinstance(self.publication_year.get(), str) or int(self.publication_year.get()) > year or int(self.publication_year.get()) < 0:
                msg.showerror(title="Error", message="Please enter a valid publication year.")
            elif not self.is_valid_isbn_13(self.isbn.get()):
                msg.showerror(title="Error", message="Please enter a valid ISBN.")
            elif isinstance(self.available_copies.get(), str) or int(self.available_copies.get()) < 0:
                msg.showerror(title="Error", message="Please enter a valid number of available copies.")
            elif isinstance(self.total_copies.get(), str) or int(self.total_copies.get()) <= 0:
                msg.showerror(title="Error", message="Please enter a valid total number of copies.")
            else:
                self.db.add_book(title=self.title.get(), author=self.author.get(), genre=self.genre.get(), publication_year=self.publication_year.get(), isbn=self.isbn.get(), available_copies=self.available_copies.get(), total_copies=self.total_copies.get())
                msg.showinfo("Done", "Book saved.")
                self.clear_text_boxes()
                self.txt_title.focus_set()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title="Error", message="Failed to save new book.\n" + str(err))

    def clear_text_boxes(self):
        self.txt_title.delete(0, "end")
        self.txt_author.delete(0, "end")
        self.txt_genre.delete(0, "end")
        self.txt_publication_year.delete(0, "end")
        self.txt_isbn.delete(0, "end")
        self.txt_available_copies.delete(0, "end")
        self.txt_total_copies.delete(0, "end")

    def create_widgets(self):
        self.lbl_title = ttk.Label(self, text="Title")
        self.lbl_title.grid(column=0, row=0, padx=15, pady=15, sticky="w")

        self.lbl_author = ttk.Label(self, text="Author")
        self.lbl_author.grid(column=0, row=1, padx=15, pady=(0, 15), sticky="w")

        self.lbl_genre = ttk.Label(self, text="Genre")
        self.lbl_genre.grid(column=0, row=2, padx=15, pady=(0, 15), sticky="w")

        self.lbl_publication_year = ttk.Label(self, text="Publication Year")
        self.lbl_publication_year.grid(column=0, row=3, padx=15, pady=(0, 15), sticky="w")

        self.lbl_isbn = ttk.Label(self, text="ISBN")
        self.lbl_isbn.grid(column=0, row=4, padx=15, pady=(0, 15), sticky="w")

        self.lbl_available_copies = ttk.Label(self, text="Available Copies")
        self.lbl_available_copies.grid(column=0, row=5, padx=15, pady=(0, 15), sticky="w")

        self.lbl_total_copies = ttk.Label(self, text="Total Copies")
        self.lbl_total_copies.grid(column=0, row=6, padx=15, pady=(0, 15), sticky="w")

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

        self.txt_available_copies = ttk.Entry(self, textvariable=self.available_copies, width=35)
        self.txt_available_copies.grid(column=1, row=5, padx=(0, 15), pady=(0, 15))

        self.txt_total_copies = ttk.Entry(self, textvariable=self.total_copies, width=35)
        self.txt_total_copies.grid(column=1, row=6, padx=(0, 15), pady=(0, 15))

        self.btn_save = ttk.Button(self, text="Save Book", command=self.save_book)
        self.btn_save.grid(column=0, row=7, columnspan=2, pady=(0, 15), sticky="e")

    def bind_widgets(self):
        self.total_copies.bind("<Return>", self.save_book)

    def close_window(self):
        self.parent.deiconify()
        self.destroy()

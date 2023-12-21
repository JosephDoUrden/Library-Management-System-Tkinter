import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import bookdb

class EditBook(tk.Toplevel):
    def __init__(self, parent, rowid, id, title, author, genre, publication_year, isbn, available_copies, total_copies):
        super().__init__()
        self.db = bookdb.BookManager()
        self.parent = parent
        self.geometry("450x300+400+200")
        self.title(f"Edit - {title}")
        self.iconbitmap("python.ico")
        self.resizable(False, False)

        
        self.title = tk.StringVar(value=title)
        self.author = tk.StringVar(value=author)
        self.genre = tk.StringVar(value=genre)
        self.publication_year = tk.IntVar(value=publication_year)
        self.isbn = tk.StringVar(value=isbn)
        self.available_copies = tk.IntVar(value=available_copies)
        self.total_copies = tk.IntVar(value=total_copies)

        self.id = id
        self.rowid = rowid  # ID of the Treeview item that is currently being edited.

        self.create_widgets()
        self.txt_title.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        try:
            # Update the recorded values in the database.
            self.db.edit_book(
                title=self.title.get(),
                author=self.author.get(),
                genre=self.genre.get(),
                publication_year=self.publication_year.get(),
                isbn=self.isbn.get(),
                available_copies=self.available_copies.get(),
                total_copies=self.total_copies.get()
            )
            # Update the values of the selected Treeview row that is in the parent window.
            self.parent.tv.item(self.rowid, values=(
                self.title.get(),
                self.author.get(),
                self.genre.get(),
                self.publication_year.get(),
                self.isbn.get(),
                self.available_copies.get(),
                self.total_copies.get()
            ))
            msg.showinfo("Success", "Book updated.")
            self.close_window()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title="Error", message="Failed to update changes.\n" + str(err))

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

        self.btn_update = ttk.Button(self, text="Update Book", command=self.update_values)
        self.btn_update.grid(column=0, row=7, columnspan=2, pady=(0, 15), sticky="e")

    def close_window(self):
        self.destroy()
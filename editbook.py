import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import bookdb
import langpack

class EditBook(tk.Toplevel):
    def __init__(self, parent, rowid, bid, title, author, genre, publication_year, isbn, status, user_id, selected_language):
        super().__init__()
        self.db = bookdb.BookManager()
        self.parent = parent
        self.selected_language = selected_language
        self.i18n = langpack.I18N(self.selected_language)
        self.geometry("500x400+400+200")
        self.title(f"Edit - {title}")
        self.iconbitmap("python.ico")
        self.resizable(False, False)

        self.bid = tk.IntVar(value=bid)
        self.title = tk.StringVar(value=title)
        self.author = tk.StringVar(value=author)
        self.genre = tk.StringVar(value=genre)
        self.publication_year = tk.IntVar(value=publication_year)
        self.isbn = tk.StringVar(value=isbn)
        self.status = tk.StringVar(value=status)
        self.user_id = -1 if user_id is None else user_id

        self.rowid = rowid  # ID of the Treeview item that is currently being edited.

        self.create_widgets()
        self.txt_title.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        try:
            # Validate the status field
            valid_statuses = ["Issued", "Available"]
            entered_status = self.status.get().strip()

            if entered_status not in valid_statuses:
                msg.showerror(title="Error", message=self.i18n.message_invalid_status)
                return

            # Update the recorded values in the database.
            self.db.edit_book(
                bid=self.bid.get(),
                title=self.title.get(),
                author=self.author.get(),
                genre=self.genre.get(),
                publication_year=self.publication_year.get(),
                isbn=self.isbn.get(),
                status=entered_status,
                user_id=self.user_id
            )

            # Update the values of the selected Treeview row that is in the parent window.
            self.parent.tv.item(self.rowid, values=(
                self.bid.get(),
                self.title.get(),
                self.author.get(),
                self.genre.get(),
                self.publication_year.get(),
                self.isbn.get(),
                entered_status,
                self.user_id
            ))

            msg.showinfo("Success", self.i18n.message_save_success_book)
            self.close_window()
        except (tk.TclError, sqlite3.Error) as err:
            msg.showerror(title="Error", message= self.i18n.message_save_error_book_new + "\n" + str(err))


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

        self.lbl_status = ttk.Label(self, text=self.i18n.text_status)
        self.lbl_status.grid(column=0, row=5, padx=15, pady=(0, 15), sticky="w")

        self.lbl_status = ttk.Label(self, text=self.i18n.text_issued)
        self.lbl_status.grid(column=0, row=6, padx=15, pady=(0, 15), sticky="w")

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

        self.txt_user_id = ttk.Entry(self, textvariable=self.user_id, width=35)
        self.txt_user_id.grid(column=1, row=6, padx=(0, 15), pady=(0, 15))

        self.btn_update = ttk.Button(self, text=self.i18n.text_update_book, command=self.update_values)
        self.btn_update.grid(column=0, row=7, columnspan=2, pady=(0, 15), sticky="e")

    def close_window(self):
        self.destroy()
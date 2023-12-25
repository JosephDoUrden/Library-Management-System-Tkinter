import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import bookdb
import editbook

class BookList(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.db = bookdb.BookManager()
        self.parent = parent
        self.geometry("950x300+400+200")
        self.title("Book Data")
        self.iconbitmap("python.ico")

        self.create_widgets()
        self.bind_widgets()
        self.list_books()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def list_books(self):
        for book in self.db.list_books():
            self.tv.insert(parent="", index="end", values=book)

    def delete_book(self, event):
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row(s)?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_book(selected_row[0])
                self.tv.delete(i)

    def show_edit_window(self, event):
        # Find the region that is double-clicked.
        # If the region is not a cell, do nothing.
        region = self.tv.identify("region", event.x, event.y)
        if region != "cell":
            return

        selected_row_id = self.tv.selection()[0]
        selected_book_row = self.tv.item(selected_row_id)["values"]
        self.edit_selected = editbook.EditBook(parent=self,
                                               rowid=selected_row_id,
                                               bid=selected_book_row[0],
                                               title=selected_book_row[1],
                                               author=selected_book_row[2],
                                               genre=selected_book_row[3],
                                               publication_year=selected_book_row[4],
                                               isbn=selected_book_row[5],
                                               status=selected_book_row[6],
                                               user_id=selected_book_row[7])
        self.edit_selected.grab_set()

    def create_widgets(self):
        self.tv = ttk.Treeview(self, height=15, show="headings", selectmode="extended")
        self.tv["columns"] = ("id", "title", "author", "genre", "publication_year", "isbn", "status", "user_id")
        self.tv.pack(fill="both", expand=True)

        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("title", text="Title", anchor="center")
        self.tv.heading("author", text="Author", anchor="center")
        self.tv.heading("genre", text="Genre", anchor="center")
        self.tv.heading("publication_year", text="Publication Year", anchor="center")
        self.tv.heading("isbn", text="ISBN", anchor="center")
        self.tv.heading("status", text="Status", anchor="center")
        self.tv.heading("user_id", text="User ID", anchor="center")

        for col in self.tv["columns"]:
            self.tv.column(col, anchor="w", width=100)

        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def bind_widgets(self):
        self.tv.bind("<Delete>", self.delete_book)
        self.tv.bind("<Double-1>", self.show_edit_window)

    def close_window(self):
        self.parent.deiconify()
        self.destroy()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import ChangePasswordWindow
import dblib
import bookdb
import langpack

class UserWindow(tk.Toplevel):
    def __init__(self, parent, shared_var, selected_language):
        super().__init__()
        self.parent = parent
        self.selected_language = selected_language
        self.i18n = langpack.I18N(self.selected_language)
        self.title("LMS - Library Management System")
        self.geometry("700x300+710+200")
        self.iconbitmap("python.ico")

        self.shared_var = shared_var
        self.current_user = self.get_user_info()

        self.db = dblib.UserDataManager()
        self.bookdb = bookdb.BookManager()
        self.tabControl = ttk.Notebook(self)

        self.library = None
        self.my_books = None

        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        tab1 = ttk.Frame(self.tabControl) 
        tab2 = ttk.Frame(self.tabControl) 
        tab3 = ttk.Frame(self.tabControl) 
  
        self.tabControl.add(tab1, text=self.i18n.text_library_tab) 
        self.tabControl.add(tab2, text=self.i18n.text_my_books_tab) 
        self.tabControl.add(tab3, text=self.i18n.text_profile_tab)

        # Widgets for Library
        self.library = ttk.Treeview(tab1)
        self.library['columns'] = ('id', 'title', 'author', 'genre', 'publication_year', 'isbn', 'status')
        self.library.pack(fill="both", expand=True)

        self.library.column("#0", width=0,  stretch=0)
        self.library.column("id",anchor='center', width=80)
        self.library.column("title",anchor='w',width=80)
        self.library.column("author",anchor='w',width=80)
        self.library.column("genre",anchor='w',width=80)
        self.library.column("publication_year",anchor='center',width=80) 
        self.library.column("isbn",anchor='center',width=80)         
        self.library.column("status",anchor='w',width=80)

        self.library.heading("#0",text="",anchor='center')
        self.library.heading("id",text="Id",anchor='center')
        self.library.heading("title",text=self.i18n.text_title,anchor='center')
        self.library.heading("author",text=self.i18n.text_author,anchor='center')
        self.library.heading("genre",text=self.i18n.text_genre,anchor='center')
        self.library.heading("publication_year",text=self.i18n.text_publication_year,anchor='center')        
        self.library.heading("isbn",text="ISBN",anchor='center')
        self.library.heading("status",text=self.i18n.text_status,anchor='center')

        for book in self.bookdb.list_books():
            self.library.insert(parent="", index="end", values=book)
        
        self.library_scroll = ttk.Scrollbar(self, orient="vertical", command=self.library.yview)
        self.library.configure(yscrollcommand=self.library_scroll.set)
        self.library_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

        # Bind the function here
        self.library.bind("<Double-1>", self.borrow_book)

        # Widgets for My Books
        self.my_books = ttk.Treeview(tab2)
        self.my_books['columns'] = ('id', 'title', 'author', 'genre', 'publication_year', 'isbn', 'status')
        self.my_books.pack(fill="both", expand=True)

        self.my_books.column("#0", width=0,  stretch=0)
        self.my_books.column("id",anchor='center', width=80)
        self.my_books.column("title",anchor='w',width=80)
        self.my_books.column("author",anchor='w',width=80)
        self.my_books.column("genre",anchor='w',width=80)
        self.my_books.column("publication_year",anchor='center',width=80) 
        self.my_books.column("isbn",anchor='center',width=80)         
        self.my_books.column("status",anchor='w',width=80)

        self.my_books.heading("#0",text="",anchor='center')
        self.my_books.heading("id",text="Id",anchor='center')
        self.my_books.heading("title",text=self.i18n.text_title,anchor='center')
        self.my_books.heading("author",text=self.i18n.text_author,anchor='center')
        self.my_books.heading("genre",text=self.i18n.text_genre,anchor='center')
        self.my_books.heading("publication_year",text=self.i18n.text_publication_year,anchor='center')        
        self.my_books.heading("isbn",text="ISBN",anchor='center')
        self.my_books.heading("status",text=self.i18n.text_status,anchor='center')

        for book in self.bookdb.get_my_books(self.current_user[0]):
            self.my_books.insert(parent="", index="end", values=book)
        
        self.my_books_scroll = ttk.Scrollbar(self, orient="vertical", command=self.my_books.yview)
        self.my_books.configure(yscrollcommand=self.my_books_scroll.set)
        self.my_books_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

        # Bind the function here
        self.my_books.bind("<Delete>", self.return_book)
        self.my_books.bind("<Double-1>", self.return_book)

        # Widgets for Profile 
        data_username = tk.StringVar()
        data_role = tk.StringVar()
        data_email = tk.StringVar()
        data_phone = tk.StringVar()
        data_book_count = tk.StringVar()

        profile_username = ttk.Label(tab3, text=self.i18n.text_username + ": " + self.current_user[2])
        profile_role  = ttk.Label(tab3, text=self.i18n.text_role + ": "  + str(self.current_user[1]))
        profile_email = ttk.Label(tab3, text=self.i18n.text_email + ": "  + self.current_user[4])
        profile_phone = ttk.Label(tab3, text=self.i18n.text_phone + ": "  + str(self.current_user[5]))
        
        self.change_password_btn = ttk.Button(tab3, text=self.i18n.title_change_password, command=self.change_password)
        self.change_password_btn.grid(column=0, row=5, padx = 15, pady=10, columnspan=2, sticky="w")  # Align to the left

        profile_username.grid(column = 0, row = 0, padx = 15, pady = 10, sticky="w")
        profile_role.grid(column = 0, row = 1, padx = 15, pady = 10, sticky="w")
        profile_email.grid(column = 0, row = 2, padx = 15, pady = 10, sticky="w")
        profile_phone.grid(column = 0, row = 3, padx = 15, pady = 10, sticky="w")    

        self.tabControl.pack(expand = 1, fill ="both") 

    def borrow_book(self, event):
        answer = msg.askyesno(title=self.i18n.text_confirm_borrow, message=self.i18n.message_confirm_borrow)
        if answer:
            for i in self.library.selection():
                selected_row = self.library.item(i)["values"]
                self.bookdb.issue_book(selected_row[0],self.db.user_detail(self.shared_var)[0])
            self.refresh_library()
            self.refresh_my_books()

    def return_book(self, event):
        answer = msg.askyesno(title=self.i18n.text_confirm_return, message=self.i18n.message_confirm_return)
        if answer:
            for i in self.my_books.selection():
                selected_row = self.my_books.item(i)["values"]
                self.bookdb.return_book(selected_row[0])
            self.refresh_my_books()
            self.refresh_library()

    def get_user_info(self):
        return dblib.UserDataManager().user_detail(self.shared_var)
    
    def change_password(self):
        self.win3 = ChangePasswordWindow.ChangePasswordWindow(self, self.current_user[2], self.selected_language)

    def refresh_library(self):
        # Refresh the content of the Library tab
        self.library.delete(*self.library.get_children())
        for book in self.bookdb.list_books():
            self.library.insert(parent="", index="end", values=book)

    def refresh_my_books(self):
        # Refresh the content of the My Books tab
        self.my_books.delete(*self.my_books.get_children())
        for book in self.bookdb.get_my_books(self.current_user[0]):
            self.my_books.insert(parent="", index="end", values=book)

    def close_window(self):
        self.destroy()

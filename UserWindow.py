import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import ChangePasswordWindow
import dblib
import bookdb

class UserWindow(tk.Toplevel):
    def __init__(self, parent, shared_var):
        super().__init__()
        self.parent = parent
        self.title("User")
        self.geometry("500x300+710+200")
        self.iconbitmap("python.ico")

        self.shared_var = shared_var
        self.current_user = self.get_user_info()

        self.db = dblib.UserDataManager()
        self.bookdb = bookdb.BookManager()
        self.tabControl = ttk.Notebook(self)
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        tab1 = ttk.Frame(self.tabControl) 
        tab2 = ttk.Frame(self.tabControl) 
        tab3 = ttk.Frame(self.tabControl) 
  
        self.tabControl.add(tab1, text ='Library') 
        self.tabControl.add(tab2, text ='My Books') 
        self.tabControl.add(tab3, text ='Profile')

        # Widgets for Library
        library = ttk.Treeview(tab1)
        library['columns'] = ('id', 'title', 'author', 'genre', 'publication_year', 'status')
        library.pack(fill="both", expand=True)

        library.column("#0", width=0,  stretch=0)
        library.column("id",anchor='center', width=80)
        library.column("title",anchor='center',width=80)
        library.column("author",anchor='center',width=80)
        library.column("genre",anchor='center',width=80)
        library.column("publication_year",anchor='center',width=80)        
        library.column("status",anchor='center',width=80)

        library.heading("#0",text="",anchor='center')
        library.heading("id",text="Id",anchor='center')
        library.heading("title",text="Title",anchor='center')
        library.heading("author",text="Author",anchor='center')
        library.heading("genre",text="Genre",anchor='center')
        library.heading("publication_year",text="Publication Year",anchor='center')
        library.heading("status",text="Status",anchor='center')

        for book in self.bookdb.list_books():
            library.insert(parent="", index="end", values=(book[0],book[1],book[2],book[3],book[4], book[5]))

        # Widgets for My Books

        # Widgets for Profile 
        data_username = tk.StringVar()
        data_role = tk.StringVar()
        data_email = tk.StringVar()
        data_phone = tk.StringVar()
        data_book_count = tk.StringVar()

        profile_username = ttk.Label(tab3, text="Username: " + self.current_user[2])
        profile_role  = ttk.Label(tab3, text="Role: " + str(self.current_user[1]))
        profile_email = ttk.Label(tab3, text="Email: " + self.current_user[4])
        profile_phone = ttk.Label(tab3, text="Phone Number: " + str(self.current_user[5]))
        profile_book_count = ttk.Label(tab3, text="Book Count: ")
        
        self.change_password_btn = ttk.Button(tab3, text="Change Password", command=self.change_password)
        self.change_password_btn.grid(column=0, row=5, padx = 15, pady=10, columnspan=2, sticky="w")  # Align to the left

        profile_username.grid(column = 0, row = 0, padx = 15, pady = 10, sticky="w")
        profile_role.grid(column = 0, row = 1, padx = 15, pady = 10, sticky="w")
        profile_email.grid(column = 0, row = 2, padx = 15, pady = 10, sticky="w")
        profile_phone.grid(column = 0, row = 3, padx = 15, pady = 10, sticky="w")
        profile_book_count.grid(column = 0, row = 4, padx = 15, pady = 10, sticky="w")        

        self.tabControl.pack(expand = 1, fill ="both") 

    def get_user_info(self):
        return dblib.UserDataManager().user_detail(self.shared_var)
    
    def change_password(self):
        self.win3 = ChangePasswordWindow.ChangePasswordWindow(self, self.current_user[2])


    def close_window(self):
        self.destroy()
    
    

    


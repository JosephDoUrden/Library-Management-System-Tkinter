import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import AdminWindow
import UserWindow
import dblib

class MainWindow:
    def __init__(self):
       self.win = tk.Tk()
       self.win.title("Login Window")
       self.win.geometry("300x300")
       self.win.iconbitmap("python.ico")

       self.win2 = None
       self.lbl1 = None
       self.btn1 = None
       self.btn2 = None

       self.db = dblib.UserDataManager()
       self.create_widgets()

    def create_widgets(self):
        self.lbl1 = ttk.Label(self.win, text="Login", font=("Calibri", 16))
        self.lbl1.grid(row=0, column=0)

        self.lbl2 = ttk.Label(self.win, text="Username: ")
        self.lbl3 = ttk.Label(self.win, text="Password: ")
        self.entryUsername = ttk.Entry(self.win, width=25)
        self.entryPassword = ttk.Entry(self.win, width=25, show="*")
        self.lbl2.grid(row=1, column=0, padx=20, pady=20)
        self.lbl3.grid(row=2, column=0)

        self.entryUsername.grid(row=1, column=1)
        self.entryPassword.grid(row=2, column=1)

        self.btn1 = ttk.Button(self.win, text="Login", command=self.open_new_window)
        self.btn1.grid(row=3, column=0, pady=10, columnspan=2, sticky="e")

        self.btn2 = ttk.Button(self.win, text="Close", command=self.win.destroy)
        self.btn2.grid(row=4, column=0, pady=10, columnspan=2, sticky="e")

    def open_new_window(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()

        user = self.db.user_check(username, password)
        
        if user:  # user[0] = role, user[1]=uname, user[2]=password
            if str(user[0]) == 'user':
                self.win2 = UserWindow.UserWindow(self)
            elif str(user[0]) == 'admin':
                self.win2 = AdminWindow.AdminWindow(self)
                
            self.win2.grab_set()
        else:
            msg.showerror(title="Error", message="Incorrect username or password")
            
            

    
    

app = MainWindow()
app.win.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3

class UserWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("User")
        self.geometry("250x210+710+290")
        self.iconbitmap("python.ico")
        
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
        self.tabControl.pack(expand = 1, fill ="both") 
  
        ttk.Label(tab1).grid(column = 0, row = 0, padx = 30, pady = 30)   
        ttk.Label(tab2).grid(column = 0, row = 0, padx = 30, pady = 30) 

    def close_window(self):
        self.destroy()
    
    

    


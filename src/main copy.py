import tkinter as tk
from tkinter import ttk
from components.centerscreen import center_screen_geometry

win = tk.Tk()

win.title("Library Management System")


# Set the window to center of the screen
win.geometry(center_screen_geometry(
    screen_width=win.winfo_screenwidth(), 
    screen_height=win.winfo_screenheight(), 
    win_width=600, 
    win_height=300
    ))


#TODO: Login Page ilgili yere taşınacak aşağıdaki kodlar temsilidir!

# create a label
label1 = ttk.Label(win, text="Username: ")
label2 = ttk.Label(win, text="Password: ")

# create a entry
entry1 = ttk.Entry(win, width=25)
entry2 = ttk.Entry(win, width=25)

# create a button
button1 = ttk.Button(win, text="Login")

# grid system
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
button1.grid(row=2, column=1, padx=10, pady=10)



win.mainloop()
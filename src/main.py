import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Library Management System")

def center_secreen_geometry(screen_width, screen_height, window_width, window_height):
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    return f"{window_width}x{window_height}+{x}+{y}"

win.geometry(center_secreen_geometry(screen_width = win.winfo_screenwidth(),
                                    screen_height= win.winfo_screenheight(),
                                    window_width=400,
                                    window_height=400))

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
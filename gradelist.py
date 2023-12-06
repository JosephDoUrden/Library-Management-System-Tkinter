import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import dblib
import editgrade


class GradeList(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.db = dblib.GradeBookManager()
        self.parent = parent
        self.geometry("450x200+710+290")
        self.title(parent.window_title)
        self.iconbitmap("python.ico")
        
        self.create_widgets()
        self.bind_widgets()
        self.list_grades()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def list_grades(self):
        for g in self.db.list_grades():
            self.tv.insert(parent="", index="end", values=g)

    def show_average(self, event):
        result = self.db.get_stats()

        if result[0] == 0:  # Check the total number of grades
            msg_content = "The database is empty."
        else:
            msg_content = (f"Number of recorded grades: {str(result[0])}\n\n"
                           f"The average: {str(round(result[1], 1))}")

        msg.showinfo(title=self.parent.window_title, message=msg_content)

    def delete_grade(self, event):
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row(s)?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                self.db.delete_grade(selected_row[0])
                self.tv.delete(i)

    def show_edit_window(self, event):
        # Find the region that is double-clicked.
        # If the region is not a cell, do nothing.
        region = self.tv.identify("region", event.x, event.y)
        if region != "cell":
            return

        selected_row_id = self.tv.selection()[0]
        selected_grade_row = self.tv.item(selected_row_id)["values"]
        self.edit_selected = editgrade.EditGrade(parent=self,
                                                 rowid=selected_row_id,
                                                 gid=selected_grade_row[0],
                                                 fname=selected_grade_row[1],
                                                 lname=selected_grade_row[2],
                                                 grade=selected_grade_row[3])
        self.edit_selected.grab_set()

    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none
        self.tv = ttk.Treeview(self, height=10, show="headings", selectmode="extended")
        self.tv["columns"] = ("id", "fname", "lname", "grade")
        self.tv.pack(fill="both", expand=True)

        # Add headings for each column.
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")

        # Configure each column.
        self.tv.column("id", anchor="center", width=45, stretch="no")
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)

        # Add a vertical scrollbar to the Treeview.
        self.tv_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def bind_widgets(self):
        self.bind("<F1>", self.show_average)  # Show the average when the user presses F1.
        self.tv.bind("<Delete>", self.delete_grade)  # Delete the selected Treeview item.
        self.tv.bind("<Double-1>", self.show_edit_window)  # Open the edit window for the selected item.

    def close_window(self):
        self.parent.win.deiconify()
        self.destroy()

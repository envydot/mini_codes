import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Student Management System")

students = []  # List to store student records

# Functions
def add_student():
    name = entry_name.get()
    roll = entry_roll.get()
    course = entry_course.get()
    if name and roll and course:
        students.append({"Name": name, "Roll": roll, "Course": course})
        update_listbox()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def update_listbox():
    listbox.delete(0, tk.END)
    for s in students:
        listbox.insert(tk.END, f"{s['Roll']} - {s['Name']} ({s['Course']})")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_course.delete(0, tk.END)

def delete_student():
    selected = listbox.curselection()
    if selected:
        students.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select a student to delete!")

# Labels and Entries
tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Roll No").grid(row=1, column=0)
entry_roll = tk.Entry(root)
entry_roll.grid(row=1, column=1)

tk.Label(root, text="Course").grid(row=2, column=0)
entry_course = tk.Entry(root)
entry_course.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, pady=5)
tk.Button(root, text="Delete Student", command=delete_student).grid(row=3, column=1, pady=5)

# Listbox
listbox = tk.Listbox(root, width=40)
listbox.grid(row=4, column=0, columnspan=2)

root.mainloop()
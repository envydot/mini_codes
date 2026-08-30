import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Main window
root = tk.Tk()
root.title("File Explorer")
root.geometry("600x400")

# Listbox to display files
listbox = tk.Listbox(root, width=80, height=20)
listbox.pack(pady=20)

# Function to open directory
def open_directory():
    folder = filedialog.askdirectory()
    if folder:
        listbox.delete(0, tk.END)
        try:
            files = os.listdir(folder)
            for f in files:
                listbox.insert(tk.END, f)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to open selected file
def open_file():
    selected = listbox.curselection()
    if selected:
        filename = listbox.get(selected[0])
        messagebox.showinfo("File Selected", f"You selected: {filename}")
    else:
        messagebox.showwarning("Selection Error", "Select a file first!")

# Buttons
tk.Button(root, text="Open Directory", command=open_directory).pack(pady=5)
tk.Button(root, text="Open File", command=open_file).pack(pady=5)

root.mainloop()
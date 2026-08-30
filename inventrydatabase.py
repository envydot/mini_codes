import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")
conn.commit()

# Main window
root = tk.Tk()
root.title("Inventory Database")
root.geometry("500x400")

# Functions
def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    if name and quantity and price:
        cursor.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
                       (name, int(quantity), float(price)))
        conn.commit()
        update_listbox()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def update_listbox():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM inventory")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[1]} - Qty: {row[2]} - ₹{row[3]:.2f}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

def delete_item():
    selected = listbox.curselection()
    if selected:
        cursor.execute("DELETE FROM inventory WHERE id=?", (selected[0]+1,))
        conn.commit()
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Select an item to delete!")

# Labels and Entries
tk.Label(root, text="Item Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Quantity").grid(row=1, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1)

tk.Label(root, text="Price").grid(row=2, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Item", command=add_item).grid(row=3, column=0, pady=5)
tk.Button(root, text="Delete Item", command=delete_item).grid(row=3, column=1, pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=2)

update_listbox()
root.mainloop()
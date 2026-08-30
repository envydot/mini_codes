import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Payroll Management System")
root.geometry("400x300")

# Functions
def calculate_salary():
    try:
        hours = float(entry_hours.get())
        rate = float(entry_rate.get())
        salary = hours * rate
        label_result.config(text=f"Total Salary: ₹{salary:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_hours.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    label_result.config(text="Total Salary: ₹0.00")

# Labels and Entries
tk.Label(root, text="Employee Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Hours Worked").grid(row=1, column=0, padx=10, pady=5)
entry_hours = tk.Entry(root)
entry_hours.grid(row=1, column=1)

tk.Label(root, text="Hourly Rate").grid(row=2, column=0, padx=10, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Calculate Salary", command=calculate_salary).grid(row=3, column=0, pady=10)
tk.Button(root, text="Clear", command=clear_entries).grid(row=3, column=1, pady=10)

# Result Label
label_result = tk.Label(root, text="Total Salary: ₹0.00", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
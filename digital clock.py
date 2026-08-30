import tkinter as tk
import time

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Label to display time
label = tk.Label(root, font=("Arial", 48), bg="black", fg="cyan")
label.pack(anchor="center")

# Function to update time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    # Call this function again after 1000ms (1 second)
    label.after(1000, update_time)

# Start the clock
update_time()

root.mainloop()
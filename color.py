import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Color Guessing Game")
root.geometry("400x300")

colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Black", "Brown", "Pink"]

score = 0

# Functions
def new_round():
    global current_color
    text_color = random.choice(colors)
    display_color = random.choice(colors)
    current_color = display_color
    label_color.config(text=text_color, fg=display_color)

def check_guess(guess):
    global score
    if guess.lower() == current_color.lower():
        score += 1
        label_result.config(text=f"Correct! Score: {score}")
    else:
        label_result.config(text=f"Wrong! It was {current_color}. Score: {score}")
    new_round()

# Widgets
label_color = tk.Label(root, text="", font=("Arial", 32))
label_color.pack(pady=20)

label_result = tk.Label(root, text="Score: 0", font=("Arial", 14))
label_result.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

for c in colors:
    tk.Button(frame_buttons, text=c, width=8, command=lambda col=c: check_guess(col)).pack(side="left")

new_round()
root.mainloop()
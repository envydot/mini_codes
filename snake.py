import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Snake Game")

# Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# Snake and food setup
snake = [(20, 20)]
snake_dir = "Right"
food = (100, 100)

# Draw snake and food
def draw_snake():
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x+20, y+20, fill="green", tags="snake")

def draw_food():
    canvas.delete("food")
    x, y = food
    canvas.create_oval(x, y, x+20, y+20, fill="red", tags="food")

# Move snake
def move_snake():
    global food
    x, y = snake[0]
    if snake_dir == "Up":
        y -= 20
    elif snake_dir == "Down":
        y += 20
    elif snake_dir == "Left":
        x -= 20
    elif snake_dir == "Right":
        x += 20

    new_head = (x, y)

    # Check collisions
    if (x < 0 or x >= 400 or y < 0 or y >= 400 or new_head in snake):
        canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 24))
        return

    snake.insert(0, new_head)

    # Check food
    if new_head == food:
        food = (random.randrange(0, 20)*20, random.randrange(0, 20)*20)
    else:
        snake.pop()

    draw_snake()
    draw_food()
    root.after(100, move_snake)

# Change direction
def change_dir(event):
    global snake_dir
    if event.keysym in ["Up", "Down", "Left", "Right"]:
        snake_dir = event.keysym

root.bind("<Key>", change_dir)

draw_snake()
draw_food()
move_snake()

root.mainloop()
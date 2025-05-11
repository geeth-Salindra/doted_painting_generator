import os
from tkinter import Tk, Label, Entry, Button, messagebox, filedialog
from turtle import Turtle, Screen
from PIL import Image

def draw_dot_image(img_path):
    try:
        if not os.path.isfile(img_path):
            raise FileNotFoundError("Image file not found!")

        # Step 1: Load and resize image to reduce detail
        img = Image.open(img_path).convert("RGB")
        dot_grid_size = 50  # Try 50x50 dots; adjust as needed
        img = img.resize((dot_grid_size, dot_grid_size))
        pixels = img.load()

        # Step 2: Turtle setup
        dot_size = 6  # Larger visible dots
        spacing = 6   # Space between dots
        width, height = img.size

        screen = Screen()
        screen.setup(width=width * spacing + 100, height=height * spacing + 100)
        screen.bgcolor("white")
        screen.colormode(255)
        screen.tracer(0)

        t = Turtle()
        t.penup()
        t.hideturtle()
        t.speed(0)

        start_x = -width * spacing // 2
        start_y = height * spacing // 2

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                t.goto(start_x + x * spacing, start_y - y * spacing)
                t.dot(dot_size, (r, g, b))

        screen.update()
        screen.mainloop()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        path_entry.delete(0, 'end')
        path_entry.insert(0, file_path)

def start_process():
    img_path = path_entry.get().strip()
    if not img_path:
        messagebox.showwarning("Input Needed", "Please enter or select an image path.")
    else:
        draw_dot_image(img_path)

# GUI setup
root = Tk()
root.title("Dot Art Generator")
root.geometry("500x150")
root.resizable(True, True)

Label(root, text="Image Path:").pack(pady=5)
path_entry = Entry(root, width=60)
path_entry.pack(pady=5)

Button(root, text="Browse", command=browse_image).pack(pady=2)
Button(root, text="Start", command=start_process, bg="green", fg="white").pack(pady=10)

root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

def show_linechart_scratching_image(root):
    window = tk.Toplevel(root)
    window.title("Line Chart: Full Session Trace")
    img = Image.open("Analyser/images/linechart_scratching.png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()
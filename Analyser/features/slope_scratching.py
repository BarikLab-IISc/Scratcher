import tkinter as tk
from PIL import Image, ImageTk

def show_slope_scratching_image(root):
    window = tk.Toplevel(root)
    window.title("Slope of Scratching Session")
    img = Image.open("Analyser/images/slope_scratching.png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()
import tkinter as tk
from PIL import Image, ImageTk

def show_auc_scratching_image(root):
    window = tk.Toplevel(root)
    window.title("Area Under the Curve (Scratching Over Time)")
    img = Image.open("Analyser/images/auc_scratching.png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()
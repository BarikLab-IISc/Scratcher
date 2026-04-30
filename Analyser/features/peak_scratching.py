import tkinter as tk
from PIL import Image, ImageTk

def show_peak_scratching_image(root):
    window = tk.Toplevel(root)
    window.title("Peak Scratching Duration")
    img = Image.open("Analyser/images/peak_scratching.png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo  # Prevent garbage collection
    label.pack()
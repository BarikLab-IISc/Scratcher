import tkinter as tk
from PIL import Image, ImageTk

def show_heatmap_scratching_image(root):
    window = tk.Toplevel(root)
    window.title("Heatmap: Scratching Duration Per Minute")
    img = Image.open("Analyser/images/heatmap_scratching.png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()
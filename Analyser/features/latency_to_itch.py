import tkinter as tk
from PIL import Image, ImageTk

def show_latency_to_itch_image(root):
    window = tk.Toplevel(root)
    window.title("Latency to Itch Onset")
    img = Image.open("Analyser/images/latency_to_itch.png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()
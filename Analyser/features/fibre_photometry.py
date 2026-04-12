import tkinter as tk
from PIL import Image, ImageTk

def show_fiber_photometry_image(root):
    window = tk.Toplevel(root)
    window.title("Fiber Photometry")
    img = Image.open("Analyser/images/fiber_photometry.png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()
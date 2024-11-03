import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import os
import time

def run_yolo():
  
    model_path = model_entry.get()
    input_path = input_entry.get()
    change_dir = dir_entry.get()
    save_output = save_var.get()
    confidence = float(conf_entry.get())

    begin = time.time()
    
    model = YOLO(model_path)
    
    if change_dir:
        os.chdir(change_dir)
    
    model.predict(input_path, save=save_output, conf=confidence)
    
    end = time.time()
    result_label.config(text=f"Prediction completed in {end - begin:.2f} seconds.")

root = tk.Tk()
root.title("YOLO Prediction GUI")

tk.Label(root, text="Model Path:").grid(row=0, column=0, padx=10, pady=5)
model_entry = tk.Entry(root, width=50)
model_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: model_entry.insert(0, filedialog.askopenfilename())).grid(row=0, column=2)

tk.Label(root, text="Input Video Path:").grid(row=1, column=0, padx=10, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: input_entry.insert(0, filedialog.askopenfilename())).grid(row=1, column=2)

tk.Label(root, text="Change Directory:").grid(row=2, column=0, padx=10, pady=5)
dir_entry = tk.Entry(root, width=50)
dir_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: dir_entry.insert(0, filedialog.askdirectory())).grid(row=2, column=2)

save_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Save Output", variable=save_var).grid(row=3, column=0, padx=10, pady=5)

tk.Label(root, text="Confidence Threshold:").grid(row=4, column=0, padx=10, pady=5)
conf_entry = tk.Entry(root, width=10)
conf_entry.insert(0, "0.5")
conf_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Button(root, text="Run YOLO Prediction", command=run_yolo).grid(row=5, column=0, columnspan=3, pady=20)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=3, pady=5)

root.mainloop()

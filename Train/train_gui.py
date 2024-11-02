import tkinter as tk
from tkinter import filedialog, messagebox
import time
from ultralytics import YOLO
import os
import warnings

def browse_directory(entry):
    directory = filedialog.askdirectory()
    if directory:
        entry.delete(0, tk.END)
        entry.insert(0, directory)

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def start_training():
    cwd = cwd_entry.get()
    model_path = model_entry.get()
    data_path = data_entry.get()
    epochs = epochs_entry.get()

    if not os.path.exists(cwd):
        messagebox.showerror("Error", "The specified working directory does not exist.")
        return
    
    try:
        epochs = int(epochs)
    except ValueError:
        messagebox.showerror("Error", "Number of epochs should be an integer.")
        return
    
    # Change to the working directory
    os.chdir(cwd)
    
    # Start the training process
    try:
        begin = time.time()
        model = YOLO(model_path)
        model.train(data=data_path, epochs=epochs)
        end = time.time()
        
        # Save the time taken
        with open("Time_taken.txt", "w") as f:
            f.write(f"Time taken for training: {end - begin} seconds")
        
        messagebox.showinfo("Success", f"Training completed! Time taken: {end - begin:.2f} seconds")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the GUI
root = tk.Tk()
root.title("YOLO Training GUI")

# Working Directory
tk.Label(root, text="Working Directory:").grid(row=0, column=0, padx=10, pady=10)
cwd_entry = tk.Entry(root, width=50)
cwd_entry.grid(row=0, column=1, padx=10, pady=10)
cwd_button = tk.Button(root, text="Browse", command=lambda: browse_directory(cwd_entry))
cwd_button.grid(row=0, column=2, padx=10, pady=10)

# Model Path
tk.Label(root, text="Model File Path:").grid(row=1, column=0, padx=10, pady=10)
model_entry = tk.Entry(root, width=50)
model_entry.grid(row=1, column=1, padx=10, pady=10)
model_button = tk.Button(root, text="Browse", command=lambda: browse_file(model_entry))
model_button.grid(row=1, column=2, padx=10, pady=10)

# Data File Path
tk.Label(root, text="Data Config Path:").grid(row=2, column=0, padx=10, pady=10)
data_entry = tk.Entry(root, width=50)
data_entry.grid(row=2, column=1, padx=10, pady=10)
data_button = tk.Button(root, text="Browse", command=lambda: browse_file(data_entry))
data_button.grid(row=2, column=2, padx=10, pady=10)

# Epochs
tk.Label(root, text="Epochs:").grid(row=3, column=0, padx=10, pady=10)
epochs_entry = tk.Entry(root, width=50)
epochs_entry.insert(0, "57")  # Default value
epochs_entry.grid(row=3, column=1, padx=10, pady=10)

# Start Training Button
train_button = tk.Button(root, text="Start Training", command=start_training, bg="green", fg="white")
train_button.grid(row=4, column=1, padx=10, pady=20)

# Run the GUI loop
root.mainloop()

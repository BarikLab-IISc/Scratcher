import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import re
import time
import pandas as pd
from ultralytics import YOLO
from video_processing import process_video
from behaviour_filtering import filter_behaviours
from behaviour_analysis import analyse_behaviours

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

def start_processing():
    model_path = model_entry.get()
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    conf_threshold = conf_threshold_entry.get()

    if not os.path.exists(model_path):
        messagebox.showerror("Error", "The specified model file does not exist.")
        return
    if not os.path.exists(input_folder):
        messagebox.showerror("Error", "The specified input folder does not exist.")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        conf_threshold = float(conf_threshold)
    except ValueError:
        messagebox.showerror("Error", "Confidence threshold should be a float value.")
        return

    model = YOLO(model_path)
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]
    for video_file in video_files:
        video_name = re.search(r'([^\\]+)\.mp4$', video_file).group(1)
        process_video(model, os.path.join(input_folder, video_file), output_folder, video_name, conf_threshold)

    messagebox.showinfo("Processing Complete", "Video processing complete. Starting behavior filtering...")

    excel_files = [f for f in os.listdir(output_folder) if f.endswith('.xlsx')]
    for excel_file in excel_files:
        input_path = os.path.join(output_folder, excel_file)
        output_path = os.path.join(output_folder, "raster_plot_input_" + excel_file)
        filter_behaviours(input_path, output_path)

    messagebox.showinfo("Filtering Complete", "Behavior filtering complete. Starting behavior analysis...")

    analyse_behaviours(output_folder)

    messagebox.showinfo("Analysis Complete", "Behavior analysis complete.")

def run_yolo():
    model_path = model_entry_predict.get()
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

def start_training():
    cwd = cwd_entry.get()
    model_path = model_entry_train.get()
    data_path = data_entry.get()
    epochs = epochs_entry.get()

    if not os.path.exists(cwd):
        messagebox.showerror("Error", "The specified working directory does not exist.")
        return
    os.chdir(cwd)

    if not os.path.exists(model_path):
        messagebox.showerror("Error", "The specified model file does not exist.")
        return

    if not os.path.exists(data_path):
        messagebox.showerror("Error", "The specified data configuration file does not exist.")
        return

    try:
        epochs = int(epochs)
    except ValueError:
        messagebox.showerror("Error", "Number of epochs should be an integer.")
        return

    model = YOLO(model_path)
    begin = time.time()

    try:
        results = model.train(data=data_path, epochs=epochs)
        end = time.time()
        time_taken = end - begin

        with open("Time_taken.txt", "w") as f:
            f.write(f"Time taken for training: {time_taken:.2f} seconds")

        messagebox.showinfo("Training Complete", f"Training completed in {time_taken:.2f} seconds. See Time_taken.txt for details.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during training:\n{e}")

root = tk.Tk()
root.title("Behavior Analysis & YOLO GUI")

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, expand=True)

analyser_frame = ttk.Frame(notebook)
notebook.add(analyser_frame, text="Analyser")

tk.Label(analyser_frame, text="YOLO Model File:").grid(row=0, column=0, padx=10, pady=10)
model_entry = tk.Entry(analyser_frame, width=50)
model_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(analyser_frame, text="Browse", command=lambda: browse_file(model_entry)).grid(row=0, column=2, padx=10, pady=10)

tk.Label(analyser_frame, text="Input Folder:").grid(row=1, column=0, padx=10, pady=10)
input_folder_entry = tk.Entry(analyser_frame, width=50)
input_folder_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(analyser_frame, text="Browse", command=lambda: browse_directory(input_folder_entry)).grid(row=1, column=2, padx=10, pady=10)

tk.Label(analyser_frame, text="Output Folder:").grid(row=2, column=0, padx=10, pady=10)
output_folder_entry = tk.Entry(analyser_frame, width=50)
output_folder_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(analyser_frame, text="Browse", command=lambda: browse_directory(output_folder_entry)).grid(row=2, column=2, padx=10, pady=10)

tk.Label(analyser_frame, text="Confidence Threshold:").grid(row=3, column=0, padx=10, pady=10)
conf_threshold_entry = tk.Entry(analyser_frame, width=50)
conf_threshold_entry.insert(0, "0.6")  
conf_threshold_entry.grid(row=3, column=1, padx=10, pady=10)

process_button = tk.Button(analyser_frame, text="Start Processing", command=start_processing, bg="green", fg="white")
process_button.grid(row=4, column=1, padx=10, pady=20)

predict_frame = ttk.Frame(notebook)
notebook.add(predict_frame, text="YOLO Prediction")

tk.Label(predict_frame, text="Model Path:").grid(row=0, column=0, padx=10, pady=5)
model_entry_predict = tk.Entry(predict_frame, width=50)
model_entry_predict.grid(row=0, column=1, padx=10, pady=5)
tk.Button(predict_frame, text="Browse", command=lambda: browse_file(model_entry_predict)).grid(row=0, column=2)

tk.Label(predict_frame, text="Input Video Path:").grid(row=1, column=0, padx=10, pady=5)
input_entry = tk.Entry(predict_frame, width=50)
input_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(predict_frame, text="Browse", command=lambda: browse_file(input_entry)).grid(row=1, column=2)

tk.Label(predict_frame, text="Change Directory:").grid(row=2, column=0, padx=10, pady=5)
dir_entry = tk.Entry(predict_frame, width=50)
dir_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(predict_frame, text="Browse", command=lambda: browse_directory(dir_entry)).grid(row=2, column=2)

save_var = tk.BooleanVar(value=True)
tk.Checkbutton(predict_frame, text="Save Output", variable=save_var).grid(row=3, column=0, padx=10, pady=5)

tk.Label(predict_frame, text="Confidence Threshold:").grid(row=4, column=0, padx=10, pady=5)
conf_entry = tk.Entry(predict_frame, width=10)
conf_entry.insert(0, "0.5")
conf_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Button(predict_frame, text="Run YOLO Prediction", command=run_yolo).grid(row=5, column=0, columnspan=3, pady=20)
result_label = tk.Label(predict_frame, text="")
result_label.grid(row=6, column=0, columnspan=3, pady=5)

train_frame = ttk.Frame(notebook)
notebook.add(train_frame, text="Training")

tk.Label(train_frame, text="Working Directory:").grid(row=0, column=0, padx=10, pady=10)
cwd_entry = tk.Entry(train_frame, width=50)
cwd_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(train_frame, text="Browse", command=lambda: browse_directory(cwd_entry)).grid(row=0, column=2, padx=10, pady=10)

tk.Label(train_frame, text="Pre-trained Model Path:").grid(row=1, column=0, padx=10, pady=10)
model_entry_train = tk.Entry(train_frame, width=50)
model_entry_train.grid(row=1, column=1, padx=10, pady=10)
tk.Button(train_frame, text="Browse", command=lambda: browse_file(model_entry_train)).grid(row=1, column=2, padx=10, pady=10)

tk.Label(train_frame, text="Data Configuration Path:").grid(row=2, column=0, padx=10, pady=10)
data_entry = tk.Entry(train_frame, width=50)
data_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(train_frame, text="Browse", command=lambda: browse_file(data_entry)).grid(row=2, column=2, padx=10, pady=10)

tk.Label(train_frame, text="Number of Epochs:").grid(row=3, column=0, padx=10, pady=10)
epochs_entry = tk.Entry(train_frame, width=10)
epochs_entry.insert(0, "10") 
epochs_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

train_button = tk.Button(train_frame, text="Start Training", command=start_training, bg="blue", fg="white")
train_button.grid(row=4, column=1, padx=10, pady=20)

root.mainloop()

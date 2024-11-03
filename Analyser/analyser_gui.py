import tkinter as tk
from tkinter import filedialog, messagebox
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

    # Process each video
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

root = tk.Tk()
root.title("Behavior Analysis GUI")

tk.Label(root, text="YOLO Model File:").grid(row=0, column=0, padx=10, pady=10)
model_entry = tk.Entry(root, width=50)
model_entry.grid(row=0, column=1, padx=10, pady=10)
model_button = tk.Button(root, text="Browse", command=lambda: browse_file(model_entry))
model_button.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Input Folder:").grid(row=1, column=0, padx=10, pady=10)
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=1, column=1, padx=10, pady=10)
input_folder_button = tk.Button(root, text="Browse", command=lambda: browse_directory(input_folder_entry))
input_folder_button.grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Output Folder:").grid(row=2, column=0, padx=10, pady=10)
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=2, column=1, padx=10, pady=10)
output_folder_button = tk.Button(root, text="Browse", command=lambda: browse_directory(output_folder_entry))
output_folder_button.grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Confidence Threshold:").grid(row=3, column=0, padx=10, pady=10)
conf_threshold_entry = tk.Entry(root, width=50)
conf_threshold_entry.insert(0, "0.6")  # defaut value is set to 0.6
conf_threshold_entry.grid(row=3, column=1, padx=10, pady=10)

process_button = tk.Button(root, text="Start Processing", command=start_processing, bg="green", fg="white")
process_button.grid(row=4, column=1, padx=10, pady=20)

# Run the GUI loop
root.mainloop()

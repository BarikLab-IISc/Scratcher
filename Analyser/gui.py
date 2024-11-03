import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import re
import time
from ultralytics import YOLO
import pandas as pd
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

def start_prediction():
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

    messagebox.showinfo("Processing Complete", "Video processing complete.")

def start_analysis():
    output_folder = output_folder_entry_analyse.get()

    if not os.path.exists(output_folder):
        messagebox.showerror("Error", "The specified output folder does not exist.")
        return

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

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, expand=True)

predict_frame = ttk.Frame(notebook)
notebook.add(predict_frame, text="Prediction")

tk.Label(predict_frame, text="YOLO Model File:").grid(row=0, column=0, padx=10, pady=10)
model_entry = tk.Entry(predict_frame, width=50)
model_entry.grid(row=0, column=1, padx=10, pady=10)
model_button = tk.Button(predict_frame, text="Browse", command=lambda: browse_file(model_entry))
model_button.grid(row=0, column=2, padx=10, pady=10)

tk.Label(predict_frame, text="Input Folder:").grid(row=1, column=0, padx=10, pady=10)
input_folder_entry = tk.Entry(predict_frame, width=50)
input_folder_entry.grid(row=1, column=1, padx=10, pady=10)
input_folder_button = tk.Button(predict_frame, text="Browse", command=lambda: browse_directory(input_folder_entry))
input_folder_button.grid(row=1, column=2, padx=10, pady=10)

tk.Label(predict_frame, text="Output Folder:").grid(row=2, column=0, padx=10, pady=10)
output_folder_entry = tk.Entry(predict_frame, width=50)
output_folder_entry.grid(row=2, column=1, padx=10, pady=10)
output_folder_button = tk.Button(predict_frame, text="Browse", command=lambda: browse_directory(output_folder_entry))
output_folder_button.grid(row=2, column=2, padx=10, pady=10)

tk.Label(predict_frame, text="Confidence Threshold:").grid(row=3, column=0, padx=10, pady=10)
conf_threshold_entry = tk.Entry(predict_frame, width=50)
conf_threshold_entry.insert(0, "0.6")  # Default value is set to 0.6
conf_threshold_entry.grid(row=3, column=1, padx=10, pady=10)

process_button = tk.Button(predict_frame, text="Start Prediction", command=start_prediction, bg="green", fg="white")
process_button.grid(row=4, column=1, padx=10, pady=20)

analyse_frame = ttk.Frame(notebook)
notebook.add(analyse_frame, text="Analysis")

tk.Label(analyse_frame, text="Processed Output Folder:").grid(row=0, column=0, padx=10, pady=10)
output_folder_entry_analyse = tk.Entry(analyse_frame, width=50)
output_folder_entry_analyse.grid(row=0, column=1, padx=10, pady=10)
output_folder_button_analyse = tk.Button(analyse_frame, text="Browse", command=lambda: browse_directory(output_folder_entry_analyse))
output_folder_button_analyse.grid(row=0, column=2, padx=10, pady=10)

analyse_button = tk.Button(analyse_frame, text="Start Analysis", command=start_analysis, bg="blue", fg="white")
analyse_button.grid(row=1, column=1, padx=10, pady=20)

root.mainloop()

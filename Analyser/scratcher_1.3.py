# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox, colorchooser
# import os

# class ScratcherGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Scratcher 1.3 ©")
#         self.root.geometry("1000x750")
#         self.root.configure(bg="#f2dbdb")
        
#         # Variables for storing paths and settings
#         self.input_folder = tk.StringVar()
#         self.output_folder = tk.StringVar()
#         self.fps_value = tk.StringVar(value="30")
#         self.selected_model = tk.StringVar(value="Model 1.3")
        
#         # Analysis variables
#         self.analysis_input_folder = tk.StringVar()
#         self.analysis_output_folder = tk.StringVar()
#         self.video_colors = {}
#         self.video_aliases = {}
#         self.selected_videos = []
#         self.start_time = tk.StringVar(value="0")
#         self.end_time = tk.StringVar(value="60")
#         self.bg_color = tk.StringVar(value="white")
#         self.show_grid = tk.BooleanVar(value=True)
#         self.figure_width = tk.StringVar(value="10")
#         self.figure_height = tk.StringVar(value="6")
        
#         # Training variables
#         self.working_dir = tk.StringVar()
#         self.model_path = tk.StringVar()
#         self.data_config_path = tk.StringVar()
#         self.epochs = tk.StringVar(value="100")
        
#         self.create_widgets()
    
#     def create_widgets(self):
#         # Header
#         header_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
#         header_frame.pack(fill='x', padx=0, pady=0)
#         header_frame.pack_propagate(False)
        
#         header_label = tk.Label(header_frame, text="Scratcher 1.3 ©", 
#                                font=('Arial', 20, 'bold'), 
#                                fg='white', bg='#2c3e50')
#         header_label.pack(expand=True)
        
#         # Main content area
#         main_frame = tk.Frame(self.root, bg="#f8c6c6")
#         main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
#         # Create notebook for tabs
#         self.notebook = ttk.Notebook(main_frame)
#         self.notebook.pack(fill='both', expand=True, pady=(0, 20))
        
#         # Create tabs
#         self.create_detect_tab()
#         self.create_analyse_tab()
#         self.create_train_tab()
        
#         # Footer
#         footer_frame = tk.Frame(self.root, bg='#34495e', height=80)
#         footer_frame.pack(fill='x', side='bottom')
#         footer_frame.pack_propagate(False)
        
#         footer_text = "BarikLab\nCentre for NeuroScience\nIndian Institute of Science Bangalore"
#         footer_label = tk.Label(footer_frame, text=footer_text, 
#                                font=('Arial', 10), 
#                                fg='white', bg='#34495e', justify='center')
#         footer_label.pack(expand=True)
    
#     def create_detect_tab(self):
#         detect_frame = ttk.Frame(self.notebook)
#         self.notebook.add(detect_frame, text="DETECT")
        
#         # Create scrollable frame
#         canvas = tk.Canvas(detect_frame, bg='#2d2d2d')
#         scrollbar = ttk.Scrollbar(detect_frame, orient="vertical", command=canvas.yview)
#         scrollable_frame = ttk.Frame(canvas)
        
#         scrollable_frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#         )
        
#         canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#         canvas.configure(yscrollcommand=scrollbar.set)
        
#         # Input folder selection
#         input_frame = ttk.LabelFrame(scrollable_frame, text="Input Settings", padding=15)
#         input_frame.pack(fill='x', padx=20, pady=10)
        
#         ttk.Label(input_frame, text="Input Folder:", font=('Arial', 10, 'bold')).pack(anchor='w')
#         input_path_frame = ttk.Frame(input_frame)
#         input_path_frame.pack(fill='x', pady=5)
#         ttk.Entry(input_path_frame, textvariable=self.input_folder, width=60).pack(side='left', fill='x', expand=True)
#         ttk.Button(input_path_frame, text="Browse", 
#                   command=lambda: self.browse_folder(self.input_folder)).pack(side='right', padx=(5,0))
        
#         # Output folder selection
#         ttk.Label(input_frame, text="Output Folder:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(15,0))
#         output_path_frame = ttk.Frame(input_frame)
#         output_path_frame.pack(fill='x', pady=5)
#         ttk.Entry(output_path_frame, textvariable=self.output_folder, width=60).pack(side='left', fill='x', expand=True)
#         ttk.Button(output_path_frame, text="Browse", 
#                   command=lambda: self.browse_folder(self.output_folder)).pack(side='right', padx=(5,0))
        
#         # Model and FPS settings
#         settings_frame = ttk.LabelFrame(scrollable_frame, text="Detection Settings", padding=15)
#         settings_frame.pack(fill='x', padx=20, pady=10)
        
#         # Model selection
#         model_frame = ttk.Frame(settings_frame)
#         model_frame.pack(fill='x', pady=5)
#         ttk.Label(model_frame, text="Model:", font=('Arial', 10, 'bold')).pack(side='left')
#         model_combo = ttk.Combobox(model_frame, textvariable=self.selected_model, 
#                                   values=["Model 1.3"], state="readonly", width=20)
#         model_combo.pack(side='right')
#         model_combo.set("Model 1.3")
        
#         # FPS entry
#         fps_frame = ttk.Frame(settings_frame)
#         fps_frame.pack(fill='x', pady=5)
#         ttk.Label(fps_frame, text="FPS:", font=('Arial', 10, 'bold')).pack(side='left')
#         ttk.Entry(fps_frame, textvariable=self.fps_value, width=20).pack(side='right')
        
#         # Start Detection Button
#         button_frame = ttk.Frame(scrollable_frame)
#         button_frame.pack(pady=20)
#         detect_btn = ttk.Button(button_frame, text="Start Detection", 
#                                command=self.start_detection,
#                                style='Accent.TButton')
#         detect_btn.pack()
        
#         canvas.pack(side="left", fill="both", expand=True)
#         scrollbar.pack(side="right", fill="y")
    
#     def create_analyse_tab(self):
#         analyse_frame = ttk.Frame(self.notebook)
#         self.notebook.add(analyse_frame, text="ANALYSE")
        
#         # Create scrollable frame
#         canvas = tk.Canvas(analyse_frame, bg="#d8edf6")
#         scrollbar = ttk.Scrollbar(analyse_frame, orient="vertical", command=canvas.yview)
#         scrollable_frame = ttk.Frame(canvas)
        
#         scrollable_frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#         )
        
#         canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#         canvas.configure(yscrollcommand=scrollbar.set)
        
#         # Input/Output folders
#         io_frame = ttk.LabelFrame(scrollable_frame, text="Input/Output Settings", padding=15)
#         io_frame.pack(fill='x', padx=20, pady=10)
        
#         ttk.Label(io_frame, text="Input Folder:", font=('Arial', 10, 'bold')).pack(anchor='w')
#         input_path_frame = ttk.Frame(io_frame)
#         input_path_frame.pack(fill='x', pady=5)
#         ttk.Entry(input_path_frame, textvariable=self.analysis_input_folder, width=60).pack(side='left', fill='x', expand=True)
#         ttk.Button(input_path_frame, text="Browse", 
#                   command=lambda: self.browse_folder(self.analysis_input_folder)).pack(side='right', padx=(5,0))
        
#         ttk.Label(io_frame, text="Output Folder:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(15,0))
#         output_path_frame = ttk.Frame(io_frame)
#         output_path_frame.pack(fill='x', pady=5)
#         ttk.Entry(output_path_frame, textvariable=self.analysis_output_folder, width=60).pack(side='left', fill='x', expand=True)
#         ttk.Button(output_path_frame, text="Browse", 
#                   command=lambda: self.browse_folder(self.analysis_output_folder)).pack(side='right', padx=(5,0))
        
#         # Video selection and settings
#         video_frame = ttk.LabelFrame(scrollable_frame, text="Video Selection & Settings", padding=15)
#         video_frame.pack(fill='x', padx=20, pady=10)
        
#         # Video selection and settings
#         video_frame = ttk.LabelFrame(scrollable_frame, text="Video Selection & Settings", padding=15)
#         video_frame.pack(fill='x', padx=20, pady=10)
        
#         # Default video entry with alias and color
#         default_video_frame = ttk.LabelFrame(video_frame, text="Default Video Configuration", padding=10)
#         default_video_frame.pack(fill='x', pady=(0,15))
        
#         # Video 1 settings
#         video1_frame = ttk.Frame(default_video_frame)
#         video1_frame.pack(fill='x', pady=5)
        
#         ttk.Label(video1_frame, text="Video 1 Alias:", font=('Arial', 10, 'bold')).pack(side='left')
#         self.video1_alias = tk.StringVar(value="Control")
#         ttk.Entry(video1_frame, textvariable=self.video1_alias, width=15).pack(side='left', padx=(10,20))
        
#         self.video1_color = tk.StringVar(value="#3498db")
#         self.video1_color_label = tk.Label(video1_frame, text="●", font=('Arial', 20), fg=self.video1_color.get())
#         self.video1_color_label.pack(side='left', padx=5)
#         ttk.Button(video1_frame, text="Choose Color", 
#                   command=lambda: self.choose_default_color(1)).pack(side='left', padx=5)
        
#         # Add more videos button
#         add_video_btn = ttk.Button(default_video_frame, text="+ Add Another Video", 
#                                   command=self.add_video_config)
#         add_video_btn.pack(pady=10)
        
#         # Container for additional videos
#         self.additional_videos_frame = ttk.Frame(default_video_frame)
#         self.additional_videos_frame.pack(fill='x')
#         self.video_configs = []
        
#         ttk.Button(video_frame, text="Select Videos from Folder", command=self.select_videos).pack(pady=10)
        
#         # Time settings - centered
#         time_label_frame = ttk.Frame(video_frame)
#         time_label_frame.pack(pady=(15,5))
#         ttk.Label(time_label_frame, text="Time Range Settings", font=('Arial', 11, 'bold')).pack()
        
#         time_frame = ttk.Frame(video_frame)
#         time_frame.pack(pady=5)
        
#         # Center the time inputs
#         time_inner_frame = ttk.Frame(time_frame)
#         time_inner_frame.pack()
        
#         ttk.Label(time_inner_frame, text="Start Time (s):", font=('Arial', 10, 'bold')).pack(side='left', padx=(0,5))
#         ttk.Entry(time_inner_frame, textvariable=self.start_time, width=10).pack(side='left', padx=5)
        
#         ttk.Label(time_inner_frame, text="End Time (s):", font=('Arial', 10, 'bold')).pack(side='left', padx=(20,5))
#         ttk.Entry(time_inner_frame, textvariable=self.end_time, width=10).pack(side='left', padx=5)
        
#         # Analysis options - centered
#         analysis_frame = ttk.LabelFrame(scrollable_frame, text="Analysis Options", padding=15)
#         analysis_frame.pack(fill='x', padx=20, pady=10)
        
#         analyses = [
#             "Peak scratching duration",
#             "Latency to itch onset", 
#             "Area under the curve (scratching over time)",
#             "Slope of scratching session (rate of increase or decrease)",
#             "Heatmap - scratching duration per minute",
#             "Line chart showing the full session trace for each selected video",
#             "Fiber Photometry Output"
#         ]
        
#         self.analysis_vars = {}
#         # Create two columns for better layout
#         col1_frame = ttk.Frame(analysis_frame)
#         col2_frame = ttk.Frame(analysis_frame)
#         col1_frame.pack(side='left', fill='both', expand=True, padx=(0,10))
#         col2_frame.pack(side='right', fill='both', expand=True, padx=(10,0))
        
#         for i, analysis in enumerate(analyses):
#             var = tk.BooleanVar()
#             self.analysis_vars[analysis] = var
#             target_frame = col1_frame if i < 4 else col2_frame
#             ttk.Checkbutton(target_frame, text=analysis, variable=var).pack(anchor='w', pady=3)
        
#         # Plot settings - centered layout
#         plot_frame = ttk.LabelFrame(scrollable_frame, text="Plot Settings", padding=15)
#         plot_frame.pack(fill='x', padx=20, pady=10)
        
#         # Center all plot settings
#         plot_center_frame = ttk.Frame(plot_frame)
#         plot_center_frame.pack()
        
#         # Background color
#         bg_frame = ttk.Frame(plot_center_frame)
#         bg_frame.pack(pady=8)
#         ttk.Label(bg_frame, text="Background Color:", font=('Arial', 10, 'bold')).pack(side='left', padx=(0,10))
#         bg_combo = ttk.Combobox(bg_frame, textvariable=self.bg_color, 
#                                values=["white", "black"], state="readonly", width=15)
#         bg_combo.pack(side='left')
        
#         # Grid lines
#         grid_frame = ttk.Frame(plot_center_frame)
#         grid_frame.pack(pady=8)
#         ttk.Checkbutton(grid_frame, text="Show Grid Lines", variable=self.show_grid).pack()
        
#         # Figure size
#         fig_frame = ttk.Frame(plot_center_frame)
#         fig_frame.pack(pady=8)
#         ttk.Label(fig_frame, text="Figure Size:", font=('Arial', 10, 'bold')).pack(pady=(0,5))
        
#         size_inputs = ttk.Frame(fig_frame)
#         size_inputs.pack()
#         ttk.Label(size_inputs, text="Width:").pack(side='left')
#         ttk.Entry(size_inputs, textvariable=self.figure_width, width=8).pack(side='left', padx=(5,15))
#         ttk.Label(size_inputs, text="Height:").pack(side='left')
#         ttk.Entry(size_inputs, textvariable=self.figure_height, width=8).pack(side='left', padx=5)
        
#         # Start Analysis Button
#         button_frame = ttk.Frame(scrollable_frame)
#         button_frame.pack(pady=20)
#         analyse_btn = ttk.Button(button_frame, text="Start Analysis", 
#                                 command=self.start_analysis,
#                                 style='Accent.TButton')
#         analyse_btn.pack()
        
#         canvas.pack(side="left", fill="both", expand=True)
#         scrollbar.pack(side="right", fill="y")
    
#     def create_train_tab(self):
#         train_frame = ttk.Frame(self.notebook)
#         self.notebook.add(train_frame, text="TRAIN")
        
#         # Create scrollable frame
#         canvas = tk.Canvas(train_frame, bg="#f6d1d1")
#         scrollbar = ttk.Scrollbar(train_frame, orient="vertical", command=canvas.yview)
#         scrollable_frame = ttk.Frame(canvas)
        
#         scrollable_frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#         )
        
#         canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#         canvas.configure(yscrollcommand=scrollbar.set)
        
#         # Training settings
#         train_settings_frame = ttk.LabelFrame(scrollable_frame, text="Training Configuration", padding=15)
#         train_settings_frame.pack(fill='x', padx=20, pady=20)
        
#         # Working Directory
#         ttk.Label(train_settings_frame, text="Working Directory:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0,5))
#         wd_frame = ttk.Frame(train_settings_frame)
#         wd_frame.pack(fill='x', pady=(0,15))
#         ttk.Entry(wd_frame, textvariable=self.working_dir, width=60).pack(side='left', fill='x', expand=True)
#         ttk.Button(wd_frame, text="Browse", 
#                   command=lambda: self.browse_folder(self.working_dir)).pack(side='right', padx=(5,0))
        
#         # SCRATCHER Model Path
#         ttk.Label(train_settings_frame, text="SCRATCHER Model Path:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0,5))
#         model_frame = ttk.Frame(train_settings_frame)
#         model_frame.pack(fill='x', pady=(0,15))
#         ttk.Entry(model_frame, textvariable=self.model_path, width=60).pack(side='left', fill='x', expand=True)
#         ttk.Button(model_frame, text="Browse", 
#                   command=lambda: self.browse_file(self.model_path)).pack(side='right', padx=(5,0))
        
#         # Data Configuration Path
#         ttk.Label(train_settings_frame, text="Data Configuration Path:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0,5))
#         config_frame = ttk.Frame(train_settings_frame)
#         config_frame.pack(fill='x', pady=(0,15))
#         ttk.Entry(config_frame, textvariable=self.data_config_path, width=60).pack(side='left', fill='x', expand=True)
#         ttk.Button(config_frame, text="Browse", 
#                   command=lambda: self.browse_file(self.data_config_path)).pack(side='right', padx=(5,0))
        
#         # Number of epochs
#         epochs_frame = ttk.Frame(train_settings_frame)
#         epochs_frame.pack(fill='x', pady=(0,15))
#         ttk.Label(epochs_frame, text="Number of Epochs:", font=('Arial', 10, 'bold')).pack(side='left')
#         ttk.Entry(epochs_frame, textvariable=self.epochs, width=20).pack(side='right')
        
#         # Start Training Button
#         button_frame = ttk.Frame(scrollable_frame)
#         button_frame.pack(pady=30)
#         train_btn = ttk.Button(button_frame, text="Start Training", 
#                               command=self.start_training,
#                               style='Accent.TButton')
#         train_btn.pack()
        
#         canvas.pack(side="left", fill="both", expand=True)
#         scrollbar.pack(side="right", fill="y")
    
#     def add_video_config(self):
#         video_num = len(self.video_configs) + 2
        
#         video_frame = ttk.Frame(self.additional_videos_frame)
#         video_frame.pack(fill='x', pady=5)
        
#         ttk.Label(video_frame, text=f"Video {video_num} Alias:", font=('Arial', 10, 'bold')).pack(side='left')
        
#         alias_var = tk.StringVar(value=f"Test_{video_num}")
#         ttk.Entry(video_frame, textvariable=alias_var, width=15).pack(side='left', padx=(10,20))
        
#         color_var = tk.StringVar(value=f"#{hex(hash(f'video{video_num}') % 16777215)[2:].zfill(6)}")
#         color_label = tk.Label(video_frame, text="●", font=('Arial', 20), fg=color_var.get())
#         color_label.pack(side='left', padx=5)
        
#         ttk.Button(video_frame, text="Choose Color", 
#                   command=lambda: self.choose_video_color(video_num, color_var, color_label)).pack(side='left', padx=5)
        
#         ttk.Button(video_frame, text="Remove", 
#                   command=lambda: self.remove_video_config(video_frame, video_num)).pack(side='right', padx=5)
        
#         self.video_configs.append({
#             'frame': video_frame,
#             'alias': alias_var,
#             'color': color_var,
#             'label': color_label,
#             'number': video_num
#         })
    
#     def choose_default_color(self, video_num):
#         color = colorchooser.askcolor(title=f"Choose color for Video {video_num}")
#         if color[1]:
#             if video_num == 1:
#                 self.video1_color.set(color[1])
#                 self.video1_color_label.config(fg=color[1])
    
#     def choose_video_color(self, video_num, color_var, color_label):
#         color = colorchooser.askcolor(title=f"Choose color for Video {video_num}")
#         if color[1]:
#             color_var.set(color[1])
#             color_label.config(fg=color[1])
    
#     def remove_video_config(self, frame, video_num):
#         frame.destroy()
#         self.video_configs = [config for config in self.video_configs if config['number'] != video_num]
#         folder = filedialog.askdirectory()
#         if folder:
#             var.set(folder)
    
#     def browse_file(self, var):
#         file = filedialog.askopenfilename()
#         if file:
#             var.set(file)
    
#     def select_videos(self):
#         if not self.analysis_input_folder.get():
#             messagebox.showwarning("Warning", "Please select input folder first!")
#             return
        
#         video_window = tk.Toplevel(self.root)
#         video_window.title("Select Videos")
#         video_window.geometry("600x500")
        
#         # List available videos
#         try:
#             video_files = [f for f in os.listdir(self.analysis_input_folder.get()) 
#                           if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
#         except:
#             video_files = ["sample_video1.mp4", "sample_video2.mp4"]  # Fallback for demo
        
#         ttk.Label(video_window, text="Select Videos and Assign Colors/Aliases:", 
#                  font=('Arial', 12, 'bold')).pack(pady=10)
        
#         # Create frame for video list
#         list_frame = ttk.Frame(video_window)
#         list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
#         self.video_vars = {}
#         self.video_alias_entries = {}
        
#         for i, video in enumerate(video_files):
#             video_frame = ttk.Frame(list_frame)
#             video_frame.pack(fill='x', pady=5)
            
#             # Checkbox for selection
#             var = tk.BooleanVar()
#             self.video_vars[video] = var
#             ttk.Checkbutton(video_frame, text=video, variable=var).pack(side='left')
            
#             # Alias entry
#             ttk.Label(video_frame, text="Alias:").pack(side='left', padx=(20,5))
#             alias_entry = ttk.Entry(video_frame, width=15)
#             alias_entry.pack(side='left', padx=5)
#             self.video_alias_entries[video] = alias_entry
            
#             # Color picker
#             color_btn = ttk.Button(video_frame, text="Choose Color", 
#                                   command=lambda v=video: self.choose_color(v))
#             color_btn.pack(side='right', padx=5)
        
#         # Confirm button
#         ttk.Button(video_window, text="Confirm Selection", 
#                   command=lambda: self.confirm_video_selection(video_window)).pack(pady=20)
    
#     def choose_color(self, video):
#         color = colorchooser.askcolor(title=f"Choose color for {video}")
#         if color[1]:  # If color was selected
#             self.video_colors[video] = color[1]
#             messagebox.showinfo("Color Selected", f"Color {color[1]} assigned to {video}")
    
#     def confirm_video_selection(self, window):
#         self.selected_videos = []
#         for video, var in self.video_vars.items():
#             if var.get():
#                 self.selected_videos.append(video)
#                 alias = self.video_alias_entries[video].get()
#                 if alias:
#                     self.video_aliases[video] = alias
        
#         if self.selected_videos:
#             messagebox.showinfo("Success", f"Selected {len(self.selected_videos)} videos")
#             window.destroy()
#         else:
#             messagebox.showwarning("Warning", "Please select at least one video!")
    
#     def start_detection(self):
#         if not self.input_folder.get() or not self.output_folder.get():
#             messagebox.showwarning("Warning", "Please select both input and output folders!")
#             return
        
#         # Here you would integrate your actual detection code
#         messagebox.showinfo("Detection Started", 
#                            f"Detection started with:\nModel: {self.selected_model.get()}\n"
#                            f"FPS: {self.fps_value.get()}\n"
#                            f"Input: {self.input_folder.get()}\n"
#                            f"Output: {self.output_folder.get()}")
    
#     def start_analysis(self):
#         if not self.selected_videos:
#             messagebox.showwarning("Warning", "Please select videos first!")
#             return
        
#         selected_analyses = [analysis for analysis, var in self.analysis_vars.items() if var.get()]
#         if not selected_analyses:
#             messagebox.showwarning("Warning", "Please select at least one analysis option!")
#             return
        
#         # Here you would integrate your actual analysis code
#         messagebox.showinfo("Analysis Started", 
#                            f"Analysis started with {len(selected_analyses)} analysis types\n"
#                            f"for {len(self.selected_videos)} videos")
    
#     def start_training(self):
#         if not all([self.working_dir.get(), self.model_path.get(), 
#                    self.data_config_path.get(), self.epochs.get()]):
#             messagebox.showwarning("Warning", "Please fill in all training parameters!")
#             return
        
#         # Here you would integrate your actual training code
#         messagebox.showinfo("Training Started", 
#                            f"Training started with {self.epochs.get()} epochs")

# def main():
#     root = tk.Tk()
    
#     # Configure style for modern dark theme
#     style = ttk.Style()
#     style.theme_use('clam')
    
#     # Configure modern dark theme colors
#     style.configure('TFrame', background="#b9e1f1")
#     style.configure('TLabel', background="#b1e5ef", foreground='#ffffff')
#     style.configure('TLabelFrame', background='#b1e5ef', foreground='#ffffff')
#     style.configure('TLabelFrame.Label', background='#b1e5ef', foreground='#4a9eff')
#     style.configure('TCheckbutton', background='#b1e5ef', foreground='#ffffff')
#     style.configure('TEntry', fieldbackground='#b1e5ef', foreground='#ffffff', bordercolor='#555555')
#     style.configure('TCombobox', fieldbackground='#b1e5ef', foreground='#ffffff', bordercolor='#555555')
#     style.configure('TButton', background='#4a9eff', foreground='#ffffff', bordercolor='#4a9eff')
#     style.map('TButton', background=[('active', '#357abd')])
    
#     # Configure custom accent button style
#     style.configure('Accent.TButton', 
#                    background='#4a9eff',
#                    foreground='white',
#                    font=('Arial', 12, 'bold'),
#                    padding=(25, 12),
#                    bordercolor='#4a9eff')
#     style.map('Accent.TButton', 
#               background=[('active', '#357abd')],
#               bordercolor=[('active', '#357abd')])
    
#     app = ScratcherGUI(root)
    
#     # Center the window
#     root.update_idletasks()
#     x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
#     y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
#     root.geometry(f"+{x}+{y}")
    
#     root.mainloop()

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
import os

class ScratcherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scratcher 1.3 ©")
        self.root.geometry("1000x750")
        self.root.configure(bg='#f8f9fa')
        
        # Variables for storing paths and settings
        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        self.fps_value = tk.StringVar(value="30")
        self.custom_model_path = tk.StringVar(value="best.pt")
        
        # Analysis variables
        self.analysis_input_folder = tk.StringVar()
        self.analysis_output_folder = tk.StringVar()
        self.video_colors = {}
        self.video_aliases = {}
        self.selected_videos = []
        self.start_time = tk.StringVar(value="0")
        self.end_time = tk.StringVar(value="60")
        self.bg_color = tk.StringVar(value="white")
        self.show_grid = tk.BooleanVar(value=True)
        self.figure_width = tk.StringVar(value="10")
        self.figure_height = tk.StringVar(value="6")
        
        # Training variables
        self.working_dir = tk.StringVar()
        self.model_path = tk.StringVar()
        self.data_config_path = tk.StringVar()
        self.epochs = tk.StringVar(value="100")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(header_frame, text="Scratcher 1.3 ©", 
                               font=('Arial', 20, 'bold'), 
                               fg='white', bg='#2c3e50')
        header_label.pack(expand=True)
        
        # Main content area
        main_frame = tk.Frame(self.root, bg='#f8f9fa')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True, pady=(0, 20))
        
        # Create tabs
        self.create_detect_tab()
        self.create_analyse_tab()
        self.create_train_tab()
        
        # Footer
        footer_frame = tk.Frame(self.root, bg='#34495e', height=80)
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        
        footer_text = "BarikLab\nCentre for NeuroScience\nIndian Institute of Science Bangalore"
        footer_label = tk.Label(footer_frame, text=footer_text, 
                               font=('Arial', 10), 
                               fg='white', bg='#34495e', justify='center')
        footer_label.pack(expand=True)
    
    def create_detect_tab(self):
        detect_frame = ttk.Frame(self.notebook)
        self.notebook.add(detect_frame, text="DETECT")
        
        # Create scrollable frame
        canvas = tk.Canvas(detect_frame, bg='white')
        scrollbar = ttk.Scrollbar(detect_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Input folder selection
        input_frame = ttk.LabelFrame(scrollable_frame, text="Input Settings", padding=15)
        input_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(input_frame, text="Input Folder:", font=('Arial', 10, 'bold')).pack(anchor='w')
        input_path_frame = ttk.Frame(input_frame)
        input_path_frame.pack(fill='x', pady=5)
        ttk.Entry(input_path_frame, textvariable=self.input_folder, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(input_path_frame, text="Browse", 
                  command=lambda: self.browse_folder(self.input_folder)).pack(side='right', padx=(5,0))
        
        # Output folder selection
        ttk.Label(input_frame, text="Output Folder:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(15,0))
        output_path_frame = ttk.Frame(input_frame)
        output_path_frame.pack(fill='x', pady=5)
        ttk.Entry(output_path_frame, textvariable=self.output_folder, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(output_path_frame, text="Browse", 
                  command=lambda: self.browse_folder(self.output_folder)).pack(side='right', padx=(5,0))
        
        # Model and FPS settings
        settings_frame = ttk.LabelFrame(scrollable_frame, text="Detection Settings", padding=15)
        settings_frame.pack(fill='x', padx=20, pady=10)
        
        # Model selection
        model_frame = ttk.Frame(settings_frame)
        model_frame.pack(fill='x', pady=5)
        ttk.Label(model_frame, text="YOLO Model (.pt):", font=('Arial', 10, 'bold')).pack(side='left')
        
        # Add browse button and entry for model
        ttk.Button(model_frame, text="Browse", 
                  command=lambda: self.browse_file(self.custom_model_path)).pack(side='right', padx=(5,0))
        ttk.Entry(model_frame, textvariable=self.custom_model_path, width=40).pack(side='right', fill='x', expand=True)
        
        # FPS entry
        fps_frame = ttk.Frame(settings_frame)
        fps_frame.pack(fill='x', pady=5)
        ttk.Label(fps_frame, text="FPS:", font=('Arial', 10, 'bold')).pack(side='left')
        ttk.Entry(fps_frame, textvariable=self.fps_value, width=20).pack(side='right')
        
        # Start Detection Button
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=20)
        detect_btn = ttk.Button(button_frame, text="Start Detection", 
                               command=self.start_detection,
                               style='Accent.TButton')
        detect_btn.pack()
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_analyse_tab(self):
        analyse_frame = ttk.Frame(self.notebook)
        self.notebook.add(analyse_frame, text="ANALYSE")
        
        # Create scrollable frame
        canvas = tk.Canvas(analyse_frame, bg='white')
        scrollbar = ttk.Scrollbar(analyse_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Input/Output folders
        io_frame = ttk.LabelFrame(scrollable_frame, text="Input/Output Settings", padding=15)
        io_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(io_frame, text="Input Folder:", font=('Arial', 10, 'bold')).pack(anchor='w')
        input_path_frame = ttk.Frame(io_frame)
        input_path_frame.pack(fill='x', pady=5)
        ttk.Entry(input_path_frame, textvariable=self.analysis_input_folder, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(input_path_frame, text="Browse", 
                  command=lambda: self.browse_folder(self.analysis_input_folder)).pack(side='right', padx=(5,0))
        
        ttk.Label(io_frame, text="Output Folder:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(15,0))
        output_path_frame = ttk.Frame(io_frame)
        output_path_frame.pack(fill='x', pady=5)
        ttk.Entry(output_path_frame, textvariable=self.analysis_output_folder, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(output_path_frame, text="Browse", 
                  command=lambda: self.browse_folder(self.analysis_output_folder)).pack(side='right', padx=(5,0))
        
        # Video selection and settings
        video_frame = ttk.LabelFrame(scrollable_frame, text="Video Selection & Settings", padding=15)
        video_frame.pack(fill='x', padx=20, pady=10)
        
        # Video selection and settings
        video_frame = ttk.LabelFrame(scrollable_frame, text="Video Selection & Settings", padding=15)
        video_frame.pack(fill='x', padx=20, pady=10)
        
        # Default video entry with alias and color
        default_video_frame = ttk.LabelFrame(video_frame, text="Default Video Configuration", padding=10)
        default_video_frame.pack(fill='x', pady=(0,15))
        
        # Video 1 settings
        video1_frame = ttk.Frame(default_video_frame)
        video1_frame.pack(fill='x', pady=5)
        
        ttk.Label(video1_frame, text="Video 1 Alias:", font=('Arial', 10, 'bold')).pack(side='left')
        self.video1_alias = tk.StringVar(value="Control")
        ttk.Entry(video1_frame, textvariable=self.video1_alias, width=15).pack(side='left', padx=(10,20))
        
        self.video1_color = tk.StringVar(value="#3498db")
        self.video1_color_label = tk.Label(video1_frame, text="●", font=('Arial', 20), fg=self.video1_color.get())
        self.video1_color_label.pack(side='left', padx=5)
        ttk.Button(video1_frame, text="Choose Color", 
                  command=lambda: self.choose_default_color(1)).pack(side='left', padx=5)
        
        # Add more videos button
        add_video_btn = ttk.Button(default_video_frame, text="+ Add Another Video", 
                                  command=self.add_video_config)
        add_video_btn.pack(pady=10)
        
        # Container for additional videos
        self.additional_videos_frame = ttk.Frame(default_video_frame)
        self.additional_videos_frame.pack(fill='x')
        self.video_configs = []
        
        ttk.Button(video_frame, text="Select Videos from Folder", command=self.select_videos).pack(pady=10)
        
        # Time settings - centered
        time_label_frame = ttk.Frame(video_frame)
        time_label_frame.pack(pady=(15,5))
        ttk.Label(time_label_frame, text="Time Range Settings", font=('Arial', 11, 'bold')).pack()
        
        time_frame = ttk.Frame(video_frame)
        time_frame.pack(pady=5)
        
        # Center the time inputs
        time_inner_frame = ttk.Frame(time_frame)
        time_inner_frame.pack()
        
        ttk.Label(time_inner_frame, text="Start Time (s):", font=('Arial', 10, 'bold')).pack(side='left', padx=(0,5))
        ttk.Entry(time_inner_frame, textvariable=self.start_time, width=10).pack(side='left', padx=5)
        
        ttk.Label(time_inner_frame, text="End Time (s):", font=('Arial', 10, 'bold')).pack(side='left', padx=(20,5))
        ttk.Entry(time_inner_frame, textvariable=self.end_time, width=10).pack(side='left', padx=5)
        
        # Analysis options - centered
        analysis_frame = ttk.LabelFrame(scrollable_frame, text="Analysis Options", padding=15)
        analysis_frame.pack(fill='x', padx=20, pady=10)
        
        analyses = [
            "Peak scratching duration",
            "Latency to itch onset", 
            "Area under the curve (scratching over time)",
            "Slope of scratching session (rate of increase or decrease)",
            "Heatmap - scratching duration per minute",
            "Line chart showing the full session trace for each selected video",
            "Fiber Photometry Output"
        ]
        
        self.analysis_vars = {}
        # Create two columns for better layout
        col1_frame = ttk.Frame(analysis_frame)
        col2_frame = ttk.Frame(analysis_frame)
        col1_frame.pack(side='left', fill='both', expand=True, padx=(0,10))
        col2_frame.pack(side='right', fill='both', expand=True, padx=(10,0))
        
        for i, analysis in enumerate(analyses):
            var = tk.BooleanVar()
            self.analysis_vars[analysis] = var
            target_frame = col1_frame if i < 4 else col2_frame
            ttk.Checkbutton(target_frame, text=analysis, variable=var).pack(anchor='w', pady=3)
        
        # Plot settings - centered layout
        plot_frame = ttk.LabelFrame(scrollable_frame, text="Plot Settings", padding=15)
        plot_frame.pack(fill='x', padx=20, pady=10)
        
        # Center all plot settings
        plot_center_frame = ttk.Frame(plot_frame)
        plot_center_frame.pack()
        
        # Background color
        bg_frame = ttk.Frame(plot_center_frame)
        bg_frame.pack(pady=8)
        ttk.Label(bg_frame, text="Background Color:", font=('Arial', 10, 'bold')).pack(side='left', padx=(0,10))
        bg_combo = ttk.Combobox(bg_frame, textvariable=self.bg_color, 
                               values=["white", "black"], state="readonly", width=15)
        bg_combo.pack(side='left')
        
        # Grid lines
        grid_frame = ttk.Frame(plot_center_frame)
        grid_frame.pack(pady=8)
        ttk.Checkbutton(grid_frame, text="Show Grid Lines", variable=self.show_grid).pack()
        
        # Figure size
        fig_frame = ttk.Frame(plot_center_frame)
        fig_frame.pack(pady=8)
        ttk.Label(fig_frame, text="Figure Size:", font=('Arial', 10, 'bold')).pack(pady=(0,5))
        
        size_inputs = ttk.Frame(fig_frame)
        size_inputs.pack()
        ttk.Label(size_inputs, text="Width:").pack(side='left')
        ttk.Entry(size_inputs, textvariable=self.figure_width, width=8).pack(side='left', padx=(5,15))
        ttk.Label(size_inputs, text="Height:").pack(side='left')
        ttk.Entry(size_inputs, textvariable=self.figure_height, width=8).pack(side='left', padx=5)
        
        # Start Analysis Button
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=20)
        analyse_btn = ttk.Button(button_frame, text="Start Analysis", 
                                command=self.start_analysis,
                                style='Accent.TButton')
        analyse_btn.pack()
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_train_tab(self):
        train_frame = ttk.Frame(self.notebook)
        self.notebook.add(train_frame, text="TRAIN")
        
        # Create scrollable frame
        canvas = tk.Canvas(train_frame, bg='white')
        scrollbar = ttk.Scrollbar(train_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Training settings
        train_settings_frame = ttk.LabelFrame(scrollable_frame, text="Training Configuration", padding=15)
        train_settings_frame.pack(fill='x', padx=20, pady=20)
        
        # Working Directory
        ttk.Label(train_settings_frame, text="Working Directory:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0,5))
        wd_frame = ttk.Frame(train_settings_frame)
        wd_frame.pack(fill='x', pady=(0,15))
        ttk.Entry(wd_frame, textvariable=self.working_dir, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(wd_frame, text="Browse", 
                  command=lambda: self.browse_folder(self.working_dir)).pack(side='right', padx=(5,0))
        
        # SCRATCHER Model Path
        ttk.Label(train_settings_frame, text="SCRATCHER Model Path:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0,5))
        model_frame = ttk.Frame(train_settings_frame)
        model_frame.pack(fill='x', pady=(0,15))
        ttk.Entry(model_frame, textvariable=self.model_path, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(model_frame, text="Browse", 
                  command=lambda: self.browse_file(self.model_path)).pack(side='right', padx=(5,0))
        
        # Data Configuration Path
        ttk.Label(train_settings_frame, text="Data Configuration Path:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(0,5))
        config_frame = ttk.Frame(train_settings_frame)
        config_frame.pack(fill='x', pady=(0,15))
        ttk.Entry(config_frame, textvariable=self.data_config_path, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(config_frame, text="Browse", 
                  command=lambda: self.browse_file(self.data_config_path)).pack(side='right', padx=(5,0))
        
        # Number of epochs
        epochs_frame = ttk.Frame(train_settings_frame)
        epochs_frame.pack(fill='x', pady=(0,15))
        ttk.Label(epochs_frame, text="Number of Epochs:", font=('Arial', 10, 'bold')).pack(side='left')
        ttk.Entry(epochs_frame, textvariable=self.epochs, width=20).pack(side='right')
        
        # Start Training Button
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=30)
        train_btn = ttk.Button(button_frame, text="Start Training", 
                              command=self.start_training,
                              style='Accent.TButton')
        train_btn.pack()
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def add_video_config(self):
        video_num = len(self.video_configs) + 2
        
        video_frame = ttk.Frame(self.additional_videos_frame)
        video_frame.pack(fill='x', pady=5)
        
        ttk.Label(video_frame, text=f"Video {video_num} Alias:", font=('Arial', 10, 'bold')).pack(side='left')
        
        alias_var = tk.StringVar(value=f"Test_{video_num}")
        ttk.Entry(video_frame, textvariable=alias_var, width=15).pack(side='left', padx=(10,20))
        
        color_var = tk.StringVar(value=f"#{hex(hash(f'video{video_num}') % 16777215)[2:].zfill(6)}")
        color_label = tk.Label(video_frame, text="●", font=('Arial', 20), fg=color_var.get())
        color_label.pack(side='left', padx=5)
        
        ttk.Button(video_frame, text="Choose Color", 
                  command=lambda: self.choose_video_color(video_num, color_var, color_label)).pack(side='left', padx=5)
        
        ttk.Button(video_frame, text="Remove", 
                  command=lambda: self.remove_video_config(video_frame, video_num)).pack(side='right', padx=5)
        
        self.video_configs.append({
            'frame': video_frame,
            'alias': alias_var,
            'color': color_var,
            'label': color_label,
            'number': video_num
        })
    
    def choose_default_color(self, video_num):
        color = colorchooser.askcolor(title=f"Choose color for Video {video_num}")
        if color[1]:
            if video_num == 1:
                self.video1_color.set(color[1])
                self.video1_color_label.config(fg=color[1])
    
    def choose_video_color(self, video_num, color_var, color_label):
        color = colorchooser.askcolor(title=f"Choose color for Video {video_num}")
        if color[1]:
            color_var.set(color[1])
            color_label.config(fg=color[1])
    
    def remove_video_config(self, frame, video_num):
        frame.destroy()
        self.video_configs = [config for config in self.video_configs if config['number'] != video_num]
        
    def browse_folder(self, var):
        folder = filedialog.askdirectory()
        if folder:
            var.set(folder)
    
    def browse_file(self, var):
        file = filedialog.askopenfilename()
        if file:
            var.set(file)
    
    def select_videos(self):
        if not self.analysis_input_folder.get():
            messagebox.showwarning("Warning", "Please select input folder first!")
            return
        
        video_window = tk.Toplevel(self.root)
        video_window.title("Select Videos")
        video_window.geometry("600x500")
        
        # List available videos
        try:
            video_files = [f for f in os.listdir(self.analysis_input_folder.get()) 
                          if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
        except:
            video_files = ["sample_video1.mp4", "sample_video2.mp4"]  # Fallback for demo
        
        ttk.Label(video_window, text="Select Videos and Assign Colors/Aliases:", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Create frame for video list
        list_frame = ttk.Frame(video_window)
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.video_vars = {}
        self.video_alias_entries = {}
        
        for i, video in enumerate(video_files):
            video_frame = ttk.Frame(list_frame)
            video_frame.pack(fill='x', pady=5)
            
            # Checkbox for selection
            var = tk.BooleanVar()
            self.video_vars[video] = var
            ttk.Checkbutton(video_frame, text=video, variable=var).pack(side='left')
            
            # Alias entry
            ttk.Label(video_frame, text="Alias:").pack(side='left', padx=(20,5))
            alias_entry = ttk.Entry(video_frame, width=15)
            alias_entry.pack(side='left', padx=5)
            self.video_alias_entries[video] = alias_entry
            
            # Color picker
            color_btn = ttk.Button(video_frame, text="Choose Color", 
                                  command=lambda v=video: self.choose_color(v))
            color_btn.pack(side='right', padx=5)
        
        # Confirm button
        ttk.Button(video_window, text="Confirm Selection", 
                  command=lambda: self.confirm_video_selection(video_window)).pack(pady=20)
    
    def choose_color(self, video):
        color = colorchooser.askcolor(title=f"Choose color for {video}")
        if color[1]:  # If color was selected
            self.video_colors[video] = color[1]
            messagebox.showinfo("Color Selected", f"Color {color[1]} assigned to {video}")
    
    def confirm_video_selection(self, window):
        self.selected_videos = []
        for video, var in self.video_vars.items():
            if var.get():
                self.selected_videos.append(video)
                alias = self.video_alias_entries[video].get()
                if alias:
                    self.video_aliases[video] = alias
        
        if self.selected_videos:
            messagebox.showinfo("Success", f"Selected {len(self.selected_videos)} videos")
            window.destroy()
        else:
            messagebox.showwarning("Warning", "Please select at least one video!")
    
    def start_detection(self):
        if not self.input_folder.get() or not self.output_folder.get():
            messagebox.showwarning("Warning", "Please select both input and output folders!")
            return
        
        # Here you would integrate your actual detection code
        messagebox.showinfo("Detection Started", 
                           f"Detection started with:\nModel: {self.custom_model_path.get()}\n"
                           f"FPS: {self.fps_value.get()}\n"
                           f"Input: {self.input_folder.get()}\n"
                           f"Output: {self.output_folder.get()}")
    
    def start_analysis(self):
        if not self.selected_videos:
            messagebox.showwarning("Warning", "Please select videos first!")
            return
        
        selected_analyses = [analysis for analysis, var in self.analysis_vars.items() if var.get()]
        if not selected_analyses:
            messagebox.showwarning("Warning", "Please select at least one analysis option!")
            return
        
        # Here you would integrate your actual analysis code
        messagebox.showinfo("Analysis Started", 
                           f"Analysis started with {len(selected_analyses)} analysis types\n"
                           f"for {len(self.selected_videos)} videos")
    
    def start_training(self):
        if not all([self.working_dir.get(), self.model_path.get(), 
                   self.data_config_path.get(), self.epochs.get()]):
            messagebox.showwarning("Warning", "Please fill in all training parameters!")
            return
        
        # Here you would integrate your actual training code
        messagebox.showinfo("Training Started", 
                           f"Training started with {self.epochs.get()} epochs")

def main():
    root = tk.Tk()
    
    # Configure style for modern dark theme
    style = ttk.Style()
    style.theme_use('clam')
    
    # Configure modern dark theme colors
    # style.configure('TFrame', background="#ffffff")
    # style.configure('TLabel', background="#ffffff", foreground='#ffffff')
    # style.configure('TLabelFrame', background="#ffffff", foreground='#ffffff')
    # style.configure('TLabelFrame.Label', background='#2d2d2d', foreground='#4a9eff')
    # style.configure('TCheckbutton', background='#2d2d2d', foreground='#ffffff')
    # style.configure('TEntry', fieldbackground='#3d3d3d', foreground='#ffffff', bordercolor='#555555')
    # style.configure('TCombobox', fieldbackground='#3d3d3d', foreground='#ffffff', bordercolor='#555555')
    # style.configure('TButton', background='#4a9eff', foreground='#ffffff', bordercolor='#4a9eff')
    # style.map('TButton', background=[('active', '#357abd')])
    
    style.configure('TFrame', background="#ffffff")

    # style.configure('TLabel', background="#ffffff", foreground='#000000')
    # style.configure('TLabelFrame', background="#ffffff", foreground='#000000')
    style.configure('TLabelFrame.Label', background='#ffffff', foreground='#000000')

    style.configure('TCheckbutton', background='#ffffff', foreground='#000000')

    style.configure('TEntry', fieldbackground='#ffffff', foreground='#000000', bordercolor='#cccccc')

    style.configure('TCombobox', fieldbackground='#ffffff', foreground='#000000', bordercolor='#cccccc')

    style.configure('TButton', background="#31bbea", foreground='#000000', bordercolor='#cccccc')
    style.map('TButton', background=[('active', '#e6e6e6')])



    # Configure custom accent button style
    style.configure('Accent.TButton', 
                   background='#4a9eff',
                   foreground='white',
                   font=('Arial', 12, 'bold'),
                   padding=(25, 12),
                   bordercolor='#4a9eff')
    style.map('Accent.TButton', 
              background=[('active', '#357abd')],
              bordercolor=[('active', '#357abd')])
    
    app = ScratcherGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    

    root.mainloop()

if __name__ == "__main__":
    main()
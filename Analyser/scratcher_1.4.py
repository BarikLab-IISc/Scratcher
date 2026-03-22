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

        canvas = tk.Canvas(analyse_frame, bg='white')
        scrollbar = ttk.Scrollbar(analyse_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # ── 1. Input / Output ────────────────────────────────────────────────
        io_frame = ttk.LabelFrame(scrollable_frame, text="Input/Output Settings", padding=15)
        io_frame.pack(fill='x', padx=20, pady=10)

        ttk.Label(io_frame, text="Input Folder:", font=('Arial', 10, 'bold')).pack(anchor='w')
        input_path_frame = ttk.Frame(io_frame)
        input_path_frame.pack(fill='x', pady=5)
        ttk.Entry(input_path_frame, textvariable=self.analysis_input_folder, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(input_path_frame, text="Browse",
                   command=lambda: [self.browse_folder(self.analysis_input_folder),
                                    self.refresh_video_table()]).pack(side='right', padx=(5, 0))

        ttk.Label(io_frame, text="Output Folder:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(15, 0))
        output_path_frame = ttk.Frame(io_frame)
        output_path_frame.pack(fill='x', pady=5)
        ttk.Entry(output_path_frame, textvariable=self.analysis_output_folder, width=60).pack(side='left', fill='x', expand=True)
        ttk.Button(output_path_frame, text="Browse",
                   command=lambda: self.browse_folder(self.analysis_output_folder)).pack(side='right', padx=(5, 0))

        # ── 2. Analysis Options ──────────────────────────────────────────────
        analysis_frame = ttk.LabelFrame(scrollable_frame, text="Analysis Options", padding=15)
        analysis_frame.pack(fill='x', padx=20, pady=10)

        analyses = [
            "Itch Bout Frequency",
            "Slope of scratching session (rate of increase or decrease)",
            "Peak Scratching Duration",
            "Area Under the Curve (AUC)",
            "Entire Session Plot",
            "Latency to First Scratch",
            "Average Scratches per Mouse",
            "Heatmap (ΔF/F per Mouse)",
        ]

        self.analysis_vars = {}
        # two-column layout
        col1 = ttk.Frame(analysis_frame)
        col2 = ttk.Frame(analysis_frame)
        col1.pack(side='left', fill='both', expand=True)
        col2.pack(side='left', fill='both', expand=True)
        for i, analysis in enumerate(analyses):
            var = tk.BooleanVar()
            self.analysis_vars[analysis] = var
            target = col1 if i < 4 else col2
            ttk.Checkbutton(target, text=analysis, variable=var).pack(anchor='w', pady=3)

        # ── 3. Video Settings (auto-populated table) ─────────────────────────
        video_outer = ttk.LabelFrame(scrollable_frame, text="Video Selection & Settings", padding=15)
        video_outer.pack(fill='x', padx=20, pady=10)

        ttk.Label(video_outer,
                  text="Set the Input Folder above then click Refresh to load videos.",
                  font=('Arial', 9, 'italic')).pack(anchor='w')
        ttk.Button(video_outer, text="↻  Refresh Video List",
                   command=self.refresh_video_table).pack(anchor='w', pady=(4, 8))

        # Header row
        hdr = ttk.Frame(video_outer)
        hdr.pack(fill='x')
        for text, w in [("Include", 7), ("Video File", 26), ("Raster File", 34),
                        ("Alias", 14), ("Colour", 8), ("Start (s)", 9), ("End (s)", 9)]:
            ttk.Label(hdr, text=text, font=('Arial', 9, 'bold'), width=w, anchor='w').pack(side='left')

        # Scrollable area for rows
        tbl_canvas = tk.Canvas(video_outer, height=200, bg='white')
        tbl_sb = ttk.Scrollbar(video_outer, orient='vertical', command=tbl_canvas.yview)
        self.video_table_frame = ttk.Frame(tbl_canvas)
        self.video_table_frame.bind(
            "<Configure>",
            lambda e: tbl_canvas.configure(scrollregion=tbl_canvas.bbox("all"))
        )
        tbl_canvas.create_window((0, 0), window=self.video_table_frame, anchor='nw')
        tbl_canvas.configure(yscrollcommand=tbl_sb.set)
        tbl_canvas.pack(side='left', fill='both', expand=True)
        tbl_sb.pack(side='right', fill='y')

        # Storage for per-video widgets
        self.video_row_data = []   # list of dicts

        # ── 4. Plot Settings ─────────────────────────────────────────────────
        plot_frame = ttk.LabelFrame(scrollable_frame, text="Plot Settings", padding=15)
        plot_frame.pack(fill='x', padx=20, pady=10)

        plot_center_frame = ttk.Frame(plot_frame)
        plot_center_frame.pack()

        bg_frame = ttk.Frame(plot_center_frame)
        bg_frame.pack(pady=8)
        ttk.Label(bg_frame, text="Background Color:", font=('Arial', 10, 'bold')).pack(side='left', padx=(0, 10))
        ttk.Combobox(bg_frame, textvariable=self.bg_color,
                     values=["white", "black"], state="readonly", width=15).pack(side='left')

        grid_frame = ttk.Frame(plot_center_frame)
        grid_frame.pack(pady=8)
        ttk.Checkbutton(grid_frame, text="Show Grid Lines", variable=self.show_grid).pack()

        fig_frame = ttk.Frame(plot_center_frame)
        fig_frame.pack(pady=8)
        ttk.Label(fig_frame, text="Figure Size:", font=('Arial', 10, 'bold')).pack(pady=(0, 5))
        size_inputs = ttk.Frame(fig_frame)
        size_inputs.pack()
        ttk.Label(size_inputs, text="Width:").pack(side='left')
        ttk.Entry(size_inputs, textvariable=self.figure_width, width=8).pack(side='left', padx=(5, 15))
        ttk.Label(size_inputs, text="Height:").pack(side='left')
        ttk.Entry(size_inputs, textvariable=self.figure_height, width=8).pack(side='left', padx=5)

        # ── 5. Start Analysis Button ─────────────────────────────────────────
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=20)
        ttk.Button(button_frame, text="Start Analysis",
                   command=self.start_analysis,
                   style='Accent.TButton').pack()

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def refresh_video_table(self):
        """Populate / refresh the per-video settings table from the input folder."""
        folder = self.analysis_input_folder.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("Warning", "Please set a valid Input Folder first.")
            return

        # Clear existing rows
        for widget in self.video_table_frame.winfo_children():
            widget.destroy()
        self.video_row_data.clear()

        video_exts = ('.mp4', '.avi', '.mov', '.mkv')
        videos = sorted([f for f in os.listdir(folder) if f.lower().endswith(video_exts)])

        if not videos:
            ttk.Label(self.video_table_frame,
                      text="No video files found in the selected folder.",
                      foreground='red').pack(anchor='w', pady=4)
            return

        for video in videos:
            stem = os.path.splitext(video)[0]
            # Look for matching raster file
            raster_candidates = [f for f in os.listdir(folder)
                                  if f.endswith('.xlsx') and stem.lower() in f.lower()]
            raster_name = raster_candidates[0] if raster_candidates else "(not found)"

            row = ttk.Frame(self.video_table_frame)
            row.pack(fill='x', pady=2)

            include_var = tk.BooleanVar(value=True)
            ttk.Checkbutton(row, variable=include_var, width=5).pack(side='left')

            ttk.Label(row, text=video, width=26, anchor='w').pack(side='left')
            ttk.Label(row, text=raster_name, width=34, anchor='w',
                      foreground='gray' if raster_name == '(not found)' else 'black').pack(side='left')

            alias_var = tk.StringVar(value=stem)
            ttk.Entry(row, textvariable=alias_var, width=14).pack(side='left', padx=2)

            color_var = tk.StringVar(value='#3498db')
            color_lbl = tk.Label(row, text="  ", bg=color_var.get(), relief='raised', width=4)
            color_lbl.pack(side='left', padx=2)
            def _pick_color(cv=color_var, cl=color_lbl):
                result = colorchooser.askcolor(title="Choose colour", color=cv.get())
                if result and result[1]:
                    cv.set(result[1])
                    cl.config(bg=result[1])
            ttk.Button(row, text="🎨", width=3, command=_pick_color).pack(side='left', padx=2)

            start_var = tk.StringVar(value="0")
            end_var = tk.StringVar(value="")
            ttk.Entry(row, textvariable=start_var, width=8).pack(side='left', padx=2)
            ttk.Entry(row, textvariable=end_var, width=8).pack(side='left', padx=2)

            self.video_row_data.append({
                'video': video,
                'raster': raster_name,
                'include': include_var,
                'alias': alias_var,
                'color': color_var,
                'start': start_var,
                'end': end_var,
            })

    
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
        
        # Integrating YOLO Detection logic
        model_path = self.custom_model_path.get()
        
        input_folder = self.input_folder.get()
        output_folder = self.output_folder.get()
        
        try:
            fps_val = float(self.fps_value.get())
        except ValueError:
            messagebox.showerror("Error", "FPS must be a number.")
            return

        try:
            from ultralytics import YOLO
            from video_processing import process_video
            from behaviour_filtering import filter_behaviours
            from behaviour_analysis import analyse_behaviours
            import re
            
            # Validate model file
            if not model_path.endswith('.pt'):
                 messagebox.showerror("Error", "Model file must be a PyTorch (.pt) file.")
                 return
                 
            if not os.path.exists(model_path):
                messagebox.showerror("Error", f"Model file not found at: {model_path}\nPlease provide a valid YOLO model.")
                return
                
            try:
                # Load the model - verify it's a valid YOLO model
                model = YOLO(model_path)
            except Exception as e:
                messagebox.showerror("Model Error", f"Failed to load the model. Ensure it is a valid YOLO version compatible model.\nError: {e}")
                return
            
            # Support both .mp4 and .avi
            import glob
            video_files = glob.glob(os.path.join(input_folder, "*.mp4")) + glob.glob(os.path.join(input_folder, "*.avi"))
            
            if not video_files:
                messagebox.showwarning("Warning", "No .mp4 or .avi files found in the input folder.")
                return
                
            for video_path in video_files:
                video_file = os.path.basename(video_path)
                # handle both .mp4 and .avi extensions
                video_name = re.sub(r'\.(mp4|avi)$', '', video_file, flags=re.IGNORECASE)
                
                # Using a default confidence threshold of 0.6 since it's not in the 1.4 GUI
                process_video(model, video_path, output_folder, video_name, conf_threshold=0.6)

            # Filtering Behaviours
            excel_files = [f for f in os.listdir(output_folder) if f.endswith('.xlsx')]
            for excel_file in excel_files:
                input_path = os.path.join(output_folder, excel_file)
                output_path = os.path.join(output_folder, "raster_plot_input_" + excel_file)
                filter_behaviours(input_path, output_path)

            # Preliminary Analysis
            analyse_behaviours(output_folder)
            
            messagebox.showinfo("Detection Complete", 
                               f"Processing complete for {len(video_files)} video(s).\n"
                               f"Output saved to {output_folder}")
                               
        except ImportError as e:
            messagebox.showerror("Import Error", f"Missing dependency for detection: {e}\nEnsure ultralytics and other modules are installed.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during detection: {e}")
    
    def start_analysis(self):
        selected_analyses = [analysis for analysis, var in self.analysis_vars.items() if var.get()]
        if not selected_analyses:
            messagebox.showwarning("Warning", "Please select at least one analysis option!")
            return
        
        # Output summary of run
        results_msg = []
        
        # New Feature: Itch Bout Frequency
        if "Itch Bout Frequency" in selected_analyses:
            try:
                import bout_frequency_analysis
                processed = bout_frequency_analysis.analyze_bout_frequency(self.analysis_input_folder.get(), self.analysis_output_folder.get())
                results_msg.append(f"Itch Bout Frequency: Processed {processed} raster files.")
            except Exception as e:
                results_msg.append(f"Itch Bout Frequency Error: {e}")
                
        # New Feature: Slope of scratching session (individual mice)
        # Note: we assume the user selected this and configured the input folder containing an Excel file
        if "Slope of scratching session (rate of increase or decrease)" in selected_analyses:
            try:
                import slope_individual_mice
                import os
                # Look for an xlsx file in the input directory to use for slope
                file_path = filedialog.askopenfilename(
                    title="Select Excel File for Slope Regression Analysis",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialdir=self.analysis_input_folder.get()
                )
                
                if file_path:
                    # Successfully picked a file
                    output_path = os.path.join(self.analysis_output_folder.get(), f"slope_plot_{os.path.basename(file_path).replace('.xlsx', '.png')}")
                    print(f"DEBUG: Chosen file path: {file_path}")
                    print(f"DEBUG: Output path: {output_path}")
                    
                    success = slope_individual_mice.plot_slope_individual_mice(
                        file_path=file_path,
                        output_path=output_path,
                        bg_color=self.bg_color.get(),
                        fig_size=(float(self.figure_width.get()), float(self.figure_height.get()))
                    )
                    
                    print(f"DEBUG: Success boolean: {success}")
                    if success:
                        results_msg.append(f"Slope Plotting: Saved to {output_path}")
                    else:
                        results_msg.append("Slope Plotting: Failed during plotting.")
                else:
                    results_msg.append("Slope Plotting: Cancelled by user.")
            except Exception as e:
                print(f"DEBUG: Slope Exception caught in GUI script: {e}")
                results_msg.append(f"Slope Plotting Error: {e}")
        
        # Peak Scratching Duration
        if "Peak Scratching Duration" in selected_analyses:
            try:
                import peak_scratch_duration
                import os
                file_path = filedialog.askopenfilename(
                    title="Select Excel File for Peak Scratch Duration",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialdir=self.analysis_input_folder.get()
                )
                if file_path:
                    output_path = os.path.join(
                        self.analysis_output_folder.get(),
                        f"peak_scratch_{os.path.basename(file_path).replace('.xlsx', '.png')}"
                    )
                    success = peak_scratch_duration.plot_peak_scratch_duration(
                        file_path=file_path,
                        output_path=output_path,
                        fig_size=(float(self.figure_width.get()), float(self.figure_height.get()))
                    )
                    if success:
                        results_msg.append(f"Peak Scratch Duration: Saved to {output_path}")
                    else:
                        results_msg.append("Peak Scratch Duration: Failed during plotting.")
                else:
                    results_msg.append("Peak Scratch Duration: Cancelled by user.")
            except Exception as e:
                print(f"DEBUG: Peak Scratch Duration Error: {e}")
                results_msg.append(f"Peak Scratch Duration Error: {e}")
        
        # Area Under the Curve (AUC)
        if "Area Under the Curve (AUC)" in selected_analyses:
            try:
                import auc_analysis
                import os
                file_path = filedialog.askopenfilename(
                    title="Select Excel File for AUC Analysis",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialdir=self.analysis_input_folder.get()
                )
                if file_path:
                    output_path = os.path.join(
                        self.analysis_output_folder.get(),
                        f"auc_{os.path.basename(file_path).replace('.xlsx', '.png')}"
                    )
                    success = auc_analysis.plot_auc(
                        file_path=file_path,
                        output_path=output_path,
                        fig_size=(float(self.figure_width.get()), float(self.figure_height.get()))
                    )
                    if success:
                        results_msg.append(f"AUC: Saved to {output_path}")
                    else:
                        results_msg.append("AUC: Failed during plotting.")
                else:
                    results_msg.append("AUC: Cancelled by user.")
            except Exception as e:
                print(f"DEBUG: AUC Error: {e}")
                results_msg.append(f"AUC Error: {e}")
        
        # Entire Session Plot
        if "Entire Session Plot" in selected_analyses:
            try:
                import entire_session_plot
                import os
                groups = []
                while True:
                    file_path = filedialog.askopenfilename(
                        title=f"Select Excel File for Group {len(groups)+1} (Cancel to finish)",
                        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                        initialdir=self.analysis_input_folder.get()
                    )
                    if not file_path:
                        break  # user cancelled – done adding groups
                    label = os.path.splitext(os.path.basename(file_path))[0]
                    color_result = colorchooser.askcolor(
                        title=f"Choose colour for: {label}",
                        color="#1f77b4"
                    )
                    color = color_result[1] if color_result and color_result[1] else f"C{len(groups)}"
                    groups.append({'file_path': file_path, 'label': label, 'color': color})

                if groups:
                    output_path = os.path.join(
                        self.analysis_output_folder.get(),
                        "entire_session_plot.png"
                    )
                    success = entire_session_plot.plot_entire_session(
                        groups=groups,
                        output_path=output_path,
                        fig_size=(float(self.figure_width.get()), float(self.figure_height.get()))
                    )
                    if success:
                        results_msg.append(f"Entire Session Plot: Saved to {output_path}")
                    else:
                        results_msg.append("Entire Session Plot: Failed during plotting.")
                else:
                    results_msg.append("Entire Session Plot: No files selected.")
            except Exception as e:
                print(f"DEBUG: Entire Session Plot Error: {e}")
                results_msg.append(f"Entire Session Plot Error: {e}")

        # Latency to First Scratch
        if "Latency to First Scratch" in selected_analyses:
            try:
                import latency_first_scratch
                import os
                file_path = filedialog.askopenfilename(
                    title="Select Excel File for Latency to First Scratch",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialdir=self.analysis_input_folder.get()
                )
                if file_path:
                    output_path = os.path.join(
                        self.analysis_output_folder.get(),
                        f"latency_{os.path.basename(file_path).replace('.xlsx', '.png')}"
                    )
                    success = latency_first_scratch.plot_latency_to_first_scratch(
                        file_path=file_path,
                        output_path=output_path,
                        fig_size=(float(self.figure_width.get()), float(self.figure_height.get()))
                    )
                    if success:
                        results_msg.append(f"Latency to First Scratch: Saved to {output_path}")
                    else:
                        results_msg.append("Latency to First Scratch: Failed during plotting.")
                else:
                    results_msg.append("Latency to First Scratch: Cancelled by user.")
            except Exception as e:
                print(f"DEBUG: Latency Error: {e}")
                results_msg.append(f"Latency to First Scratch Error: {e}")

        # Average Scratches per Mouse
        if "Average Scratches per Mouse" in selected_analyses:
            try:
                import average_scratches
                import os
                file_path = filedialog.askopenfilename(
                    title="Select Excel File for Average Scratches per Mouse",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialdir=self.analysis_input_folder.get()
                )
                if file_path:
                    output_path = os.path.join(
                        self.analysis_output_folder.get(),
                        f"avg_scratches_{os.path.basename(file_path).replace('.xlsx', '.png')}"
                    )
                    success = average_scratches.plot_average_scratches(
                        file_path=file_path,
                        output_path=output_path,
                        fig_size=(float(self.figure_width.get()), float(self.figure_height.get()))
                    )
                    if success:
                        results_msg.append(f"Average Scratches: Saved to {output_path}")
                    else:
                        results_msg.append("Average Scratches: Failed during plotting.")
                else:
                    results_msg.append("Average Scratches: Cancelled by user.")
            except Exception as e:
                print(f"DEBUG: Average Scratches Error: {e}")
                results_msg.append(f"Average Scratches Error: {e}")

        # Heatmap (ΔF/F per Mouse)
        if "Heatmap (ΔF/F per Mouse)" in selected_analyses:
            try:
                import heatmap_analysis
                file_path = filedialog.askopenfilename(
                    title="Select Excel File for Heatmap Analysis",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                    initialdir=self.analysis_input_folder.get()
                )
                if file_path:
                    saved = heatmap_analysis.plot_heatmaps(
                        file_path=file_path,
                        output_dir=self.analysis_output_folder.get(),
                        fig_size=(float(self.figure_width.get()), float(self.figure_height.get()))
                    )
                    if saved:
                        results_msg.append(f"Heatmap: Saved {saved} palette variants to {self.analysis_output_folder.get()}")
                    else:
                        results_msg.append("Heatmap: Failed during plotting.")
                else:
                    results_msg.append("Heatmap: Cancelled by user.")
            except Exception as e:
                print(f"DEBUG: Heatmap Error: {e}")
                results_msg.append(f"Heatmap Error: {e}")

        unimplemented = [a for a in selected_analyses if a not in [
            "Itch Bout Frequency",
            "Slope of scratching session (rate of increase or decrease)",
            "Peak Scratching Duration",
            "Area Under the Curve (AUC)",
            "Entire Session Plot",
            "Latency to First Scratch",
            "Average Scratches per Mouse",
            "Heatmap (ΔF/F per Mouse)"
        ]]
        if unimplemented:
            results_msg.append(f"Other selections ({len(unimplemented)} items) remain frontend placeholders.")
        
        messagebox.showinfo("Analysis Complete", "\n".join(results_msg))
    
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
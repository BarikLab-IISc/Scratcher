# Scratcher 1.4 User Guide

Welcome to **Scratcher 1.4**! This graphical application (GUI) is designed to process videos of mice to detect scratching behavior, extract behavioral data, and generate analysis plots and summaries.

---

## 1. Prerequisites & Installation

Before running the application, you need to download the repository and ensure your Python environment has the necessary libraries installed. If you are using Windows, you can run these commands in your Command Prompt, PowerShell, or Windows Subsystem for Linux (WSL).

### Download the Repository
Open your terminal and clone the repository using Git:
```bash
git clone https://github.com/BarikLab-IISc/Scratcher.git
cd Scratcher/Analyser
```

### Create a Virtual Environment and Install Dependencies
It is highly recommended to use a Python virtual environment to avoid conflicts with other projects.

Run the following commands to create a virtual environment, activate it, and install the required Python libraries.

**For Linux / MacOS (or WSL):**
```bash
# Install Tkinter for the GUI (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3-tk python3-venv

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required Python packages from the requirements file
pip install -r requirements.txt
```

**For Windows (Command Prompt / PowerShell):**
```powershell
# Create and activate the virtual environment
python -m venv venv
venv\Scripts\activate

# Install the required Python packages from the requirements file
pip install -r requirements.txt
```

You will also need:
- Valid video files (`.mp4` or `.avi`) of the mice.
- A trained YOLO model (`.pt` file), for example, `best.pt`.

---

## 2. Launching the Application

If you just cloned the repository and are in the `Scratcher/Analyser` folder, you can run the Python script directly:

```bash
python3 scratcher_1.4.py
```
*(Note for Windows users not using WSL: You can use `python` instead of `python3`)*

A window titled **"Scratcher 1.3 ©"** (which houses the 1.4 features) will open, presenting you with three main tabs: **DETECT**, **ANALYSE**, and **TRAIN**.

---

## 3. Step-by-Step Workflow

The standard pipeline consists of two steps: detecting behavior from videos (DETECT tab), and then analyzing that behavior (ANALYSE tab).

### Step 1: Extract Data from Videos (DETECT Tab)
This step uses Artificial Intelligence (YOLO) to scan your video files and convert the mouse's behavior into second-by-second Excel spreadsheets (`raster*.xlsx`).

1. **Input Folder:** Click "Browse" and select the folder containing your raw `.mp4` or `.avi` videos.
2. **Output Folder:** Click "Browse" and select an empty folder where you want the resulting Excel files to be saved.
3. **YOLO Model (.pt):** 
   - By default, the application looks for a model named `best.pt`. 
   - If your model has a different name or is located elsewhere, click "Browse" and locate your `.pt` model file.
4. **FPS:** Enter the Frames Per Second at which your videos were recorded (e.g., 30 or 60).
5. **Start Detection:** Click the blue button to begin.
   > **Note:** The application window may freeze or appear unresponsive while the AI processes the videos in the background. This is normal! Wait until a popup appears saying **"Detection Complete"**.

---

### Step 2: Generate Plots & Summaries (ANALYSE Tab)
Once you have generated the Excel files (or if you already have valid Excel files), use this tab to create visual charts and text summaries.

1. **Input Folder:** Click "Browse" and select the folder containing the generated Excel files (`raster*.xlsx`) from Step 1.
2. **Output Folder:** Click "Browse" and select where you want the final `.png` plots and `.txt` summaries to be saved.
3. **Select Videos:** 
   - Click the **"Select Videos from Folder"** button. This is required to process the data.
   - You can assign specific text "Aliases" to each video (e.g., "Control Mouse 1", "Treated Mouse 2").
   - Click "Confirm Selection" when done.
4. **Analysis Options:** Check the boxes for the analyses you wish to run. Newly integrated options include:
   - **`Itch Bout Frequency`**: Analyzes the `raster*.xlsx` files and creates a `.txt` file summarizing the frequency and length of scratching bouts.
   - **`Slope of scratching session`**: Looks for a non-raster Excel file containing time-series data to plot the regression slope of scratching duration across multiple mice.
   *(Note: Some of the other options currently act as static image previews and are placeholders for future updates).*
5. **Start Analysis:** Click the blue button. The application will process your spreadsheets and save the graphs directly to your chosen Output Folder!

---

### Step 3: Train New AI Models (TRAIN Tab)
If you need to improve your AI's accuracy by training it on new data:

1. **Working Directory:** The folder where training logs and resources will be stored.
2. **SCRATCHER Model Path:** Select an existing model to start training from (transfer learning).
3. **Data Configuration Path:** Select the `.yaml` file that defines where your training images and labels are located.
4. **Number of Epochs:** Enter how many training cycles the AI should undergo (e.g., 100).
5. **Start Training:** Click the button to begin the training process. (This can take many hours depending on your hardware).

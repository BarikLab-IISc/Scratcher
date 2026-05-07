

# Scratcher

<div align="center">

<!-- <img src="https://github.com/user-attachments/assets/99690b33-8da1-4016-9221-bf1c010b310b"
     alt="Scratcher Logo"
     width="200"
     height="200" /> -->
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/971e6c30-2005-4974-b1bc-5968fb1de373" />



# Scratcher  
**Automated Analysis of Rodent Scratching Behavior**

![Version](https://img.shields.io/badge/version-1.4-brightgreen)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLO](https://img.shields.io/badge/YOLO-v9-red.svg)](https://github.com/ultralytics/ultralytics)
[![Neuroscience](https://img.shields.io/badge/Neuroscience-10.1016%2Fj.neuroscience.2026.03.046-green.svg)](https://doi.org/10.1016/j.neuroscience.2026.03.046)

</div>

## Overview

**Scratcher** is an end-to-end deep learning-driven analysis suite for automated identification, quantification, and high-throughput analysis of nape-directed scratching behavior in rodent models of acute and chronic itch. This tool transforms behavioral classification problems into object detection tasks using state-of-the-art computer vision techniques to decipher the neural basis of various scratching behaviors.

### What's New in Scratcher

**v1.4 (Current Release)**

Scratcher 1.4 is a major upgrade to the analysis and GUI infrastructure. Key additions:

**Video Table GUI**
- Videos and their matching raster files are auto-detected from the input folder — no more manual file dialogs
- Each video can be configured with a custom **alias**, **colour**, and **start/end time** directly in the table
- Smart bidirectional raster file matching with automatic priority for `raster_plot_input_` prefixed files

**8 Integrated Analysis Plots**

| Plot | Description |
|------|-------------|
| Itch Bout Frequency | Counts itch bout occurrences per video |
| Slope of Scratching Session | Linear regression with R-squared per mouse, including an inset panel showing regression lines |
| Peak Scratching Duration | Scatter plot of the time and duration of each mouse's longest consecutive itch bout |
| Area Under the Curve (AUC) | Bar chart of total itch seconds per mouse, computed via Simpson's rule |
| Entire Session Plot | Spline-smoothed (cubic interpolation) line chart with SEM shading, binned per minute |
| Latency to First Scratch | Bar chart showing the first second each mouse scratched |
| Average Scratches per Mouse | Bar chart of itch rate as a percentage of the session |
| Heatmap | Per-video heatmaps using each video's assigned colour, plus a combined multi-colour heatmap |

**Raster Pipeline**
- Shared `raster_utils.py` backend reads the standardised `seconds | behaviour` raster format
- Automatic deduplication of overlapping timestamps
- Graceful handling of videos with zero detections — the pipeline skips empty files instead of crashing

**Detection Improvements**
- Support for `.mp4` and `.avi` video formats
- Configurable custom model path in the GUI
- Bundled model (`best.pt`) is a YOLOv9c architecture trained for 57 epochs on 640x640 frames, detecting 3 classes: **Itch**, **Locomotion**, and **Others**

**Platform Compatibility**
- Automatic Retina display scaling fix on macOS to reduce GUI rendering lag
- Error messages from plotting failures are now surfaced in the GUI messagebox instead of failing silently

**v1.3 (Previous Release)**
- Scratcher 1.3 (GUI version) added `.avi` file format support
- A comprehensive, step-wise tutorial was added to help new users get started with Scratcher and Roboflow


### Key Features

- **Automated Behavior Detection**: YOLO-based object detection for scratching behavior identification
- **Comprehensive Analysis**: Multiple visualization and statistical analysis tools
- **User-Friendly Interface**: Both GUI and command-line interfaces
- **High-Throughput Processing**: Batch processing of multiple video files
- **Advanced Visualizations**: Heatmaps, line charts, AUC analysis, and more
- **Custom Model Training**: Built-in tools for training custom YOLO models

## Installation

### Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (recommended for faster processing)
- 8GB+ RAM (16GB+ recommended for large datasets)

---

### Installing in a Virtual Environment (Recommended)

To avoid dependency conflicts, it is strongly recommended to install Scratcher inside a Python virtual environment.

```bash
# Clone the repository
git clone https://github.com/BarikLab-IISc/Scratcher.git
cd Scratcher/Analyser

# Create a virtual environment
python3 -m venv scratcher-venv

# Activate the virtual environment
source scratcher-venv/bin/activate
# On Windows: scratcher-venv\Scripts\activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Verify installation
python -c "import ultralytics; print('Installation successful!')"
````

---

### Quick Install (Without Virtual Environment)

> ⚠️ We don't recommended this, but this section is provided for convenience.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/BarikLab-IISc/Scratcher.git
   cd Scratcher
   ```

2. **Install dependencies**:

   ```bash
   cd Analyser
   pip install -r requirements.txt
   ```

3. **Verify installation**:

   ```bash
   python -c "import ultralytics; print('Installation successful!')"
   ```

---

### Dependencies

* `ultralytics>=8.0.20` — YOLO model framework
* `opencv-python>=4.8.1.78` — Computer vision operations
* `pandas>=1.5.3` — Data manipulation and analysis
* `openpyxl>=3.1.2` — Excel file handling
* `matplotlib` — Plotting engine
* `seaborn` — Statistical visualization styling
* `scipy` — Spline smoothing and numerical integration (AUC, entire session plot)
* `tkinter` — GUI framework (included with Python)

## Quick Start

### GUI Interface (Recommended for beginners)

Launch the graphical user interface:

```bash
cd Analyser
python scratcher_1.4.py
```

The GUI provides three main tabs:

* **DETECT**: Process videos with the bundled YOLOv9c model (or a custom model). Supports `.mp4` and `.avi` formats.
* **ANALYSE**: Select videos from the auto-populated table, configure per-video settings (alias, colour, time range), choose from 8 analysis types, and generate publication-quality plots.
* **TRAIN**: Train custom YOLO models on your own annotated datasets.

### Command Line Interface

For batch processing and automation:

```bash
cd Analyser
python main.py -m <model_path> -i <input_folder> -o <output_folder> [-c <conf_threshold>]
```

#### Command Line Arguments

| Argument                 | Description                                                       |
| ------------------------ | ----------------------------------------------------------------- |
| `-m`, `--model`          | **Required**. Path to the YOLO model weights file                 |
| `-i`, `--input_folder`   | **Required**. Path to the folder containing video files           |
| `-o`, `--output_folder`  | **Required**. Path to the folder where output files will be saved |
| `-c`, `--conf_threshold` | *Optional*. Confidence threshold for detections (default: `0.6`)  |

### Example Usage

```bash
# Process videos with custom confidence threshold
python main.py -m models/scratcher_v1.3.pt -i data/videos/ -o results/ -c 0.7

# Process with default settings
python main.py -m models/scratcher_v1.3.pt -i data/videos/ -o results/
```

## Analysis Features

### Behavioral Detection
- **Frame-by-frame Processing**: Each video frame is classified by the YOLO model into Itch, Locomotion, or Others
- **Majority-vote Filtering**: Raw frame-level predictions are aggregated into 1-second bins using a majority-vote scheme (`behaviour_filtering.py`), producing a raster file with columns `seconds | behaviour`
- **Confidence Filtering**: Adjustable detection thresholds (default: 0.6)
- **Batch Processing**: All videos in the input folder are processed sequentially

### Statistical Analysis
- **Temporal Binning**: 1-minute and 3-minute behavioral batching with per-bin itch statistics
- **Behavioral Categorization**: Automatic classification with priority rules (e.g., Itch overrides Others when both are detected)
- **Quantitative Metrics**: Duration, frequency, AUC, latency, and slope measurements

### Visualization Tools (v1.4)

All plots respect the per-video colour, alias, and figure size settings from the GUI.

| Plot | Script | Method |
|------|--------|--------|
| Itch Bout Frequency | `bout_frequency_analysis.py` | Per-file bout counting |
| Slope of Scratching Session | `slope_individual_mice.py` | `scipy.stats.linregress` with inset panel |
| Peak Scratching Duration | `peak_scratch_duration.py` | Longest consecutive itch bout detection |
| Area Under the Curve | `auc_analysis.py` | `scipy.integrate.simpson` on the binary itch series |
| Entire Session Plot | `entire_session_plot.py` | Cubic spline smoothing (`make_interp_spline`) with SEM shading |
| Latency to First Scratch | `latency_first_scratch.py` | First itch-positive second per mouse |
| Average Scratches per Mouse | `average_scratches.py` | Mean itch rate as a fraction of total session length |
| Heatmap | `heatmap_analysis.py` | Per-video colour heatmaps (white-to-colour gradient) plus a combined RGBA overlay |

## Model Training

### Training Custom Models

1. **Prepare your dataset**:
   - Organize videos in training/validation splits
   - Create YOLO-format annotation files
   - Configure `data.yaml` file

2. **Launch training**:
   ```bash
   cd Train
   python train.py --cwd <working_directory> --model_path <base_model> --data_path <data.yaml> --epochs <num_epochs>
   ```

3. **Monitor training**:
   - Training progress is displayed in real-time
   - Model checkpoints are saved automatically
   - Training time is logged to `Time_taken.txt`

### Training Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--cwd` | Working directory for training | Required |
| `--model_path` | Path to base YOLO model | Required |
| `--data_path` | Path to data configuration file | Required |
| `--epochs` | Number of training epochs | 57 |

## Output Files

### Detection Outputs
- **Excel Files**: Detailed behavioral annotations with timestamps
- **Raster Plot Data**: Formatted data for further analysis
- **Statistical Summaries**: Behavioral counts and durations

### Analysis Outputs
- **Visualization Images**: PNG files for all generated plots
- **Statistical Reports**: Excel files with quantitative analysis
- **Time Series Data**: Processed behavioral time series

## Project Structure

```
Scratcher/
├── Analyser/                 # Main analysis package
│   ├── features/            # Visualization modules
│   ├── images/              # Sample output images
│   ├── gui.py              # Main GUI interface
│   ├── main.py             # CLI entry point
│   └── requirements.txt    # Python dependencies
├── Model/                   # Model training scripts
├── Train/                   # Training utilities
└── Data/                    # Sample data
```

## Advanced Usage

### Custom Analysis Pipeline

```python
from ultralytics import YOLO
from video_processing import process_video
from behaviour_filtering import filter_behaviours
import raster_utils

# 1. Detect behaviours in a video
model = YOLO('best.pt')
process_video(model, 'input_video.mp4', 'output/', 'video_name', conf_threshold=0.6)

# 2. Filter frame-level detections into second-wise raster
filter_behaviours('output/video_name_behaviour_frames.xlsx',
                  'output/raster_plot_input_video_name_behaviour_frames.xlsx')

# 3. Load raster data for custom analysis
binary = raster_utils.raster_to_binary('output/raster_plot_input_video_name_behaviour_frames.xlsx')
print(f'Total itch seconds: {binary.sum()}')

# 4. Multi-mouse comparison
wide = raster_utils.build_wide_df(
    ['raster_mouse1.xlsx', 'raster_mouse2.xlsx'],
    ['Control', 'Experimental']
)
```

### Integration with Other Tools

Scratcher outputs are compatible with:
- **MATLAB**: Import Excel data for further analysis
- **R**: Statistical analysis of behavioral data
- **Python**: Direct integration with pandas/NumPy workflows

## Troubleshooting

### Common Issues

1. **CUDA Out of Memory**:
   - Reduce batch size in model configuration
   - Use CPU-only mode: `model = YOLO('model.pt', device='cpu')`

2. **Video Format Issues**:
   - Ensure videos are in `.mp4` or `.avi` format
   - Check video codec compatibility

3. **Model Loading Errors**:
   - Verify model file path and format
   - Check YOLO version compatibility

### Performance Optimization

- Use GPU acceleration when available
- Process videos in smaller batches for large datasets
- Adjust confidence thresholds based on your data quality

## Contributing

We welcome contributions to Scratcher! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Commit your changes**: `git commit -am 'Add new feature'`
4. **Push to the branch**: `git push origin feature/new-feature`
5. **Submit a pull request**

### Development Setup

```bash
git clone https://github.com/BarikLab-IISc/Scratcher.git
cd Scratcher
pip install -r Analyser/requirements.txt
pip install -e .  # Install in development mode
```

## Citation

If you use Scratcher in your research, please cite:

```bibtex
@article{NANDI2026155,
  title = {Scratcher: An automated machine-vision tool for dissecting the neural basis of itch},
  journal = {Neuroscience},
  volume = {603},
  pages = {155-175},
  year = {2026},
  issn = {0306-4522},
  doi = {https://doi.org/10.1016/j.neuroscience.2026.03.046},
  url = {https://www.sciencedirect.com/science/article/pii/S0306452226002344},
  author = {Devangshu Nandi and Raghav Kaushik Ravi and Jagat Narayan Prajapati and Arnab Barik}
}
```

**Software Citation:**
```bibtex
@software{scratcher2026,
  title={Scratcher: Automated Analysis of Rodent Scratching Behavior},
  author={Nandi, Devangshu and Ravi, Raghav Kaushik and Prajapati, Jagat Narayan and Barik, Arnab},
  year={2026},
  url={https://github.com/BarikLab-IISc/Scratcher}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **BarikLab** - Centre for NeuroScience, Indian Institute of Science Bangalore
- **Ultralytics** - For the YOLO framework
- **OpenCV Community** - For computer vision tools

## Contact

- **Lab Website**: [BarikLab IISc](https://sites.google.com/view/molecules-cells-and-circuits/home)
- **Issues**: [GitHub Issues](https://github.com/BarikLab-IISc/Scratcher/issues)
- **Email**: [nandidevangshu@gmail.com]

## References

1. Nandi, D., Ravi, R.K., Prajapati, J.N. & Barik, A. (2026). Scratcher: An automated machine-vision tool for dissecting the neural basis of itch. *Neuroscience*, 603, 155-175. [DOI](https://doi.org/10.1016/j.neuroscience.2026.03.046)
2. YOLO: Real-Time Object Detection - [arXiv:1506.02640](https://arxiv.org/abs/1506.02640)
3. Ultralytics YOLO - [GitHub](https://github.com/ultralytics/ultralytics)
4. OpenCV Documentation - [opencv.org](https://opencv.org)

---

**Note**: This tool is designed for research purposes. Please ensure compliance with your institution's animal research guidelines and ethical standards.

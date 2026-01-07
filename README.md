<!-- <center> SCRATCHER </center>

## Problem Statement
An independent end-to-end analysis deep-learning driven suite for the automated identification, quantifcation and high-throughput analysis of nape-directed scratching behaviour in rodent models of acute and chronic itch to decipher the neural basis of various scratching behaviours.

## What are we trying to do ?
Our approach was to experiment with computer vision to figure out if a classification problem could be transformed to an object detection problem. 

## DATA:
data will be added soon

## Running the Analyser - CLI
    git clone "https://github.com/BarikLab-IISc/Scratcher"

    python parser.py -m <model_path> -i <input_folder> -o <output_folder> [-c <conf_threshold>]

| Argument               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `-m`, `--model`        | **Required**. Path to the YOLO model weights file.                          |
| `-i`, `--input_folder` | **Required**. Path to the folder containing video files.                    |
| `-o`, `--output_folder`| **Required**. Path to the folder where output files will be saved.          |
| `-c`, `--conf_threshold`| *Optional*. Confidence threshold for detections (default: `0.6`).          |

## Running the Analyser - GUI
    python gui.py

<img width="847" alt="image" src="https://github.com/user-attachments/assets/8c90c569-48f9-4119-8470-b8f50e791963" />



 -->

# Scratcher

<div align="center">

<!-- <img src="https://github.com/user-attachments/assets/99690b33-8da1-4016-9221-bf1c010b310b"
     alt="Scratcher Logo"
     width="200"
     height="200" /> -->
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/971e6c30-2005-4974-b1bc-5968fb1de373" />



# Scratcher  
**Automated Analysis of Rodent Scratching Behavior**

![Version](https://img.shields.io/badge/version-1.3-brightgreen)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLO](https://img.shields.io/badge/YOLO-v8%2B-red.svg)](https://github.com/ultralytics/ultralytics)
[![bioRxiv](https://img.shields.io/badge/bioRxiv-10.1101%2F2025.08.18.670778-green.svg)](https://www.biorxiv.org/content/10.1101/2025.08.18.670778v1)

</div>

## Overview

**Scratcher** is an end-to-end deep learning-driven analysis suite for automated identification, quantification, and high-throughput analysis of nape-directed scratching behavior in rodent models of acute and chronic itch. This tool transforms behavioral classification problems into object detection tasks using state-of-the-art computer vision techniques to decipher the neural basis of various scratching behaviors.

### 💥  What’s New in Scratcher v1.3

**📌 v1.3**
- 💡 Scratcher 1.3 now supports `.avi` file format
- 💡 A comprehensive, step-wise tutorial has been added to help new users get started with **Scratcher** and **Roboflow**

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

### Quick Install

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

### Dependencies

- `ultralytics>=8.0.20` - YOLO model framework
- `opencv-python>=4.8.1.78` - Computer vision operations
- `pandas>=1.5.3` - Data manipulation and analysis
- `openpyxl>=3.1.2` - Excel file handling
- `tkinter` - GUI framework (included with Python)

## Quick Start

### GUI Interface (Recommended for beginners)

Launch the graphical user interface:

```bash
cd Analyser
    python gui.py
```

The GUI provides three main tabs:
- **Detection**: Process videos with pre-trained models
- **Analysis**: Generate behavioral analysis and visualizations
- **Training**: Train custom YOLO models

### Command Line Interface

For batch processing and automation:

```bash
cd Analyser
python main.py -m <model_path> -i <input_folder> -o <output_folder> [-c <conf_threshold>]
```

#### Command Line Arguments

| Argument | Description |
|----------|-------------|
| `-m`, `--model` | **Required**. Path to the YOLO model weights file |
| `-i`, `--input_folder` | **Required**. Path to the folder containing video files |
| `-o`, `--output_folder` | **Required**. Path to the folder where output files will be saved |
| `-c`, `--conf_threshold` | *Optional*. Confidence threshold for detections (default: `0.6`) |

### Example Usage

```bash
# Process videos with custom confidence threshold
python main.py -m models/scratcher_v1.3.pt -i data/videos/ -o results/ -c 0.7

# Process with default settings
python main.py -m models/scratcher_v1.3.pt -i data/videos/ -o results/
```

## Analysis Features

### Behavioral Detection
- **Real-time Processing**: Frame-by-frame analysis of video data
- **Multi-class Detection**: Identifies different behavioral categories
- **Confidence Filtering**: Adjustable detection thresholds
- **Batch Processing**: Handle multiple videos simultaneously

### Statistical Analysis
- **Temporal Analysis**: 1-minute and 3-minute behavioral batching
- **Behavioral Categorization**: Automatic classification of detected behaviors
- **Quantitative Metrics**: Duration, frequency, and intensity measurements

### Visualization Tools
- **Heatmaps**: Scratching duration per minute visualization
- **Line Charts**: Full session behavioral traces
- **Area Under Curve (AUC)**: Scratching behavior over time
- **Peak Analysis**: Peak scratching duration identification
- **Slope Analysis**: Behavioral trend analysis
- **Fiber Photometry**: Integration with neural recording data
- **Latency Analysis**: Time-to-itch measurements

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
from behaviour_analysis import analyse_behaviours

# Load custom model
model = YOLO('path/to/your/model.pt')

# Process single video
process_video(model, 'input_video.mp4', 'output_folder/', 'video_name', 0.7)

# Analyze behaviors
analyse_behaviours('output_folder/')
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
   - Ensure videos are in MP4 format
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

If you use Scratcher in your research, please cite our preprint:

```bibtex
@article{scratcher2025,
  title={Scratcher: Automated Analysis of Rodent Scratching Behavior},
  author={[Author Names]},
  journal={bioRxiv},
  year={2025},
  doi={10.1101/2025.08.18.670778},
  url={https://www.biorxiv.org/content/10.1101/2025.08.18.670778v1}
}
```

**Software Citation:**
```bibtex
@software{scratcher2024,
  title={Scratcher: Automated Analysis of Rodent Scratching Behavior},
  author={BarikLab, IISc},
  year={2024},
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

1. **Scratcher: Automated Analysis of Rodent Scratching Behavior** - [bioRxiv:10.1101/2025.08.18.670778](https://www.biorxiv.org/content/10.1101/2025.08.18.670778v1)
2. YOLO: Real-Time Object Detection - [arXiv:1506.02640](https://arxiv.org/abs/1506.02640)
3. Ultralytics YOLO - [GitHub](https://github.com/ultralytics/ultralytics)
4. OpenCV Documentation - [opencv.org](https://opencv.org)

---

**Note**: This tool is designed for research purposes. Please ensure compliance with your institution's animal research guidelines and ethical standards.

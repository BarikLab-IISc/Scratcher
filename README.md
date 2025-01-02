# BarikLab

## Problem Statement
Nociefensive behavioural analysis of mice and calculating the duration of behaviours in a sample with a good accuracy.

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





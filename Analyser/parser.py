import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Process video files and analyze behaviours.")
    
    parser.add_argument(
        '-m', '--model', 
        type=str, 
        required=True, 
        help='Path to the YOLO model weights file.'
    )
    
    parser.add_argument(
        '-i', '--input_folder', 
        type=str, 
        required=True, 
        help='Path to the folder containing video files.'
    )
    
    parser.add_argument(
        '-o', '--output_folder', 
        type=str, 
        required=True, 
        help='Path to the folder where output files will be saved.'
    )
    
    parser.add_argument(
        '-c', '--conf_threshold', 
        type=float, 
        default=0.6, 
        help='Confidence threshold for detections (default: 0.6).'
    )
    
    return parser

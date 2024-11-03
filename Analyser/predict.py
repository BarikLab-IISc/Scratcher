import argparse
import time
from ultralytics import YOLO
import os

def main(args):
    begin = time.time()
    
    model = YOLO(args.model_path)
    
    if args.change_dir:
        os.chdir(args.change_dir)
    
    model.predict(args.input_path, save=args.save, conf=args.confidence)
    
    end = time.time()
    print(f"Prediction completed in {end - begin:.2f} seconds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run YOLO model on a video and save the output.")
    
    parser.add_argument("--model_path", type=str, required=True, help="Path to the YOLO model weights.")
    parser.add_argument("--input_path", type=str, required=True, help="Path to the input video file.")
    parser.add_argument("--change_dir", type=str, help="Directory to change to before running the prediction.")
    parser.add_argument("--save", type=bool, default=True, help="Save the prediction output.")
    parser.add_argument("--confidence", type=float, default=0.5, help="Confidence threshold for prediction.")
    
    args = parser.parse_args()
    main(args)

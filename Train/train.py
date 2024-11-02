import argparse
import time
from ultralytics import YOLO
import os
import warnings

def main(args):
    # Set the working directory
    if not os.path.exists(args.cwd):
        warnings.warn("The path entered does not seem to exist")
    else:
        os.chdir(args.cwd)
    
    # Initialize YOLO model
    model = YOLO(args.model_path)
    
    # Record start time
    begin = time.time()
    
    # Train the model
    results = model.train(data=args.data_path, epochs=args.epochs)
    
    # Record end time
    end = time.time()
    
    # Save time taken to a file
    with open("Time_taken.txt", "w") as f:
        f.write(f"Time taken for analysing video is : {end - begin} seconds")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="YOLO Model Training Script")
    parser.add_argument("--cwd", type=str, required=True, help="Desired working directory")
    parser.add_argument("--model_path", type=str, required=True, help="Path to YOLO model file")
    parser.add_argument("--data_path", type=str, required=True, help="Path to data configuration file")
    parser.add_argument("--epochs", type=int, default=57, help="Number of training epochs")

    # Parse arguments
    args = parser.parse_args()
    main(args)


# command : python train_parser.py --cwd "<desired working directory>" --model_path "<path to YOLO model file>" --data_path "<path to data.yaml file>" --epochs <number of epochs>

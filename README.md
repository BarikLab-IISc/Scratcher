# BarikLab

## What are we trying to do ?
Our approach was to experiment with computer vision to figure out if a classification problem could be transformed to an object detection problem. 
## DATA:
    Our data for training the model 

## MODEL:

## Model : 
    The Model folder has 4 files :
    - train.py -- Train your own model with this file by replacing the model's path with your model of choice.
    - predct.py --  Use this file for analysing a video with your own model (by replacing the path to your own weights, by default our models weights are given as the argument)
    - frame-wise_analysis.py -- Frame-wise analysis of the video to calculate the number of frames in each class along with the frame numbers.
                             -- Outputs 'n' .txt files for 'n' classes in the dataset along with another file for storing 'no detection' frames
    - statistical_analysis.py -- Analysing the confidence levels of the frames of each class and getting the stats out



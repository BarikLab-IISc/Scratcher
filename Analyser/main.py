import os
import re
from ultralytics import YOLO
from video_processing import process_video
from behaviour_filtering import filter_behaviours
from behaviour_analysis import analyse_behaviours
from cli_parser import create_parser

def change_cwd(path):
    os.chdir(path)

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    
    model = YOLO(args.model)
    
    change_cwd(args.input_folder)
    print(f"Current working directory: {os.getcwd()}")
    
    paths = [f for f in os.listdir(args.input_folder) if f.endswith('.mp4')]
    print(f"Found video files: {paths}")
    
    for i in paths:
        name = re.search(r'([^\\]+)\.mp4$', i).group(1)
        process_video(model, os.path.join(args.input_folder, i), args.output_folder, name, args.conf_threshold)
    
    excel_paths = [f for f in os.listdir(args.output_folder) if f.endswith('.xlsx')]
    for i in excel_paths:
        output_path = os.path.join(args.output_folder, "raster_plot_input_" + i)
        filter_behaviours(os.path.join(args.output_folder, i), output_path)

    analyse_behaviours(args.output_folder)

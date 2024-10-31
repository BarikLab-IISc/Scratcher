import os
import re
from ultralytics import YOLO
from video_processing import process_video
from behaviour_filtering import filter_behaviours
from behaviour_analysis import analyse_behaviours

def change_cwd(path):
    os.chdir(path)

if __name__ == "__main__":
    output_folder = r"D:\Raghav\Model_itch_others_loco\Paper 1.3\TO_ANALYSE\Hm4di\DCZ\Batch2"
    model = YOLO(r"D:\Raghav\Model_itch_others_loco\Paper 1.3\runs\detect\train\weights\best.pt")
    
    change_cwd(output_folder)
    print(os.getcwd())
    
    paths = [f for f in os.listdir(output_folder) if f.endswith('.mp4')]
    print(paths)
    
    for i in paths:
        name = re.search(r'([^\\]+)\.mp4$', i).group(1)
        process_video(model, i, output_folder, name, 0.5)
    
    # Filter behaviours
    excel_paths = [f for f in os.listdir(output_folder) if f.endswith('.xlsx')]
    for i in excel_paths:
        output_path = "raster_plot_input_" + i
        filter_behaviours(os.path.join(output_folder, i), output_path)

    # Analyze behaviours
    analyse_behaviours(output_folder)

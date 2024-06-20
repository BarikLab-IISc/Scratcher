import cv2
from collections import defaultdict
import os
import re
from ultralytics import YOLO
model = YOLO(r"D:\Raghav\Models\Model-12\train\weights\best.pt")

def get_total_frames(video_path) :
    cap = cv2.VideoCapture(video_path)
    prop = int(cv2.CAP_PROP_FRAME_COUNT) 
    count = int(cv2.VideoCapture.get(cap, prop))
    return count

def get_no_detection_frames(class_frames, video_path):
    s = set()
    for behaviour, frames in class_frames.items() :
        for frame, confidence in frames :
            s.add(frame)
    tot_frames = get_total_frames(video_path)
    no_detection_frames = []
    for i in range(1, tot_frames + 1) :
        if i not in s :
            no_detection_frames.append(i)
    
    return no_detection_frames

# def get_classname_from_frame(class_frames, frame):
#     for behaviour, frames in class_frames.items():
#         if frame in frames :
#             return behaviour
#     return None

def process_video(model, video_path, output_folder, video_name, conf_threshold=0.6):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return
    frame_idx = 1
    class_frames = defaultdict(list)
    frames_list = [''] * (get_total_frames(video_path) + 1)
    frame_sequence = []
    frame_set = set()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model.predict(frame, conf=conf_threshold)
        detections = results[0].boxes

        for det in detections:
            class_id = int(det.cls)
            class_name = model.names[class_id]
            frames_list[frame_idx] += class_name
            confidence = float(det.conf)
            class_frames[class_name].append((frame_idx, confidence))
        frame_idx += 1

        no_detection_frames = get_no_detection_frames(class_frames, video_path)
        for frame in no_detection_frames :
            class_frames['no_detection'].append((frame, 0))

        # filtering code
        j = 0
        i = 1
        # for i in range(1, len(frames_list) + 1):
        while i < len(frames_list) :
            if len(frames_list[i]) == 0 :
                i += 1
                continue
            else:
                # print(i, " ", j)
                frame_sequence.append(frames_list[i])
                if frame_sequence[j] in ['Grooming1', 'Licking1'] :
                    if i != 0 :
                        if frame_sequence[j - 1] in ['Locomotion1', 'Rearing1']:
                            count = 0
                            start = i
                            while frame_sequence[j] in ['Grooming1', 'Licking1']:
                                # print(i, " a ", j)
                                end = i
                                i += 1
                                frame_sequence.append(frames_list[i])
                                j += 1
                                count += 1
                            if (frames_list[i] in ['Locomotion1', 'Rearing1']) & (count <= 15):
                                print("Captured ", start, end)
                                for frame in range(start, end + 1) :
                                    # print(frame)
                                    frame_set.add(frame)
                                
                            if i >= len(frames_list) :
                                break
                j += 1
                i += 1
        filtered_class_frames = defaultdict(list)
        for behaviour, frames in class_frames.items():
            for frame, confidence in frames:
                if frame in frame_set:
                    continue
                else:
                    filtered_class_frames[behaviour].append((frame, confidence))  
    cap.release()

    print("Capturing Done......")
    print("\n")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for class_name, frames in filtered_class_frames.items():
        count = 0
        with open(f"{output_folder}/{class_name}_frames_{video_name}.txt", "w") as f :
            for frame, confidence in frames :
                f.write(f"{frame}, {confidence}\n")
                count += 1
            f.write(f"Total no of frames : {count}\n")
            
    print("Processing complete.")

video_path = r"D:\Raghav\Analysis\analyse_videos\Day1_P400_Oxali_Blue.mp4"
video_name = re.search(r'([^\\]+)\.mp4$', video_path).group(1)
output_folder = r"D:\Raghav\output\model-12-output3"
process_video(model, video_path, output_folder, video_name)
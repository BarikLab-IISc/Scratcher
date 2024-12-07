import time
begin = time.time()
model = YOLO(r"D:\Raghav\Models\Model-12\train\weights\best.pt")
model.predict(r"D:\Raghav\Analysis\analyse_videos\Day1_P220_Oxali_Green.mp4", save = True, conf = 0.6)
end = time.time()
print("Time taken for prediction : ", (end - begin))

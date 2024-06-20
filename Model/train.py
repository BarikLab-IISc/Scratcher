import time
from ultralytics import YOLO
begin = time.time()
model = YOLO('yolov9c.pt')
results = model.train(data = r"D:\Raghav\Models\Model-13\data1\data.yaml", epochs = 45)
end = time.time()
print("The time taken for processing is : ", (end - begin))
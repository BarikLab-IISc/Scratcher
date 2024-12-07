import statistics as st
licking_conf = []
grooming_conf = []
locomotion_conf = []
unclear_conf = []
rearing_conf = []

def extract_frames(data, output, behaviour) :
    for i in range(0, len(data) - 1) :
        value = data[i].split(", ")[1]
        result = "{:.2f}".format(float(value))
        output.append(float(result))
    print(behaviour)
    print("Mean is :", st.mean(output))
    print("Median is :", st.median(output))
    print("Mode is :", st.mode(output))

with open(r"D:\Raghav\output\model-12-output3\Licking1_frames_Day1_P400_Oxali_Blue.txt", "r") as f:
    licking = f.readlines()
extract_frames(licking, licking_conf, "licking")

with open(r"D:\Raghav\output\model-12-output3\Grooming1_frames_Day1_P400_Oxali_Blue.txt", "r") as f:
    grooming = f.readlines()
extract_frames(grooming, grooming_conf, "grooming")

with open(r"D:\Raghav\output\model-12-output3\Locomotion1_frames_Day1_P400_Oxali_Blue.txt", "r") as f:
    locomotion = f.readlines()
extract_frames(locomotion, locomotion_conf, "locomotion")

with open(r"D:\Raghav\output\model-12-output3\Unclear1_frames_Day1_P400_Oxali_Blue.txt", "r") as f:
    unclear = f.readlines()
extract_frames(unclear, unclear_conf, "unclear")

with open(r"D:\Raghav\output\model-12-output3\Rearing1_frames_Day1_P400_Oxali_Blue.txt", "r") as f:
    rearing = f.readlines()
extract_frames(rearing, rearing_conf, "rearing")
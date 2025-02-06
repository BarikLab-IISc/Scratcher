import openpyxl
import pandas as pd

# def filter_behaviours(input_excel_path, output_excel_path):
#     wb = openpyxl.load_workbook(input_excel_path)
#     ws = wb.active
#     df = pd.DataFrame(ws.values)
    
#     if df.shape[1] < 2:
#         raise ValueError("The input Excel file must have at least two columns")
    
#     behaviours = df.iloc[:, 1]
#     output_df = pd.DataFrame(columns=["Seconds", "Behaviour"])
    
#     for i in range(0, len(behaviours), 30):
#         chunk = behaviours[i:i+30]
#         behaviour_counts = chunk.value_counts()
#         majority_behaviour = behaviour_counts.index[0]
        
#         if len(behaviour_counts.index) > 1 and majority_behaviour == "Others" and behaviour_counts.index[1] == 'Itch':
#             majority_behaviour = "Itch"
#         elif str(majority_behaviour) in ["Itch,Locomotion", "Locomotion,Itch", "Itch,Others", "Others,Itch"]:
#             majority_behaviour = "Itch"
#         elif str(majority_behaviour) in ["Locomotion,Others", "Others,Locomotion"]:
#             majority_behaviour = "Locomotion,Others"
#         elif "Locomotion" in str(majority_behaviour) and "Others" in str(majority_behaviour):
#             majority_behaviour = "Locomotion,Others"
#         elif "Locomotion" in str(majority_behaviour):
#             majority_behaviour = "Locomotion"
#         elif "Others" in str(majority_behaviour):
#             majority_behaviour = "Others"
#         elif "Itch" in str(majority_behaviour):
#             majority_behaviour = "Itch"

#         new_row = pd.DataFrame({"Seconds": [i//30 + 1], "Behaviour": [majority_behaviour]})
#         output_df = pd.concat([output_df, new_row], ignore_index=True)

#     with pd.ExcelWriter(output_excel_path, mode="w", engine="openpyxl") as writer:
#         output_df.to_excel(writer, sheet_name="Second-wise Behaviours", index=False)

#         behaviour_durations = output_df.groupby("Behaviour")["Seconds"].count().reset_index()
#         behaviour_durations.columns = ["Behaviour", "Total Duration (s)"]

#         all_behaviours = ["Locomotion", "Others", "Itch", "no_detection"]
#         for behaviour in all_behaviours:
#             if behaviour not in behaviour_durations["Behaviour"].values:
#                 new_row = pd.DataFrame({"Behaviour": [behaviour], "Total Duration (s)": [0]})
#                 behaviour_durations = pd.concat([behaviour_durations, new_row], ignore_index=True)

#         behaviour_durations["Behaviour"] = behaviour_durations["Behaviour"].astype(str)
#         behaviour_durations = behaviour_durations.sort_values("Behaviour")  
#         behaviour_durations.to_excel(writer, sheet_name="Behaviour Durations", index=False)


import openpyxl
import pandas as pd

def filter_behaviours(input_excel_path, output_excel_path):
    wb = openpyxl.load_workbook(input_excel_path)
    ws = wb.active
    df = pd.DataFrame(ws.values)
    
    if df.shape[1] < 2:
        raise ValueError("The input Excel file must have at least two columns")
    
    behaviours = df.iloc[:, 1]
    output_df = pd.DataFrame(columns=["Seconds", "Behaviour"])
    
    itch_counts = []
    
    for i in range(0, len(behaviours), 30):
        chunk = behaviours[i:i+30]
        behaviour_counts = chunk.value_counts()
        majority_behaviour = behaviour_counts.index[0]
        
        if len(behaviour_counts.index) > 1 and majority_behaviour == "Others" and behaviour_counts.index[1] == 'Itch':
            majority_behaviour = "Itch"
        elif str(majority_behaviour) in ["Itch,Locomotion", "Locomotion,Itch", "Itch,Others", "Others,Itch"]:
            majority_behaviour = "Itch"
        elif str(majority_behaviour) in ["Locomotion,Others", "Others,Locomotion"]:
            majority_behaviour = "Locomotion,Others"
        elif "Locomotion" in str(majority_behaviour) and "Others" in str(majority_behaviour):
            majority_behaviour = "Locomotion,Others"
        elif "Locomotion" in str(majority_behaviour):
            majority_behaviour = "Locomotion"
        elif "Others" in str(majority_behaviour):
            majority_behaviour = "Others"
        elif "Itch" in str(majority_behaviour):
            majority_behaviour = "Itch"
        
        if majority_behaviour == "Itch":
            itch_counts.append(1)
        else:
            itch_counts.append(0)
        
        new_row = pd.DataFrame({"Seconds": [i//30 + 1], "Behaviour": [majority_behaviour]})
        output_df = pd.concat([output_df, new_row], ignore_index=True)
    
    with pd.ExcelWriter(output_excel_path, mode="w", engine="openpyxl") as writer:
        output_df.to_excel(writer, sheet_name="Second-wise Behaviours", index=False)

        behaviour_durations = output_df.groupby("Behaviour")["Seconds"].count().reset_index()
        behaviour_durations.columns = ["Behaviour", "Total Duration (s)"]

        all_behaviours = ["Locomotion", "Others", "Itch", "no_detection"]
        for behaviour in all_behaviours:
            if behaviour not in behaviour_durations["Behaviour"].values:
                new_row = pd.DataFrame({"Behaviour": [behaviour], "Total Duration (s)": [0]})
                behaviour_durations = pd.concat([behaviour_durations, new_row], ignore_index=True)

        behaviour_durations["Behaviour"] = behaviour_durations["Behaviour"].astype(str)
        behaviour_durations = behaviour_durations.sort_values("Behaviour") 
        behaviour_durations.to_excel(writer, sheet_name="Behaviour Durations", index=False)
        
        itch_series = pd.Series(itch_counts)
        avg_itch_per_min = itch_series.rolling(window=1).sum().mean()  
        avg_itch_per_3min = itch_series.rolling(window=3).sum().mean()  
        
        itch_stats = pd.DataFrame({
            "Metric": ["Avg Itch per Min", "Avg Itch per 3 Min"],
            "Value": [avg_itch_per_min, avg_itch_per_3min]
        })
        itch_stats.to_excel(writer, sheet_name="Itch Statistics", index=False)


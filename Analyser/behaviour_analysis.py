# import os
# import pandas as pd
# import re

# def analyse_behaviours(output_folder):
#     raster_files = [f for f in os.listdir(output_folder) if f.startswith('raster') and f.endswith('.xlsx')]
    
#     for file_path in raster_files:
#         df = pd.read_excel(file_path)
#         df['serial'] = (df['Seconds'] // 180) 

#         behaviour_map = {'Itch': ['Itch'], 
#                          'Locomotion': ['Locomotion'], 
#                          'Others': ['Others'], 
#                          'Locomotion,Others': ['Locomotion,Others']}
#         df['Behaviour_Cat'] = df['Behaviour'].apply(lambda x: next((k for k, v in behaviour_map.items() if x in v), 'no_detection'))

#         grouped_df = df.groupby(['serial', 'Behaviour_Cat']).size().reset_index(name='count')

#         pivoted_df = grouped_df.pivot(index='serial', columns='Behaviour_Cat', values='count').fillna(0)
#         name = re.search(r'([^\\]+)\.xlsx$', file_path).group(1) 

#         output_file = f"3min-batched-{name}_output.xlsx"
#         pivoted_df.to_excel(f"{output_folder}/{output_file}", index=True)

#         with pd.ExcelWriter(file_path, mode='a') as writer:
#             pivoted_df.to_excel(writer, sheet_name='3-min-batching', index=True)


import os
import pandas as pd
import re

def analyse_behaviours(output_folder):
    raster_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.startswith('raster') and f.endswith('.xlsx')]
    
    for file_path in raster_files:
        df = pd.read_excel(file_path)
        
        df['serial_3min'] = (df['Seconds'] // 180)
        
        df['serial_1min'] = (df['Seconds'] // 60)
        
        behaviour_map = {
            'Itch': ['Itch'], 
            'Locomotion': ['Locomotion'], 
            'Others': ['Others'], 
            'Locomotion,Others': ['Locomotion,Others']
        }
        
        df['Behaviour_Cat'] = df['Behaviour'].apply(lambda x: next((k for k, v in behaviour_map.items() if x in v), 'no_detection'))
        
        grouped_3min_df = df.groupby(['serial_3min', 'Behaviour_Cat']).size().reset_index(name='count')
        pivoted_3min_df = grouped_3min_df.pivot(index='serial_3min', columns='Behaviour_Cat', values='count').fillna(0)
        
        grouped_1min_df = df.groupby(['serial_1min', 'Behaviour_Cat']).size().reset_index(name='count')
        pivoted_1min_df = grouped_1min_df.pivot(index='serial_1min', columns='Behaviour_Cat', values='count').fillna(0)
        
        name = os.path.splitext(os.path.basename(file_path))[0]
        
        output_3min_file = os.path.join(output_folder, f"3min-batched-{name}_output.xlsx")
        pivoted_3min_df.to_excel(output_3min_file, index=True)
        
        output_1min_file = os.path.join(output_folder, f"1min-batched-{name}_output.xlsx")
        pivoted_1min_df.to_excel(output_1min_file, index=True)
        
        with pd.ExcelWriter(file_path, mode='a') as writer:
            pivoted_3min_df.to_excel(writer, sheet_name='3-min-batching', index=True)
            pivoted_1min_df.to_excel(writer, sheet_name='1-min-batching', index=True)




import pandas as pd
from pathlib import Path
from collections import defaultdict
import os

def analyze_bout_frequency(input_folder, output_folder):
    """
    Analyzes raster excel files containing second-wise behaviors and outputs 
    itch bout frequencies to text files in the output directory.
    """
    folder = Path(input_folder)
    out_dir = Path(output_folder)
    
    # Process each raster Excel file
    files_processed = 0
    for xlsx_file in folder.glob("raster*.xlsx"):
        try:
            # Read the sheet
            df = pd.read_excel(xlsx_file, sheet_name="Second-wise Behaviours")
            
            # Extract behavior column (second column)
            behaviors = df.iloc[:, 1].astype(str)
            
            # Detect itch bouts with time ranges
            bout_data = []  # Will store (duration, start_second, end_second)
            current_bout = 0
            bout_start = None
            
            for idx, behavior in enumerate(behaviors):
                actual_second = df.iloc[idx, 0]  # Get the second from first column
                
                if "no_detection" in behavior.lower():
                    continue  # Skip, don't interrupt bout
                elif "itch" in behavior.lower():
                    if current_bout == 0:
                        bout_start = actual_second
                    current_bout += 1
                else:
                    if current_bout > 0:
                        bout_end = df.iloc[idx - 1, 0]
                        bout_data.append((current_bout, bout_start, bout_end))
                    current_bout = 0
                    bout_start = None
            
            # Don't forget last bout if file ends with itch
            if current_bout > 0:
                bout_end = df.iloc[len(behaviors) - 1, 0]
                bout_data.append((current_bout, bout_start, bout_end))
            
            # Group bouts by duration
            bout_groups = defaultdict(list)
            for duration, start, end in bout_data:
                bout_groups[duration].append((start, end))
            
            # Write results to txt file
            output_file = out_dir / f"{xlsx_file.stem}_bout_frequency.txt"
            with open(output_file, 'w') as f:
                f.write(f"Itch Bout Duration Analysis for: {xlsx_file.name}\n\n")
                for duration in sorted(bout_groups.keys()):
                    ranges = ", ".join([f"{s}-{e}" for s, e in bout_groups[duration]])
                    f.write(f"{duration}-second bouts: {len(bout_groups[duration])} ({ranges})\n")
            
            files_processed += 1
        except Exception as e:
            print(f"Error processing {xlsx_file.name}: {e}")
            
    return files_processed

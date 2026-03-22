import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


def plot_latency_to_first_scratch(file_path, output_path, fig_size=(10, 6)):
    """
    Reads an Excel file with time in the first column and per-mouse scratch
    duration in subsequent columns. For each mouse it finds the first time
    point at which scratching > 0 and plots that as a bar chart.

    Returns True on success, False on error.
    """
    try:
        data = pd.read_excel(file_path, header=0)
        time = data.iloc[:, 0]
        mouse_headers = data.columns[1:]

        latency_values = []
        labels = []

        for col in mouse_headers:
            mouse_data = pd.to_numeric(data[col], errors='coerce')
            nonzero_indices = mouse_data[mouse_data > 0].index
            if len(nonzero_indices) > 0:
                latency_time = time.iloc[nonzero_indices[0]]
            else:
                latency_time = None
            latency_values.append(latency_time)
            labels.append(col)

        # Filter out mice with no detected scratch
        filtered_labels    = [l for l, v in zip(labels, latency_values) if v is not None]
        filtered_latencies = [v for v in latency_values if v is not None]

        if not filtered_latencies:
            print("No non-zero scratch values found in any mouse column.")
            return False

        fig, ax = plt.subplots(figsize=fig_size)
        ax.bar(filtered_labels, filtered_latencies, color='teal')
        ax.set_ylabel("Latency to First Scratch (minutes)", fontsize=12)
        ax.set_xlabel("Mouse", fontsize=12)
        ax.set_title("Latency to First Scratch", fontsize=14)
        ax.set_ylim(0, max(filtered_latencies) * 1.1)
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_latency_to_first_scratch: {e}")
        return False

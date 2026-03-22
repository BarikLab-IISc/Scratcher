import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


def plot_average_scratches(file_path, output_path, fig_size=(10, 6)):
    """
    Reads an Excel file with time in the first column and per-mouse scratch
    duration in subsequent columns. Computes the mean scratch duration for
    each mouse across the entire session and plots it as a bar chart.

    Returns True on success, False on error.
    """
    try:
        data = pd.read_excel(file_path, header=0)
        mouse_headers = data.columns[1:]

        avg_values = []
        labels = []

        for col in mouse_headers:
            numeric_col = pd.to_numeric(data[col], errors='coerce')
            avg_values.append(numeric_col.mean())
            labels.append(col)

        if not avg_values:
            print("No mouse columns found.")
            return False

        fig, ax = plt.subplots(figsize=fig_size)
        ax.bar(labels, avg_values, color='steelblue')
        ax.set_xlabel("Mouse", fontsize=12)
        ax.set_ylabel("Average Scratch Duration (seconds)", fontsize=12)
        ax.set_title("Average Scratches per Mouse", fontsize=14)
        ax.set_ylim(0, max(avg_values) * 1.1)
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_average_scratches: {e}")
        return False

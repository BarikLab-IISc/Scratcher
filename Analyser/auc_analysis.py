import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for use inside GUI
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import os


def plot_auc(file_path, output_path, fig_size=(8, 6)):
    """
    Reads an Excel file with time in the first column and per-mouse scratch
    duration in subsequent columns. Computes the Area Under the Curve (AUC)
    for each mouse using Simpson's rule and saves a bar chart to output_path.

    Returns True on success, False on error.
    """
    try:
        data = pd.read_excel(file_path, header=0)
        time = data.iloc[:, 0]
        mouse_columns = data.columns[1:]

        auc_values = []
        mouse_names = []

        for col in mouse_columns:
            auc = simpson(data[col].values, x=time.values)
            auc_values.append(auc)
            mouse_names.append(col)

        fig, ax = plt.subplots(figsize=fig_size)
        ax.bar(mouse_names, auc_values, color='steelblue')
        ax.set_xlabel("Mouse Name", fontsize=12)
        ax.set_ylabel("AUC", fontsize=12)
        ax.set_title("Area Under the Curve (AUC) for Each Mouse", fontsize=14)
        ax.set_ylim(0, max(auc_values) * 1.1 if auc_values else 1)
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_auc: {e}")
        return False

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import raster_utils


def plot_auc(file_paths, labels, colors, output_path, fig_size=(8, 6)):
    """
    Compute Area Under the Curve for each mouse using the binary Itch series
    and plot as a bar chart.
    """
    try:
        auc_values = []

        for fp in file_paths:
            s = raster_utils.raster_to_binary(fp)
            t = s.index.astype(float).values
            y = s.values
            if len(y) < 2:
                auc_values.append(0.0)
            else:
                auc_values.append(simpson(y, x=t))

        fig, ax = plt.subplots(figsize=fig_size)
        ax.bar(labels, auc_values, color=colors)
        ax.set_xlabel("Mouse", fontsize=12)
        ax.set_ylabel("AUC (Itch seconds)", fontsize=12)
        ax.set_title("Area Under the Curve — Itch Duration", fontsize=14)
        if auc_values:
            ax.set_ylim(0, max(auc_values) * 1.1)
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True
    except Exception as e:
        print(f"Error in plot_auc: {e}")
        return False

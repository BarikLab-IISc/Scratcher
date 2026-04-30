import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import raster_utils


def plot_average_scratches(file_paths, labels, colors, output_path, fig_size=(10, 6)):
    """
    For each raster file, compute the fraction of seconds labelled as Itch
    (= average Itch rate across the session) and plot as a bar chart.
    """
    try:
        avg_values = []

        for fp in file_paths:
            s = raster_utils.raster_to_binary(fp)
            val = s.mean() * 100.0 if not s.empty else 0.0
            avg_values.append(val)  # as percentage

        fig, ax = plt.subplots(figsize=fig_size)
        ax.bar(labels, avg_values, color=colors)
        ax.set_xlabel("Mouse", fontsize=12)
        ax.set_ylabel("Average Itch Rate (% of session)", fontsize=12)
        ax.set_title("Average Scratch Rate per Mouse", fontsize=14)
        if avg_values:
            ax.set_ylim(0, max(avg_values) * 1.1)
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True
    except Exception as e:
        print(f"Error in plot_average_scratches: {e}")
        return False

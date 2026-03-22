import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for use inside GUI
import matplotlib.pyplot as plt
import os


def plot_peak_scratch_duration(file_path, output_path, fig_size=(8, 6)):
    """
    Reads an Excel file with time in the first column and per-mouse scratch
    duration in subsequent columns.  For each mouse it finds the single time
    point at which scratching was highest and plots that as a scatter point.

    The resulting figure is saved to output_path (PNG).
    Returns True on success, False on error.
    """
    try:
        data = pd.read_excel(file_path, header=0)
        time = data.iloc[:, 0]
        mouse_headers = data.columns[1:]

        x_coords = []   # time (minutes) at peak
        y_coords = []   # peak scratch duration (seconds)
        labels = []     # mouse identifiers

        for col in mouse_headers:
            idx_peak = data[col].apply(pd.to_numeric, errors='coerce').idxmax()
            x_coords.append(time.iloc[idx_peak])
            y_coords.append(pd.to_numeric(data[col], errors='coerce').iloc[idx_peak])
            labels.append(col)

        # Colormap — get_cmap takes only the name; use Normalize for discrete colours
        cmap = matplotlib.colormaps.get_cmap('viridis')
        n = max(len(x_coords) - 1, 1)
        colors = [cmap(i / n) for i in range(len(x_coords))]

        fig, ax = plt.subplots(figsize=fig_size)

        for i in range(len(x_coords)):
            ax.scatter(x_coords[i], y_coords[i],
                       s=100,
                       color=colors(i),
                       label=labels[i])

        ax.set_xlabel("Time since injection (minutes)", fontsize=12)
        ax.set_ylabel("Peak Scratch Duration (seconds)", fontsize=12)
        ax.set_title("Peak Scratching Duration", fontsize=14)
        ax.legend(title="Mouse")

        if y_coords:
            ax.set_ylim(0, max(y_coords) * 1.1)
        if x_coords:
            ax.set_xlim(0, max(x_coords) * 1.1)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_peak_scratch_duration: {e}")
        return False

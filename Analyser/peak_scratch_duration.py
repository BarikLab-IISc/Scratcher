import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import raster_utils


def plot_peak_scratch_duration(file_paths, labels, colors, output_path, fig_size=(8, 6)):
    """
    For each mouse (raster file), find the time of the longest consecutive
    Itch bout and plot it as a scatter (x=time of peak, y=bout length).
    """
    try:
        x_coords, y_coords = [], []

        for fp in file_paths:
            df = raster_utils.load_raster(fp)
            max_len, best_start = 0, None
            cur_len, cur_start = 0, None

            for _, row in df.iterrows():
                b = str(row["behaviour"]).lower()
                if "itch" in b:
                    if cur_len == 0:
                        cur_start = row["seconds"]
                    cur_len += 1
                    if cur_len > max_len:
                        max_len = cur_len
                        best_start = cur_start
                elif "no_detection" not in b:
                    cur_len, cur_start = 0, None

            x_coords.append(float(best_start) if best_start is not None else 0.0)
            y_coords.append(float(max_len))

        fig, ax = plt.subplots(figsize=fig_size)
        for i in range(len(x_coords)):
            ax.scatter(x_coords[i], y_coords[i], s=100,
                       color=colors[i], label=labels[i])

        ax.set_xlabel("Time of Peak Bout (seconds)", fontsize=12)
        ax.set_ylabel("Peak Bout Duration (seconds)", fontsize=12)
        ax.set_title("Peak Scratching Bout per Mouse", fontsize=14)
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

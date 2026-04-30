import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import raster_utils


def plot_peak_scratch_duration(file_paths, labels, colors, output_path, fig_size=(8, 6)):
    """
    For each mouse (raster file), find the time of the longest consecutive
    Itch bout and plot it as a scatter (x=time of peak, y=bout length).
    Mice with zero Itch detections are excluded from the plot.
    """
    try:
        x_coords, y_coords, plot_labels, plot_colors = [], [], [], []

        for fp, label, color in zip(file_paths, labels, colors):
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

            # Only include mice that had at least one Itch bout
            if best_start is not None and max_len > 0:
                x_coords.append(float(best_start))
                y_coords.append(float(max_len))
                plot_labels.append(label)
                plot_colors.append(color)

        if not x_coords:
            print("Peak Scratch Duration: No Itch bouts found in any file.")
            return False

        fig, ax = plt.subplots(figsize=fig_size)
        for i in range(len(x_coords)):
            ax.scatter(x_coords[i], y_coords[i], s=120,
                       color=plot_colors[i], label=plot_labels[i],
                       edgecolors='black', linewidths=0.8, alpha=0.85,
                       zorder=5 + i)

        ax.set_xlabel("Time of Peak Bout (seconds)", fontsize=12)
        ax.set_ylabel("Peak Bout Duration (seconds)", fontsize=12)
        ax.set_title("Peak Scratching Bout per Mouse", fontsize=14)
        ax.legend(title="Mouse")

        y_max = max(y_coords) if y_coords else 1
        x_max = max(x_coords) if x_coords else 1
        ax.set_ylim(0, y_max * 1.15 if y_max > 0 else 1)
        ax.set_xlim(0, x_max * 1.15 if x_max > 0 else 1)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True
    except Exception as e:
        print(f"Error in plot_peak_scratch_duration: {e}")
        return False

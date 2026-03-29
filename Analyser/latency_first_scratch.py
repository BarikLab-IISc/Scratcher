import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import raster_utils


def plot_latency_to_first_scratch(file_paths, labels, colors, output_path, fig_size=(10, 6)):
    """
    For each raster file, find the first second labelled as Itch and
    plot a bar chart of latency per mouse.
    """
    try:
        latencies = []

        for fp in file_paths:
            df = raster_utils.load_raster(fp)
            itch_rows = df[df["behaviour"].str.contains("Itch", case=False, na=False)]
            if not itch_rows.empty:
                latencies.append(float(itch_rows.iloc[0]["seconds"]))
            else:
                latencies.append(None)

        filtered_labels  = [l for l, v in zip(labels, latencies)  if v is not None]
        filtered_colors  = [c for c, v in zip(colors, latencies)  if v is not None]
        filtered_latencies = [v for v in latencies if v is not None]

        if not filtered_latencies:
            print("No Itch behaviour found in any raster file.")
            return False

        fig, ax = plt.subplots(figsize=fig_size)
        ax.bar(filtered_labels, filtered_latencies, color=filtered_colors)
        ax.set_ylabel("Latency to First Scratch (seconds)", fontsize=12)
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

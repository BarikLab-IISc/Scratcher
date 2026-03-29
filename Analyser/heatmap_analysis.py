import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import raster_utils
import os

DIVERGING_PALETTES = ['coolwarm', 'seismic', 'RdBu_r', 'BrBG', 'PiYG', 'Reds']


def plot_heatmaps(file_paths, labels, output_dir, fig_size=(12, 6)):
    """
    Build a heatmap where rows = mice, columns = seconds.
    Each cell is 1 if that second was Itch, 0 otherwise.
    Saves one PNG per diverging palette to output_dir.
    """
    try:
        wide = raster_utils.build_wide_df(file_paths, labels)
        data_t = wide.set_index("seconds").transpose()
        data_t.index = labels

        base = "heatmap_raster"
        saved = 0

        for palette in DIVERGING_PALETTES:
            fig, ax = plt.subplots(figsize=fig_size)
            sns.heatmap(data_t, cmap=palette, center=0, ax=ax,
                        cbar_kws={'label': 'Itch (1=yes, 0=no)'})
            ax.set_title(f"Itch Heatmap ({palette})", fontsize=14)
            ax.set_xlabel("Time (seconds)", fontsize=12)
            ax.set_ylabel("Mouse", fontsize=12)

            plt.tight_layout()
            out_path = os.path.join(output_dir, f"{base}_{palette}.png")
            plt.savefig(out_path, dpi=300, bbox_inches='tight')
            plt.close(fig)
            saved += 1

        return saved
    except Exception as e:
        print(f"Error in plot_heatmaps: {e}")
        return 0

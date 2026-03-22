import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


DIVERGING_PALETTES = ['coolwarm', 'seismic', 'RdBu_r', 'BrBG', 'PiYG', 'Reds']


def plot_heatmaps(file_path, output_dir, fig_size=(12, 6)):
    """
    Reads an Excel file where the first column is time (seconds) and the
    remaining columns are per-mouse ΔF/F values. Generates one heatmap PNG
    per diverging colour palette, saved to output_dir.

    Returns the number of heatmaps saved, or 0 on error.
    """
    try:
        df = pd.read_excel(file_path, header=0)
        time = df.iloc[:, 0]
        data = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)

        # Transpose: rows = mice, columns = time points
        data_t = data.transpose()
        data_t.columns = time

        base = os.path.splitext(os.path.basename(file_path))[0]
        saved = 0

        for palette in DIVERGING_PALETTES:
            fig, ax = plt.subplots(figsize=fig_size)
            sns.heatmap(
                data_t,
                cmap=palette,
                center=0,
                ax=ax,
                cbar_kws={'label': 'ΔF/F'}
            )
            ax.set_title(f'Heatmap of ΔF/F across Mice ({palette})', fontsize=14)
            ax.set_xlabel('Time (s)', fontsize=12)
            ax.set_ylabel('Mice', fontsize=12)

            plt.tight_layout()
            out_path = os.path.join(output_dir, f"heatmap_{base}_{palette}.png")
            plt.savefig(out_path, dpi=300, bbox_inches='tight')
            plt.close(fig)
            saved += 1

        return saved

    except Exception as e:
        print(f"Error in plot_heatmaps: {e}")
        return 0

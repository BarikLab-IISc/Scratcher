import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import raster_utils


def plot_entire_session(file_paths, labels, colors, output_path, fig_size=(10, 6)):
    """
    Plot each mouse's Itch activity as a smoothed line over the session,
    binned per minute with SEM shading — publication-quality style.

    Parameters
    ----------
    file_paths : list of str  — raster .xlsx paths (one per mouse)
    labels     : list of str  — display name per mouse
    colors     : list of str  — hex colour per mouse
    output_path: str          — PNG save path
    fig_size   : tuple

    Returns True on success, False on error.
    """
    try:
        sns.set_style("ticks")
        sns.set_context("talk")

        fig, ax = plt.subplots(figsize=fig_size)
        markers = ['o', 's', 'D', '^', 'v', 'P', '*', 'X']

        for idx, (fp, label, color) in enumerate(zip(file_paths, labels, colors)):
            s = raster_utils.raster_to_binary(fp)
            if s.empty:
                continue
            seconds = s.index.astype(float)
            values = s.values

            # Bin into 1-minute windows: sum itch-seconds per minute
            minute_bins = (seconds / 60).astype(int)
            df_bin = pd.DataFrame({'minute': minute_bins, 'itch': values})
            per_minute = df_bin.groupby('minute')['itch'].sum()
            time_min = per_minute.index.values.astype(float)
            counts = per_minute.values.astype(float)

            if len(counts) == 0:
                continue

            # Smooth with a rolling window (3-minute window)
            win = min(3, max(1, len(counts) // 3))
            smoothed = np.convolve(counts, np.ones(win) / win, mode='same')

            # Rolling SEM for shading
            rolling_std = np.array([
                counts[max(0, i - win):i + win + 1].std()
                for i in range(len(counts))
            ])
            sem = rolling_std  # use std as error band

            # Plot the line
            marker = markers[idx % len(markers)]
            ax.plot(time_min, smoothed,
                    color=color, lw=2.5, zorder=3,
                    marker=marker, markersize=8,
                    markevery=max(len(time_min) // 10, 1),
                    markerfacecolor=color, markeredgecolor=color,
                    label=label)

            # SEM shading — prominent like the reference
            ax.fill_between(time_min,
                            smoothed - sem,
                            smoothed + sem,
                            color=color, alpha=0.25, zorder=2)

        # Clean, publication-quality axis styling
        ax.set_xlabel("Time (minutes)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Scratch Duration (s/min)", fontsize=14, fontweight='bold')
        ax.set_title("Scratching Behaviour Over Entire Session", fontsize=15,
                      fontweight='bold')

        # Clean up spines (keep left + bottom only)
        sns.despine(ax=ax, top=True, right=True)
        ax.tick_params(axis='both', which='major', labelsize=12)

        # Legend — top-right, clean
        ax.legend(frameon=True, fancybox=True, shadow=False,
                  fontsize=11, loc='upper right',
                  edgecolor='#cccccc', facecolor='white', framealpha=0.9)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight',
                    facecolor='white')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_entire_session: {e}")
        return False

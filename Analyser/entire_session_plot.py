import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline
import raster_utils


def _loess_smooth(x, y, smooth_factor=300):
    """Cubic spline approximation for LOESS-like smoothing."""
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)
    if len(x_arr) < 4:          # need at least k+1 = 4 points for k=3
        return x_arr, y_arr
    x_new = np.linspace(x_arr.min(), x_arr.max(), smooth_factor)
    spline = make_interp_spline(x_arr, y_arr, k=3)
    y_smooth = spline(x_new)
    return x_new, y_smooth


def plot_entire_session(file_paths, labels, colors, output_path, fig_size=(10, 6)):
    """
    Plot each mouse's Itch activity as a spline-smoothed line over the session
    with SEM shading — publication-quality style.

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

            time_sec = per_minute.index.values.astype(float) * 60  # in seconds
            counts = per_minute.values.astype(float)

            if len(counts) == 0:
                continue

            # Rolling SEM for shading (window = 3 bins)
            win = min(3, max(1, len(counts) // 3))
            rolling_std = np.array([
                counts[max(0, i - win):i + win + 1].std()
                for i in range(len(counts))
            ])

            # LOESS-like spline smoothing for the line
            x_smooth, y_smooth = _loess_smooth(time_sec, counts)

            # Plot the smoothed line
            marker = markers[idx % len(markers)]
            ax.plot(x_smooth, y_smooth,
                    label=label, color=color, lw=2,
                    marker=marker, markevery=30)

            # SEM shading on the original (non-smoothed) x-axis
            ax.fill_between(time_sec,
                            counts - rolling_std,
                            counts + rolling_std,
                            color=color, alpha=0.2)

        # Axis styling
        ax.set_xlabel("Time (seconds)", fontweight='bold')
        ax.set_ylabel("Scratching Duration (seconds)", fontweight='bold')

        # Clean up spines (keep left + bottom only)
        sns.despine(ax=ax, top=True, right=True)

        # Legend
        ax.legend(frameon=True, fancybox=True, shadow=True)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight',
                    facecolor='white')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_entire_session: {e}")
        return False

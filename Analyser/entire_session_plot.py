import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import raster_utils


def plot_entire_session(file_paths, labels, colors, output_path, fig_size=(10, 6)):
    """
    Plot each mouse's binary Itch series as an individual line over the session.

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
            time = s.index.astype(float)
            values = s.values

            # Rolling mean (window=60s) for a smoother line
            window = min(60, len(values) // 3) if len(values) > 3 else 1
            smoothed = np.convolve(values, np.ones(window) / window, mode='same')

            marker = markers[idx % len(markers)]
            ax.plot(time, smoothed,
                    label=label, color=color, lw=2,
                    marker=marker, markevery=max(len(time) // 10, 1))
            # SEM shading (using rolling std)
            if len(values) > window:
                rolling_std = np.array([
                    values[max(0, i - window):i + window].std()
                    for i in range(len(values))
                ])
                ax.fill_between(time,
                                smoothed - rolling_std,
                                smoothed + rolling_std,
                                color=color, alpha=0.15)

        ax.set_xlabel("Time (seconds)", fontsize=13)
        ax.set_ylabel("Itch Rate (smoothed)", fontsize=13)
        ax.set_title("Scratching Behaviour Over Entire Session", fontsize=15)
        ax.legend(frameon=True, fancybox=True, shadow=True)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_entire_session: {e}")
        return False

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline
import os


def _loess_smooth(x, y, smooth_factor=300):
    """Cubic spline approximation for smoothing."""
    x_new = np.linspace(x.min(), x.max(), smooth_factor)
    spline = make_interp_spline(x, y, k=3)
    y_smooth = spline(x_new)
    return x_new, y_smooth


def plot_entire_session(groups, output_path, fig_size=(10, 6)):
    """
    Plots the full scratching session for multiple groups with SEM shading.

    Parameters
    ----------
    groups : list of dict
        Each dict must have keys:
            'file_path' : str   – path to the Excel file
            'label'     : str   – legend label for this group
            'color'     : str   – matplotlib color string (e.g. '#ff0000' or 'blue')
        The Excel file is expected to have columns: [Time, Mean, SEM, ...]
    output_path : str
        Full path (including filename) where the PNG will be saved.
    fig_size : tuple
        (width, height) in inches.

    Returns True on success, False on error.
    """
    try:
        sns.set_style("ticks")
        sns.set_context("talk")

        fig, ax = plt.subplots(figsize=fig_size)

        markers = ['o', 's', 'D', '^', 'v', 'P', '*', 'X']

        for idx, grp in enumerate(groups):
            df = pd.read_excel(grp['file_path'], header=0)
            x   = df.iloc[:, 0]
            y   = df.iloc[:, 1]
            sem = df.iloc[:, 2]
            color   = grp.get('color', f'C{idx}')
            label   = grp.get('label', f'Group {idx + 1}')
            marker  = markers[idx % len(markers)]

            x_smooth, y_smooth = _loess_smooth(x, y)

            ax.plot(x_smooth, y_smooth,
                    label=label, color=color, lw=2,
                    marker=marker, markevery=30)
            ax.fill_between(x,
                            y - sem, y + sem,
                            color=color, alpha=0.2)

        ax.set_xlabel("Elapsed time (min) since injection", fontsize=13)
        ax.set_ylabel("Scratching Duration (seconds)", fontsize=13)
        ax.set_title("Scratching Behaviour Over Time", fontsize=15)
        ax.legend(frameon=True, fancybox=True, shadow=True)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return True

    except Exception as e:
        print(f"Error in plot_entire_session: {e}")
        return False

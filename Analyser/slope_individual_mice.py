import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import raster_utils


def plot_slope_individual_mice(file_paths, labels, colors, output_path,
                                bg_color="white", fig_size=(10, 8)):
    """
    Plot scratching session slope (regression lines + inset) for multiple mice.

    Parameters
    ----------
    file_paths : list of str  — one raster .xlsx per mouse
    labels     : list of str  — display name per mouse
    colors     : list of str  — hex colour per mouse
    output_path: str          — PNG save path
    bg_color   : str
    fig_size   : tuple
    """
    try:
        wide = raster_utils.build_wide_df(file_paths, labels)
        time = wide["seconds"]
        mouse_columns = wide.columns[1:]

        is_dark = bg_color.lower() == "black"
        text_color = "white" if is_dark else "black"
        grid_alpha = 0.3 if is_dark else 0.4

        fig, ax = plt.subplots(figsize=fig_size)
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)

        for col, color in zip(mouse_columns, colors):
            y = wide[col]
            reg = linregress(time, y)
            slope, intercept, r_value = reg.slope, reg.intercept, reg.rvalue
            regression_line = intercept + slope * time

            ax.scatter(time, y, color=color, s=35, edgecolor=text_color,
                       linewidth=0.3, alpha=0.9)
            ax.plot(time, regression_line, color=color, alpha=0.6, linewidth=2)
            ax.plot([], [], color=color, marker='o', linestyle='None',
                    label=f"{col}  (slope={slope:.3f}, R²={r_value**2:.2f})")

        ax.set_xlabel("Time (seconds)", fontsize=12, color=text_color)
        ax.set_ylabel("Itch Detected (binary)", fontsize=12, color=text_color)
        ax.set_title("Scratching Trend Over Session", fontsize=14, color=text_color)
        ax.tick_params(colors=text_color)
        ax.grid(True, linestyle='--', alpha=grid_alpha)
        ax.legend(title="Mouse", fontsize=9, title_fontsize=10, loc="upper left",
                  frameon=True, facecolor=bg_color, labelcolor=text_color)

        # Inset — regression lines only
        ax_inset = inset_axes(ax, width="40%", height="40%", loc="upper right", borderpad=2)
        ax_inset.set_facecolor(bg_color)
        for col, color in zip(mouse_columns, colors):
            y = wide[col]
            reg = linregress(time, y)
            regression_line = reg.intercept + reg.slope * time
            ax_inset.plot(time, regression_line, color=color, linewidth=2)
        ax_inset.set_title("Regression Lines", fontsize=10, color=text_color)
        ax_inset.grid(True, linestyle='--', alpha=grid_alpha)
        ax_inset.tick_params(colors=text_color)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight',
                    facecolor=bg_color)
        plt.close(fig)
        return True
    except Exception as e:
        print(f"Error plotting slope individual mice: {e}")
        return False

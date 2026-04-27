import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns
import raster_utils
import os


def _hex_to_cmap(hex_color, name="custom"):
    """Build a white→hex_color LinearSegmentedColormap."""
    rgb = mcolors.to_rgb(hex_color)
    cdict = {
        'red':   [(0, 1, 1), (1, rgb[0], rgb[0])],
        'green': [(0, 1, 1), (1, rgb[1], rgb[1])],
        'blue':  [(0, 1, 1), (1, rgb[2], rgb[2])],
    }
    return mcolors.LinearSegmentedColormap(name, cdict, N=256)


def plot_heatmaps(file_paths, labels, output_dir, fig_size=(12, 6),
                  colors=None):
    """
    Build itch heatmaps (rows = mice, columns = seconds).

    Produces:
      • One individual heatmap per video, coloured with that video's
        assigned colour (white → colour gradient).
      • One combined heatmap with all videos stacked, each row tinted
        in its own colour.

    Parameters
    ----------
    file_paths : list of str
    labels     : list of str
    output_dir : str
    fig_size   : tuple
    colors     : list of str  — hex colours, one per video (optional;
                 falls back to a default palette if not supplied)

    Returns the number of PNGs saved, or 0 on error.
    """
    try:
        wide = raster_utils.build_wide_df(file_paths, labels)
        data_t = wide.set_index("seconds").transpose()
        if data_t.empty:
            print("Heatmap: No data to plot.")
            return 0
        data_t.index = labels

        # Fallback palette when colours are not provided
        if colors is None or len(colors) < len(labels):
            default_palette = sns.color_palette("tab10", n_colors=len(labels))
            colors = [mcolors.to_hex(c) for c in default_palette]

        saved = 0

        # ── Individual heatmaps (one per video, in its own colour) ────────
        for idx, (label, color) in enumerate(zip(labels, colors)):
            row_data = data_t.iloc[[idx]]
            cmap = _hex_to_cmap(color, name=f"cmap_{idx}")

            fig, ax = plt.subplots(figsize=fig_size)
            sns.heatmap(row_data, cmap=cmap, vmin=0, vmax=1, ax=ax,
                        cbar_kws={'label': 'Itch (1=yes, 0=no)'})
            ax.set_title(f"Itch Heatmap — {label}", fontsize=14)
            ax.set_xlabel("Time (seconds)", fontsize=12)
            ax.set_ylabel("")

            plt.tight_layout()
            safe_label = label.replace(" ", "_").replace("/", "_")
            out_path = os.path.join(output_dir,
                                    f"heatmap_{safe_label}.png")
            plt.savefig(out_path, dpi=300, bbox_inches='tight')
            plt.close(fig)
            saved += 1

        # ── Combined heatmap (all videos, each row in its own colour) ─────
        if len(labels) > 1:
            fig, ax = plt.subplots(figsize=fig_size)
            data_arr = data_t.values.astype(float)
            n_mice, n_seconds = data_arr.shape

            # Build an RGBA image: each row tinted with its colour
            rgba = np.ones((n_mice, n_seconds, 4))   # start white
            for i, color in enumerate(colors):
                rgb = mcolors.to_rgb(color)
                for c in range(3):
                    # interpolate white(1) → colour channel
                    rgba[i, :, c] = 1.0 - data_arr[i] * (1.0 - rgb[c])
                rgba[i, :, 3] = 1.0   # fully opaque

            ax.imshow(rgba, aspect='auto', interpolation='nearest',
                      extent=[0, n_seconds, n_mice, 0])
            ax.set_yticks(np.arange(n_mice) + 0.5)
            ax.set_yticklabels(labels)
            ax.set_xlabel("Time (seconds)", fontsize=12)
            ax.set_ylabel("Mouse", fontsize=12)
            ax.set_title("Itch Heatmap — All Videos (per-video colours)",
                         fontsize=14)

            # Colour legend patches
            from matplotlib.patches import Patch
            patches = [Patch(facecolor=c, label=l)
                       for c, l in zip(colors, labels)]
            ax.legend(handles=patches, loc='upper right', fontsize=9,
                      title="Video", title_fontsize=10, framealpha=0.9)

            plt.tight_layout()
            out_path = os.path.join(output_dir, "heatmap_combined.png")
            plt.savefig(out_path, dpi=300, bbox_inches='tight')
            plt.close(fig)
            saved += 1

        return saved
    except Exception as e:
        print(f"Error in plot_heatmaps: {e}")
        return 0

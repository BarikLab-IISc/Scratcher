import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import os
import matplotlib
matplotlib.use('Agg') # Ensure it doesn't try to open a window during GUI analysis

def plot_slope_individual_mice(file_path, output_path, title="Scratching Duration Over Time", bg_color='white', fig_size=(10, 8)):
    """
    Reads an excel file with time in the first column and duration for multiple mice 
    in subsequent columns. Generates a scatterplot with regression lines and an inset,
    and saves it to the output_path.
    """
    try:
        # Read Excel file
        data = pd.read_excel(file_path, header=0)
        time = pd.to_numeric(data.iloc[:, 0], errors='coerce')
        mouse_columns = data.columns[1:]
        
        # Determine styling based on bg_color
        is_dark = bg_color.lower() == 'black'
        text_color = 'white' if is_dark else 'black'
        grid_alpha = 0.4
        
        # Set up figure styling
        plt.style.use('dark_background' if is_dark else 'default')
        
        # Define color palette
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        
        # Create main figure and axis
        fig, ax = plt.subplots(figsize=fig_size)
        
        if is_dark:
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')
        
        # Plot data and regression lines
        for col, color in zip(mouse_columns, colors * (len(mouse_columns) // len(colors) + 1)):
            y = pd.to_numeric(data[col], errors='coerce').fillna(0)
            reg_result = linregress(time, y)
            slope, intercept, r_value = reg_result.slope, reg_result.intercept, reg_result.rvalue
            regression_line = intercept + slope * time
        
            # Scatter individual bright points
            ax.scatter(time, y, color=color, s=35, edgecolor=text_color, linewidth=0.3, alpha=0.9)
        
            # Slightly dimmer regression line
            ax.plot(time, regression_line, color=color, alpha=0.6, linewidth=2)
        
            # Create legend entry with slope and R²
            label_text = f"{col}  (slope={slope:.3f}, R²={r_value**2:.2f})"
            ax.plot([], [], color=color, marker='o', linestyle='None', label=label_text)
        
        # Axis formatting
        ax.set_xlabel("Time (minutes)", fontsize=12, color=text_color)
        ax.set_ylabel("Scratch Duration", fontsize=12, color=text_color)
        ax.set_xlim(0, max(time) + 2 if len(time) > 0 else 45)
        ax.grid(True, linestyle='--', alpha=grid_alpha)
        ax.set_title(title, fontsize=14, color=text_color)
        ax.tick_params(colors=text_color)
        
        # --- Add inset showing regression lines only ---
        ax_inset = inset_axes(ax, width="40%", height="40%", loc="upper right", borderpad=2)
        if is_dark:
            ax_inset.set_facecolor('black')
            
        for col, color in zip(mouse_columns, colors * (len(mouse_columns) // len(colors) + 1)):
            y = pd.to_numeric(data[col], errors='coerce').fillna(0)
            reg_result = linregress(time, y)
            slope, intercept = reg_result.slope, reg_result.intercept
            regression_line = intercept + slope * time
            ax_inset.plot(time, regression_line, color=color, linewidth=2)
        
        ax_inset.set_title("Regression Lines (Zoomed)", fontsize=10, color=text_color)
        ax_inset.set_xlim(ax.get_xlim())
        ax_inset.grid(True, linestyle='--', alpha=grid_alpha)
        ax_inset.tick_params(colors=text_color)
        
        # Legend formatting
        ax.legend(title="Mouse Data", fontsize=9, title_fontsize=10, loc="upper left", frameon=True)
        
        # Save the figure
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        plt.close(fig)
        return True
        
    except Exception as e:
        print(f"Error plotting slope individual mice: {e}")
        return False

"""
raster_utils.py
Shared utilities for reading and converting Scratcher raster Excel files.

Raster file format
------------------
Sheet: "Second-wise Behaviours"  (falls back to first sheet)
Col 0: seconds (int)
Col 1: behaviour label (str) — one of:
        "Itch", "Locomotion", "Others", "no_detection"
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------------
# Low-level readers
# ---------------------------------------------------------------------------

def load_raster(file_path: str) -> pd.DataFrame:
    """
    Read a raster file and return a two-column DataFrame.
    Columns are renamed to ['seconds', 'behaviour'].
    """
    try:
        df = pd.read_excel(file_path, sheet_name="Second-wise Behaviours", header=0)
    except Exception:
        df = pd.read_excel(file_path, sheet_name=0, header=0)

    df = df.iloc[:, :2].copy()
    df.columns = ["seconds", "behaviour"]
    df["seconds"] = pd.to_numeric(df["seconds"], errors="coerce")
    df["behaviour"] = df["behaviour"].astype(str).str.strip()
    df = df.dropna(subset=["seconds"])
    return df.reset_index(drop=True)


def raster_to_binary(file_path: str, itch_label: str = "Itch") -> pd.Series:
    """
    Convert a raster file to a numeric Series indexed by seconds.
    Value is 1.0 if the behaviour contains itch_label (case-insensitive),
    0.0 otherwise.  no_detection rows are treated as 0.
    """
    df = load_raster(file_path)
    binary = df["behaviour"].str.contains(itch_label, case=False).astype(float)
    binary.index = df["seconds"].astype(int)
    return binary


# ---------------------------------------------------------------------------
# Multi-file helpers
# ---------------------------------------------------------------------------

def build_wide_df(file_paths: list, labels: list = None,
                  itch_label: str = "Itch") -> pd.DataFrame:
    """
    Given N raster files (one per mouse), build a wide DataFrame:
        col 0  : seconds  (union of all time axes, filled with 0 where missing)
        col 1..N: per-mouse binary Itch series

    Parameters
    ----------
    file_paths : list of str
    labels     : list of str, column names for each mouse (defaults to filename stem)
    itch_label : str, behaviour token to treat as 1.0

    Returns
    -------
    pd.DataFrame  with columns ['seconds', mouse1, mouse2, ...]
    """
    if labels is None:
        import os
        labels = [os.path.splitext(os.path.basename(fp))[0] for fp in file_paths]

    series_list = []
    for fp in file_paths:
        s = raster_to_binary(fp, itch_label)
        series_list.append(s)

    # Align on a common seconds index
    all_seconds = sorted(set().union(*[s.index for s in series_list]))
    wide = pd.DataFrame({"seconds": all_seconds})
    for label, s in zip(labels, series_list):
        wide[label] = wide["seconds"].map(s).fillna(0.0)

    return wide


def get_labels_and_colors(video_row_data: list) -> tuple:
    """
    Extract (labels, colors) from the GUI's video_row_data list,
    filtering only included rows.
    Returns (list of labels, list of hex color strings, list of file paths)
    """
    labels, colors, paths = [], [], []
    for row in video_row_data:
        if row["include"].get():
            # Raster file path is in the input folder
            raster = row.get("raster_path", "")
            if raster:
                labels.append(row["alias"].get() or row["video"])
                colors.append(row["color"].get())
                paths.append(raster)
    return labels, colors, paths

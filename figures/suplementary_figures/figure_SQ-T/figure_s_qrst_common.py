"""Shared plotting code for Supplementary Figures Q-T."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd


OUTPUT_ROOT = Path(__file__).parent
DATA_ROOT = Path("/Volumes/NeoData/Projects/temple/mda/MDA_PGH_2023")
SCENARIOS = ["", "_imp", "_itc", "_itc_imp"]
SCENARIO_LABELS = ["", "IMPORTATION", "ITC", "ITC\nIMPORTATION"]
SCENARIO_FILE_INDEX = {"_itc_imp": 0, "_itc": 1, "_imp": 2, "": 3}
METRICS = ("pfpr", "C580Y", "plas")
METRIC_TITLES = (
    r"$PfPR_{2-10}$",
    "ALLELE FREQUENCY OF 580Y",
    "GENOTYPE FREQUENCY OF\nPIPERAQUINE RESISTANTS",
)
RUN_QUANTILES = (0.01, 0.05, 0.50, 0.95, 0.99)
# Figure Q's published upper purple trajectory reaches 580Y fixation after
# about 2.5 years. The closest matching stored run in the Figure2 no-import,
# no-ITC 4-MDA set is column 435 (zero-based); the rank-based q99 run does not
# reproduce that trajectory. Keep this override explicit rather than silently
# presenting it as the exact q99 run.
UPPER_LINE_OVERRIDES = {("Figure2", 3): 435}
PURPLE = "#7969ad"
GRAY = "#c9c9c9"


def _read_runs(data_dir, run_set, metric):
    path = data_dir / f"{run_set}_{metric}.csv"
    values = pd.read_csv(path, header=None).to_numpy(dtype=float)
    if values.shape != (409, 1000):
        raise ValueError(f"Expected 409 x 1000 data at {path}, got {values.shape}")
    return np.nan_to_num(values, nan=0.0, posinf=0.0, neginf=0.0)


def _run_columns_by_rank(values_at_selection, quantiles):
    ranked_columns = np.argsort(values_at_selection, kind="stable")
    ranks = np.rint(np.asarray(quantiles) * (len(ranked_columns) - 1)).astype(int)
    return ranked_columns[ranks]


def make_figure(data_folder, baseline_pfpr, output_name):
    data_dir = DATA_ROOT / data_folder / "data"
    dates = pd.date_range("2008-01-01", "2042-01-01", freq="MS")
    plot_start = pd.Timestamp("2022-01-01")
    plot_end = pd.Timestamp("2042-01-01")
    # The four-round MDA schedule ends on 2022-04-16. The October monthly
    # snapshot is the closest available observation to six months afterward.
    selection_date = pd.Timestamp("2022-10-01")
    plot_mask = (dates >= plot_start - pd.DateOffset(years=2)) & (dates <= plot_end)
    selection_row = int(np.flatnonzero(dates == selection_date)[0])
    years = (dates[plot_mask] - plot_start).days / 365.2425

    matplotlib.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    })
    fig, axes = plt.subplots(4, 3, figsize=(22.42, 13.98), sharex=True)

    prevalence_max = 2.5 if baseline_pfpr == 2 else 8.0
    prevalence_ticks = (
        [0.0, 1.0, 2.0]
        if baseline_pfpr == 2
        else [0.0, 2.0, 4.0, 6.0, 8.0]
    )

    for row, scenario in enumerate(SCENARIOS):
        scenario_index = SCENARIO_FILE_INDEX[scenario]
        four_mda_set = 4 * 4 + scenario_index
        zero_mda_set = scenario_index
        c580y_four = _read_runs(data_dir, four_mda_set, "C580Y")
        c580y_zero = _read_runs(data_dir, zero_mda_set, "C580Y")

        selected_four = _run_columns_by_rank(
            c580y_four[selection_row], RUN_QUANTILES
        )
        upper_line_override = UPPER_LINE_OVERRIDES.get((data_folder, scenario_index))
        if upper_line_override is not None:
            selected_four[-1] = upper_line_override
        selected_zero = _run_columns_by_rank(
            c580y_zero[selection_row], (0.50,)
        )[0]

        for col, metric in enumerate(METRICS):
            ax = axes[row, col]
            four_mda = _read_runs(data_dir, four_mda_set, metric)
            zero_mda = _read_runs(data_dir, zero_mda_set, metric)
            lower, upper = np.percentile(four_mda, [1, 99], axis=1)

            ax.fill_between(
                years,
                lower[plot_mask],
                upper[plot_mask],
                color=PURPLE,
                alpha=0.18,
                linewidth=0,
                zorder=1,
            )
            for run_column in selected_four:
                ax.plot(
                    years,
                    four_mda[plot_mask, run_column],
                    color=PURPLE,
                    linewidth=0.85,
                    alpha=0.95,
                    zorder=3,
                )
            ax.plot(
                years,
                zero_mda[plot_mask, selected_zero],
                color=GRAY,
                linewidth=1.05,
                zorder=2,
            )

            ax.set_xlim(-2, 20)
            ax.set_xticks([-2, 0, 5, 10, 15])
            ax.grid(True, color="#d8d8d8", linewidth=0.6, alpha=0.8)
            ax.text(
                0.025,
                0.94,
                "ABCDEFGHIJKL"[row * 3 + col],
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=15,
                fontweight="bold",
            )

            if col == 0:
                ax.set_ylim(0, prevalence_max)
                ax.set_yticks(prevalence_ticks)
                ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=0))
                ax.set_ylabel(SCENARIO_LABELS[row], labelpad=12)
            else:
                ax.set_ylim(1e-4, 1)
                ax.set_yscale("log")
                ax.set_yticks([1e-3, 1e-2, 1e-1, 1])
                ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
                ax.yaxis.set_minor_formatter(ticker.NullFormatter())

            if row == 0:
                ax.set_title(METRIC_TITLES[col])
            if row == 3:
                ax.set_xlabel("YEAR")

    fig.tight_layout()
    output_path = OUTPUT_ROOT / output_name
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(output_path)

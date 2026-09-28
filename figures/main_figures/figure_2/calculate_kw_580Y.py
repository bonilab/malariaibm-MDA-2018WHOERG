#!/usr/bin/env python3
"""Recalculate the published Kruskal-Wallis tests for 580Y frequency.

Compares five MDA-round groups (0-4), each with 1,000 simulation runs,
at output row 229 (the paper's five-year 580Y outcome timepoint, matching the published Figure 3B medians).
Uses the same tie-corrected asymptotic chi-square approximation as
R's stats::kruskal.test, without requiring SciPy or R.
"""
from collections import Counter
from csv import reader, writer
from math import exp, floor, log, log1p, log10
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIGURES = {
    "Figure 2": HERE,
    "Figure 3": HERE.parent / "figure_3",
}
TIME_ROW = 228
RUNS_PER_GROUP = 1000
# figure2.py / Figure3.py map mda*4 + 3 to no import, mda*4 + 2 to import.
SCENARIOS = {"B (no resistance import)": 3, "E (resistance import)": 2}


def read_group(path):
    with path.open(newline="") as f:
        rows = list(reader(f))
    if TIME_ROW >= len(rows):
        raise ValueError(f"{path}: missing output row {TIME_ROW}")
    values = [float(v) for v in rows[TIME_ROW] if v.strip()]
    if len(values) != RUNS_PER_GROUP:
        raise ValueError(f"{path}: expected {RUNS_PER_GROUP} runs, found {len(values)}")
    return values


def kruskal_wallis(groups):
    """Return tie-corrected H and its chi-square(df=k-1) asymptotic p-value."""
    pooled = sorted((value, group_index) for group_index, group in enumerate(groups) for value in group)
    n = len(pooled)
    rank_sums = [0.0] * len(groups)
    ties = Counter(value for value, _ in pooled)
    tie_term = sum(t ** 3 - t for t in ties.values())

    i = 0
    while i < n:
        j = i + 1
        while j < n and pooled[j][0] == pooled[i][0]:
            j += 1
        average_rank = ((i + 1) + j) / 2.0
        for _, group_index in pooled[i:j]:
            rank_sums[group_index] += average_rank
        i = j

    h = 12.0 / (n * (n + 1)) * sum(
        rank_sum * rank_sum / len(group)
        for rank_sum, group in zip(rank_sums, groups)
    ) - 3.0 * (n + 1)
    correction = 1.0 - tie_term / (n ** 3 - n)
    if correction <= 0:
        raise ValueError("Tie correction is zero or negative")
    h /= correction

    # Survival function for chi-square with 4 degrees of freedom.
    x = h / 2.0
    log_p = -x + log1p(x)
    log10_p = log_p / log(10.0)
    p = exp(log_p) if log_p > -745.0 else 0.0
    exponent = floor(log10_p)
    p_scientific = f"{10 ** (log10_p - exponent):.7g}e{exponent:+d}"
    return h, p, p_scientific, log10_p


results = []
for figure, data_dir in FIGURES.items():
    for panel, scenario_index in SCENARIOS.items():
        groups = []
        for mda in range(5):
            run_set = mda * 4 + scenario_index
            path = data_dir / "data" / f"{run_set}_C580Y.csv"
            groups.append(read_group(path))
        h, p, p_scientific, log10_p = kruskal_wallis(groups)
        results.append((figure, panel, TIME_ROW, h, p_scientific, log10_p))
        print(f"{figure} {panel}: H={h:.6g}, p≈{p_scientific}, log10(p)={log10_p:.6f}")

out = HERE / "kruskal_wallis_580Y_year5.csv"
with out.open("w", newline="") as f:
    w = writer(f)
    w.writerow(["figure", "comparison", "output_row", "H_tie_corrected", "p_value_chi_square_df4", "log10_p_value"])
    w.writerows(results)
print(f"Saved {out}")

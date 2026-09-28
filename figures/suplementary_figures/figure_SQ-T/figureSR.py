"""Regenerate Supplementary Figure R from the Figure S2 run-level outputs."""

from figure_s_qrst_common import make_figure


if __name__ == "__main__":
    make_figure("FigureS2", baseline_pfpr=5, output_name="FigureSR.png")

"""Regenerate Supplementary Figure T from the Figure 3 run-level outputs."""

from figure_s_qrst_common import make_figure


if __name__ == "__main__":
    make_figure("Figure3", baseline_pfpr=5, output_name="FigureST.png")

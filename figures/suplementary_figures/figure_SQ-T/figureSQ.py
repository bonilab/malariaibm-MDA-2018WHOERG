"""Regenerate Supplementary Figure Q from the Figure 2 run-level outputs."""

from figure_s_qrst_common import make_figure


if __name__ == "__main__":
    make_figure("Figure2", baseline_pfpr=2, output_name="FigureSQ.png")

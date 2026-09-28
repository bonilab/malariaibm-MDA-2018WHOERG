"""Regenerate Supplementary Figure S from the Figure S1 run-level outputs."""

from figure_s_qrst_common import make_figure


if __name__ == "__main__":
    make_figure("FigureS1", baseline_pfpr=2, output_name="FigureSS.png")

"""Palmer penguins scatter plot in Altair.

Usage (from this folder or any other):
    python plot.py
"""

from pathlib import Path

import altair as alt
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "penglings.csv"
IMG = ROOT.parent / "img"

SPECIES = ["Adelie", "Chinstrap", "Gentoo"]
COLORS = ["#FB7708", "#830FBF", "#0E7877"]


def load_penguins(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    for column in ("flipper_length_mm", "body_mass_g", "bill_length_mm"):
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df = df.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])
    df["sex"] = df["sex"].fillna("unknown").replace({"": "unknown"})
    return df


def build_chart(df: pd.DataFrame) -> alt.Chart:
    # Empty legend selections match every point, so the default view stays at 0.8.
    focus = alt.selection_point(fields=["species"], bind="legend")
    return (
        alt.Chart(df)
        .mark_circle()
        .encode(
            x=alt.X(
                "flipper_length_mm:Q",
                title="Flipper Length (mm)",
                scale=alt.Scale(domain=[165, 235], zero=False),
                axis=alt.Axis(values=list(range(170, 231, 10))),
            ),
            y=alt.Y(
                "body_mass_g:Q",
                title="Body Mass (g)",
                scale=alt.Scale(domain=[2500, 6500], zero=False),
                axis=alt.Axis(values=list(range(3000, 6501, 500))),
            ),
            color=alt.Color(
                "species:N",
                title="Species",
                scale=alt.Scale(domain=SPECIES, range=COLORS),
            ),
            size=alt.Size(
                "bill_length_mm:Q",
                title="Bill Length (mm)",
                scale=alt.Scale(domain=[32.1, 59.6], range=[50, 616]),
                legend=None,
            ),
            opacity=alt.condition(focus, alt.value(0.8), alt.value(0.12)),
            tooltip=[
                alt.Tooltip("species:N", title="Species"),
                alt.Tooltip("island:N", title="Island"),
                alt.Tooltip("sex:N", title="Sex"),
                alt.Tooltip("flipper_length_mm:Q", title="Flipper length (mm)", format=".0f"),
                alt.Tooltip("body_mass_g:Q", title="Body mass (g)", format=".0f"),
                alt.Tooltip("bill_length_mm:Q", title="Bill length (mm)", format=".1f"),
            ],
        )
        .add_params(focus)
        .properties(
            width=640,
            height=440,
            title="Flipper length and body mass of Palmer penguins",
        )
        .configure_axis(
            labelFont="Segoe UI",
            titleFont="Segoe UI",
            labelFontSize=12,
            titleFontSize=13,
            gridColor="#ececec",
        )
        .configure_title(
            font="Segoe UI",
            fontSize=16,
            anchor="start",
            color="#222222",
        )
        .configure_legend(
            labelFont="Segoe UI",
            titleFont="Segoe UI",
            orient="right",
        )
        .configure_view(stroke=None)
    )


def main() -> None:
    df = load_penguins(DATA)
    chart = build_chart(df)
    IMG.mkdir(exist_ok=True)
    chart.save(ROOT / "penguins.html")
    chart.save(IMG / "altair.png", scale_factor=2)
    print(f"plotted {len(df)} penguins")


if __name__ == "__main__":
    main()

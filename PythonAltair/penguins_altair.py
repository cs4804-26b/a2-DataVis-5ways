"""Recreate the penguins scatterplot with Altair
"""

from pathlib import Path

import altair as alt
import pandas as pd

HERE = Path(__file__).resolve().parent
CSV = HERE.parent / "penglings.csv"

# Three  colours
SPECIES_COLORS = ["#F2A03D", "#8E44AD", "#2A7F7F"]


def load_data() -> pd.DataFrame:
    """Load and clean the penguin observations."""
    df = pd.read_csv(CSV)

    # Drop observations that are missing any variables
    df = df.dropna(
        subset=["bill_length_mm", "flipper_length_mm", "body_mass_g"]
    ).copy()

    # Keep the colour assignment
    df["species"] = pd.Categorical(
        df["species"], categories=["Adelie", "Chinstrap", "Gentoo"], ordered=True
    )
    return df


def build_chart(df: pd.DataFrame) -> alt.Chart:
    """Build the scatterplot with colour, size, and tooltip encodings."""
    return (
        alt.Chart(df, title="Penguin body mass vs. flipper length")
        .mark_circle(opacity=0.8, stroke=None)
        .encode(
            x=alt.X(
                "flipper_length_mm:Q",
                title="Flipper Length (mm)",
                scale=alt.Scale(domain=[168, 234], nice=False),
                axis=alt.Axis(values=list(range(170, 231, 10))),
            ),
            y=alt.Y(
                "body_mass_g:Q",
                title="Body Mass (g)",
                scale=alt.Scale(domain=[2700, 6300], nice=False),
                axis=alt.Axis(values=list(range(3000, 6001, 1000))),
            ),
            color=alt.Color(
                "species:N",
                title="species",
                scale=alt.Scale(domain=["Adelie", "Chinstrap", "Gentoo"],
                                range=SPECIES_COLORS),
                legend=alt.Legend(orient="right"),
            ),
            size=alt.Size(
                "bill_length_mm:Q",
                title="bill_length_mm",
                scale=alt.Scale(range=[30, 240]),
                legend=alt.Legend(orient="right", values=[40, 50]),
            ),
            tooltip=[
                alt.Tooltip("species:N", title="Species"),
                alt.Tooltip("island:N", title="Island"),
                alt.Tooltip("flipper_length_mm:Q", title="Flipper (mm)"),
                alt.Tooltip("body_mass_g:Q", title="Body mass (g)"),
                alt.Tooltip("bill_length_mm:Q", title="Bill (mm)"),
                alt.Tooltip("sex:N", title="Sex"),
            ],
        )
        .properties(width=640, height=480, background="#F5F5F5")
        .configure_axis(
            grid=True,
            gridColor="#FFFFFF",
            gridWidth=1.5,
            domainColor="#BDBDBD",
            tickColor="#BDBDBD",
            labelColor="#333333",
            titleColor="#111111",
            titleFontSize=14,
            labelFontSize=12,
        )
        .configure_view(stroke=None)
        .configure_title(fontSize=15, anchor="start", color="#111111")
        .interactive()
    )


def main() -> None:
    df = load_data()
    chart = build_chart(df)

    html_path = HERE / "penguins_altair.html"
    png_path = HERE / "penguins_altair.png"

    chart.save(html_path)
    chart.save(png_path, scale_factor=2)

    print(f"{len(df)} observations plotted")
    print(f"wrote {html_path}")
    print(f"wrote {png_path}")


if __name__ == "__main__":
    main()

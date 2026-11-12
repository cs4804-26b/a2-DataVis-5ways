from pathlib import Path

import altair as alt
import pandas as pd

here = Path(__file__).parent
# Works whether the folder is next to penglings.csv or inside the repo root
csv = next(p for p in (here / "penglings.csv", here.parent / "penglings.csv") if p.exists())

df = pd.read_csv(csv, na_values=["NA", ""])
df = df.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm", "species"])

species_colors = alt.Scale(
    domain=["Adelie", "Chinstrap", "Gentoo"],
    range=["#ff8c00", "#a52bd4", "#008b8b"],
)

chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.8)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(domain=[169, 234], zero=False),
            axis=alt.Axis(values=list(range(170, 231, 10))),
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(domain=[2500, 6500], zero=False),
            axis=alt.Axis(values=list(range(3000, 6001, 1000)), format="d"),
        ),
        color=alt.Color("species:N", title="Species", scale=species_colors),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            scale=alt.Scale(zero=False, range=[20, 250]),
            legend=alt.Legend(values=[40, 50]),
        ),
    )
    .properties(width=600, height=400)
)

chart.save(here / "altair-penguins.png", scale_factor=2)
print(f"Plotted {len(df)} penguins")
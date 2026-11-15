from pathlib import Path

import altair as alt
import pandas as pd

csv_path = Path(__file__).resolve().parent.parent / "penglings.csv"
penguins = pd.read_csv(csv_path).dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])
chart = alt.Chart(penguins).mark_circle(opacity=0.8).encode(
    x = alt.X("flipper_length_mm:Q", title="Flipper length (mm)", scale=alt.Scale(domain=[169, 234], nice=False), axis=alt.Axis(values=list(range(170, 231, 10)), grid=True),),
    y = alt.Y("body_mass_g:Q", title="Body mass (g)", scale=alt.Scale(domain=[2500, 6500], nice=False), axis=alt.Axis(values=[3000, 4000, 5000, 6000], grid=True),),
    color = alt.Color("species:N", title="Species", scale=alt.Scale(domain=["Adelie", "Gentoo", "Chinstrap"], range=["#4b77a6", "#f08a24", "#d95556"], ), ),
    size = alt.Size("bill_length_mm:Q", title="Bill length (mm)", scale=alt.Scale(domain=[32.1, 59.6], range=[20, 105], nice=False), legend=alt.Legend(values=[40, 50]), ),
    tooltip = [
        alt.Tooltip("species:N", title="Species"),
        alt.Tooltip("flipper_length_mm:Q", title="Flipper length (mm)"),
        alt.Tooltip("body_mass_g:Q", title="Body mass (g)"),
        alt.Tooltip("bill_length_mm:Q", title="Bill length (mm)"),
    ],
    ).properties(width=600, height=400)

chart.save(Path(__file__).with_name("scatterplot.html"))
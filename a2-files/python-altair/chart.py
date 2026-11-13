# Penguin scatterplot in Python + Altair
# Run from the repo root:  python python-altair/chart.py
# Needs: pip install altair vl-convert-python pandas
import altair as alt
import pandas as pd

df = pd.read_csv("penglings.csv").dropna(
    subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

# Clicking a species in the legend highlights it and fades the others
pick = alt.selection_point(fields=["species"], bind="legend")

chart = alt.Chart(df).mark_circle().encode(
    x=alt.X("flipper_length_mm:Q", title="Flipper Length (mm)",
            scale=alt.Scale(zero=False, domain=[170, 235])),
    y=alt.Y("body_mass_g:Q", title="Body Mass (g)",
            scale=alt.Scale(zero=False)),
    color=alt.Color("species:N", scale=alt.Scale(
        domain=["Adelie", "Chinstrap", "Gentoo"],
        range=["#FF8C00", "#A034F0", "#159090"])),
    # zero=False matters here, otherwise the size scale starts at 0 and
    # every penguin's bill (32 to 60 mm) ends up looking about the same size
    size=alt.Size("bill_length_mm:Q", scale=alt.Scale(zero=False, range=[10, 220]),
                  legend=alt.Legend(values=[40, 50])),
    opacity=alt.condition(pick, alt.value(0.8), alt.value(0.08)),
    tooltip=["species", "island", "flipper_length_mm", "body_mass_g", "bill_length_mm", "sex"],
).add_params(pick).properties(width=560, height=360).interactive()

chart.save("python-altair/chart.html")
chart.save("img/altair.png", scale_factor=2)

import altair as alt
import pandas as pd

df = pd.read_csv("data/penglings.csv")
colors = {
    "Adelie":"#FF9633",
    "Chinstrap":"#801BBA",
    "Gentoo":"#14978C"
}

chart = alt.Chart(df).mark_circle(opacity=0.8).encode(
    alt.X('flipper_length_mm').scale(domain=(160, 240)),
    alt.Y('body_mass_g').scale(domain=(2500, 6500)),
    color=alt.Color("species", scale=alt.Scale(domain=colors.keys(), range=colors.values())),
    size=alt.Size('bill_length_mm', 
                  scale=alt.Scale(domain=[min(df["bill_length_mm"]), max(df["bill_length_mm"])],
                                  range=[28, 140])
    )
)
chart.save("../img/altair_vis.png")
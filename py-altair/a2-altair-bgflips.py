import pandas as pd
import altair as alt

df = pd.read_csv("penglings.csv")
dfclean = df.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm", "species"])

chart = alt.Chart(dfclean).mark_circle(opacity=0.8).encode(
    x=alt.X("flipper_length_mm:Q",
            scale=alt.Scale(zero=False),
            title="Flipper Length (mm)"),
    y=alt.Y("body_mass_g:Q",
            scale=alt.Scale(zero=False),
            title="Body Mass (g)"),
    color=alt.Color("species:N",
                    scale=alt.Scale(
                        domain=["Adelie", "Chinstrap", "Gentoo"],
                        range=["darkorange", "darkorchid", "darkcyan"]
                    ),
                    title="species"),
    size=alt.Size("bill_length_mm:Q",
                  scale=alt.Scale(zero=False, range=[20, 300]),
                  title="Bill Length (mm)")
).properties(
    width=550,
    height=400,
    background="lightgray"
)

chart.save("a2-altair-picture-bgflips.png")

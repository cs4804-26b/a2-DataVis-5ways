import altair as alt
import pandas as pd

# load and drop na rows
df = pd.read_csv("../penglings.csv")
df = df.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

chart = alt.Chart(df).mark_circle(opacity=0.8).encode(
    x=alt.X("flipper_length_mm", title="Flipper Length (mm)", scale=alt.Scale(zero=False)),
    y=alt.Y("body_mass_g", title="Body Mass (g)", scale=alt.Scale(zero=False)),
    color=alt.Color("species", title="Species",
                    scale=alt.Scale(domain=["Adelie", "Chinstrap", "Gentoo"],
                                    range=["#ff8c00", "#a034f0", "#159090"])),
    size=alt.Size("bill_length_mm", title="Bill Length (mm)", scale=alt.Scale(zero=False)),
    tooltip=["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"]
).properties(width=550, height=400).interactive()

# html is interactive, png is for the readme
chart.save("penguins_altair.html")
chart.save("../img/altair.png", scale_factor=2)

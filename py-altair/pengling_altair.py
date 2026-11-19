import altair as alt
import pandas as pd

source = pd.read_csv("./penglings.csv")

domain=['Adelie', 'Chinstrap', 'Gentoo']
colors=["#ff8e08","#9933cc","#158f8f"]

chart = alt.Chart(source).mark_circle().encode(
    alt.X('flipper_length_mm', title = "Flipper Length (mm)").scale(zero=False),
    alt.Y('body_mass_g', title = "Body Mass (g)").scale(zero=False),
    alt.Size('bill_length_mm').scale(zero=False),
    color=alt.Color('species').scale(domain=domain,range=colors)
).configure_mark(
    opacity = 0.8
).configure(
    background = "#ebebeb"
).configure_axis(
    gridColor="#fdfdfd"
)

chart.save("pengling_altair.html")

import pandas as pd
import altair as alt

# Load data
data = pd.read_csv("../penglings.csv")
data = data.dropna(subset=[
    "species",
    "bill_length_mm",
    "flipper_length_mm",
    "body_mass_g"
])

# Define species colors
speciesColors = {
    "Adelie": "#ff922e",
    "Chinstrap": "#a83fd1",
    "Gentoo": "#159b9b"
}

chart = alt.Chart(data).mark_circle(
    opacity=0.75,
    strokeWidth=1.5
).encode(
    x = alt.X(
        "flipper_length_mm:Q",
        title="Flipper Length (mm)",
        scale=alt.Scale(domain=[170, 234]),
        axis=alt.Axis(tickCount=4)
    ),
    y = alt.Y(
        "body_mass_g:Q",
        title="Body Mass (g)",
        scale=alt.Scale(domain=[2500, 6500]),
        axis=alt.Axis(tickCount=9)
    ),
    size=alt.Size(
        "bill_length_mm:Q",
        title="Bill Length (mm)",
        scale=alt.Scale(range=[20, 1000]),
        legend=alt.Legend(values=[40, 50])
    ),
    color=alt.Color(
        "species:N",
        title="Species",
        scale=alt.Scale(
            domain=list(speciesColors.keys()),
            range=list(speciesColors.values())
        )
    ),
).properties(
    width=700,
    height=500
).configure(
    background="white"
).configure_view(
    stroke=None
).configure_axis(
    grid=True,
    gridColor="white",
    gridWidth=2,
    domainColor="#666666",
    tickColor="#666666"
).configure_legend(
    titleFontSize=14,
    labelFontSize=12
)

chart = chart.interactive()
chart.save("penguins.html")
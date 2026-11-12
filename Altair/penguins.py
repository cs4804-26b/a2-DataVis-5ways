import pandas as pd
import altair as alt
# Load dataset
penguins = pd.read_csv("penglings.csv")

# Remove the missing measurements
penguins = penguins.dropna(
    subset=[
        "species",
        "bill_length_mm",
        "flipper_length_mm",
        "body_mass_g"
    ]
)

# Set color for species
species_colors = alt.Scale(
    domain=["Adelie", "Chinstrap", "Gentoo"],
    range=["#E09719", "#B363C7", "#27f5b4"]
)
# Create the scatterplot
chart = alt.Chart(penguins).mark_circle(
    opacity=0.8
).encode(
    # Flipper length on x-axis
    x=alt.X(
        "flipper_length_mm:Q",
        title="Flipper Length (mm)",
        scale=alt.Scale(domain=[170, 235])
    ),
    # Body mass on y-axis
    y=alt.Y(
        "body_mass_g:Q",
        title="Body Mass (g)",
        scale=alt.Scale(domain=[2500, 6500])
    ),
    # Color represents penguin species
    color=alt.Color(
        "species:N",
        title="Species",
        scale=species_colors
    ),
    # Size represents bill length
    size=alt.Size(
        "bill_length_mm:Q",
        title="Bill Length (mm)",
        scale=alt.Scale(range=[30, 300])
    )
).properties(
    title="Penguin Flipper Length vs Body Mass",
    width=850,
    height=550
).configure_axis(
    grid=True
).configure_view(
    stroke=None
)
# Save visual as HTML file
chart.save("altair/penguins.html")

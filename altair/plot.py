import pandas as pd
import altair as alt
from pathlib import Path

# Load the dataset
file_path = Path(__file__).resolve().parent.parent / "penglings.csv"
penguins = pd.read_csv(file_path, na_values=["NA"])

# Skip missing data
penguins = penguins.dropna(subset=[
  "species",
  "flipper_length_mm",
  "body_mass_g",
  "bill_length_mm"
])

#Pick colors for each species
species_colors = ["#E69F00", "#56B4E9", "#009E73"]

# Create the scatterplot
chart = alt.Chart(penguins).mark_circle(opacity = 0.8).encode(
  x=alt.X(
    "flipper_length_mm:Q",
    title="Flipper Length (mm)",
    scale=alt.Scale(domain=[165, 235])
  ),
  y=alt.Y(
    "body_mass_g:Q",
    title="Body Mass (g)",
    scale=alt.Scale(domain=[2500, 6500])
  ),
  color = alt.Color(
    "species:N",
    scale=alt.Scale(
      domain=["Adelie", "Chinstrap", "Gentoo"],
      range = species_colors
    )
  ),
  size=alt.Size(
    "bill_length_mm:Q",
    title="Bill Length (mm)"
  ),
  tooltip=[
    alt.Tooltip("species:N", title="Species"),
    alt.Tooltip("flipper_length_mm:Q", title="Flipper Length"),
    alt.Tooltip("body_mass_g:Q", title="Body Mass"),
    alt.Tooltip("bill_length_mm:Q", title="Bill Length")
                ]
).properties(
  width=650,
  height=450,
  title="Penguin Body Mass and Flipper Length"
)

# Save the chart 
chart.save(
  Path(__file__).resolve().parent / "altair.html"
)
  
    

  

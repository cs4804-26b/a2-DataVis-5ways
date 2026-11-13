
from pathlib import Path

import pandas as pd
import altair as alt

# Find the main assignment folder
project_folder = Path(__file__).resolve().parent.parent

# Load the penguin dataset
penguins = pd.read_csv(
    project_folder / "penglings.csv",
    na_values=["NA"]
)

# Remove rows with missing measurements
needed = [
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm"
]

penguins = penguins.dropna(subset=needed)

# Check the cleaned data
print("Total penguins:", len(penguins))
print(penguins["species"].value_counts())



# Use the same species colors
species_colors = ["#FF8C00", "#A536D2", "#008B8B"]

# Create the scatterplot
base_chart = alt.Chart(penguins).mark_circle(
    opacity=0.8
).encode(
    x=alt.X(
        "flipper_length_mm:Q",
        title="Flipper Length (mm)",
        scale=alt.Scale(domain=[169, 234], zero=False, nice=False),
        axis=alt.Axis(values=list(range(170, 231, 10)))
    ),

    y=alt.Y(
        "body_mass_g:Q",
        title="Body Mass (g)",
        scale=alt.Scale(domain=[2500, 6500], zero=False, nice=False),
        axis=alt.Axis(values=[3000, 4000, 5000, 6000])
    ),

    color=alt.Color(
        "species:N",
        scale=alt.Scale(
            domain=["Adelie", "Chinstrap", "Gentoo"],
            range=species_colors
        ),
        legend=alt.Legend(title="Species")
    ),

    size=alt.Size(
        "bill_length_mm:Q",
        scale=alt.Scale(
            domain=[30, 60],
            range=[40, 450]
        ),
        legend=alt.Legend(
            title="Bill Length (mm)",
            values=[40, 50]
        )
    ), 

   tooltip=[
        alt.Tooltip("species:N", title="Species"),
        alt.Tooltip(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)"
        ),
        alt.Tooltip(
            "body_mass_g:Q",
            title="Body Mass (g)",
            format=",d"
        ),
        alt.Tooltip(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            format=".1f"
        ),
        alt.Tooltip("island:N", title="Island"),
        alt.Tooltip("year:O", title="Year")
    ] 
).properties(
    width=730,
    height=490,
    background="white"
)


# Apply consistent styling to the chart
def style_chart(chart):
    return (
        chart
        .configure_view(
            fill="#EBEBEB",
            stroke=None
        )
        .configure_axis(
            gridColor="white",
            gridWidth=1,
            tickSize=0,
            domain=False,
            labelFont="Arial",
            titleFont="Arial",
            labelFontSize=12,
            titleFontSize=14,
            labelPadding=8
        )
        .configure_legend(
            orient="right",
            labelFont="Arial",
            titleFont="Arial",
            labelFontSize=12,
            titleFontSize=12,
            padding=10
        )
    )



# Make the main static chart
static_chart = style_chart(base_chart)

# Save it in the img folder
image_folder = project_folder / "img"
image_folder.mkdir(exist_ok=True)

static_chart.save(
    image_folder / "python.png",
    scale_factor=2
)

print("Saved python.png")


# Create a selection connected to the species legend
species_selection = alt.selection_point(
    fields=["species"],
    bind="legend"
)

# Create the interactive version
interactive_chart = base_chart.encode(
    opacity=alt.condition(
        species_selection,
        alt.value(0.8),
        alt.value(0.12)
    )
).add_params(
    species_selection
)

# Allow zooming and panning
interactive_chart = interactive_chart.interactive()

# Apply the same styling as the static chart
interactive_chart = style_chart(interactive_chart)

# Save the interactive version as HTML
interactive_chart.save(
    project_folder / "python-altair" / "penguins-interactive.html"
)

print("Saved penguins-interactive.html")


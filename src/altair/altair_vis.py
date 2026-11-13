
import pandas as pd
import altair as alt
import webbrowser
import os

# Load and clean dataset
penguin_data = pd.read_csv("./penglings.csv")

penguin_data = penguin_data.dropna(
    subset=[
        "flipper_length_mm",
        "body_mass_g",
        "bill_length_mm",
        "species"
    ]
)

# Define colors
species_colors = {
    "Adelie": "#e11d48",
    "Chinstrap": "#ecb425",
    "Gentoo": "#2563EB"
}

# Shared color scale
color_scale = alt.Scale(
    domain=list(species_colors.keys()),
    range=list(species_colors.values())
)

# Interactive selection
brush = alt.selection_interval(
    encodings=["x", "y"]
)

# Main scatterplot
scatterplot = alt.Chart(penguin_data).mark_circle(
    opacity=0.8,
    stroke="#333333",
    strokeWidth=0.5
).encode(
    x=alt.X(
        "flipper_length_mm:Q",
        title="Flipper Length (mm)",
        scale=alt.Scale(zero=False)
    ),
    y=alt.Y(
        "body_mass_g:Q",
        title="Body Mass (g)",
        scale=alt.Scale(zero=False)
    ),
    color=alt.Color(
        "species:N",
        scale=color_scale,
        legend=alt.Legend(
            title="Species",
            symbolSize=150,
            symbolStrokeColor="#333333",
            symbolStrokeWidth=0.5
        )
    ),
    size=alt.Size(
        "bill_length_mm:Q",
        scale=alt.Scale(zero=False),
        legend=alt.Legend(
            title="Bill Length (mm)",
            symbolFillColor="#888888",
            symbolStrokeColor="#333333",
            symbolStrokeWidth=0.5,
            symbolOpacity=0.8
        )
    )
).add_params(
    brush
).properties(
    width=750,
    height=500,
    title=alt.Title(
        "Penguin Measurements",
        subtitle="Click and drag across the scatterplot to highlight penguins and view their body mass distribution below."
    )
)

# Body mass distribution
histogram = alt.Chart(penguin_data).mark_bar(
    opacity=0.8
).encode(
    x=alt.X(
        "body_mass_g:Q",
        bin=alt.Bin(maxbins=20),
        title="Body Mass (g)"
    ),
    y=alt.Y(
        "count():Q",
        title="Number of Penguins"
    ),
    color=alt.Color(
        "species:N",
        scale=color_scale,
        legend=None
    )
).transform_filter(
    brush
).properties(
    width=750,
    height=180,
    title=alt.Title(
        "Body Mass Distribution of Selected Penguins",
        fontSize=16
    )
)

# Combine charts
dashboard = alt.vconcat(
    scatterplot,
    histogram
).resolve_scale(
    color="shared"
).configure(
    background="#F7F7F2",
    font="Arial"
).configure_axis(
    labelFont="Arial",
    titleFont="Arial",
    labelFontSize=11,
    titleFontSize=13,
    labelColor="#222222",
    titleColor="#222222",
    gridColor="#DDDDDD",
    gridWidth=0.7,
    domainColor="#AAAAAA",
    tickColor="#AAAAAA"
).configure_legend(
    labelFont="Arial",
    titleFont="Arial",
    labelFontSize=11,
    titleFontSize=12,
    titleFontWeight="bold",
    labelColor="#222222",
    titleColor="#222222",
    padding=8
).configure_title(
    font="Arial",
    fontSize=20,
    subtitleFont="Arial",
    subtitleFontSize=13,
    color="#222222",
    subtitleColor="#555555",
    anchor="middle"
)

# Save and open visualization in the script directory
output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "index.html"
)

dashboard.save(output_path)

# Center visualization on the page
with open(output_path, "r", encoding="utf-8") as file:
    html = file.read()

html = html.replace(
    "</head>",
    """
    <style>
        #vis {
            display: flex;
            justify-content: center;
            width: 100%;
        }
    </style>
    </head>
    """
)

with open(output_path, "w", encoding="utf-8") as file:
    file.write(html)

webbrowser.open(output_path)

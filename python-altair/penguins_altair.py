
import pandas as pd
import altair as alt

# ChatGPT assisted with the Altair code and implementation.

# Load the penguin data
penguins = pd.read_csv("penglings.csv")

# Remove penguins with missing measurements
penguins = penguins.dropna(subset=[
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm",
    "species"
])

# Some penguins have no recorded sex
penguins["sex"] = penguins["sex"].fillna("Unknown")

# Create the scatterplot
chart = alt.Chart(penguins).mark_circle(opacity=0.8).encode(
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
    title="Species",
    scale=alt.Scale(
        domain=["Adelie", "Gentoo", "Chinstrap"],
        range=["#177E89", "#59A5D8", "#E8A44D"]
    )
),


    size=alt.Size(
        "bill_length_mm:Q",
        title="Bill Length (mm)",
        scale=alt.Scale(domain=[30, 60], range=[30, 220])
    ),
    
tooltip=[
    alt.Tooltip("species:N", title="Species"),
    alt.Tooltip("island:N", title="Island"),
    alt.Tooltip("sex:N", title="Sex"),
    alt.Tooltip("year:O", title="Year"),
    alt.Tooltip("flipper_length_mm:Q", title="Flipper (mm)", format=".0f"),
    alt.Tooltip("body_mass_g:Q", title="Mass (g)", format=",.0f"),
    alt.Tooltip("bill_length_mm:Q", title="Bill (mm)", format=".1f")
]



).properties(
    width=600,
    height=400,
    title="Penguin Body Mass vs. Flipper Length"
)

# Save the chart
chart.save(
    "python-altair/penguins_altair.html",
    embed_options={"tooltip": {"theme": "dark"}}
)
chart.save("img/altair.png")

print("Altair chart created!")

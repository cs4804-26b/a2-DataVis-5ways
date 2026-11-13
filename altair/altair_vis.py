
import pandas as pd
import altair as alt

# load data w/ pandas form csv
data = pd.read_csv("penglings.csv")

# Convert columns to numeric and 
numeric_columns = [
    "bill_length_mm",
    "flipper_length_mm",
    "body_mass_g"
]

for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")


species_selection = alt.selection_point(
    fields = ["species"],
    bind = "legend"
)

axes_x = {
    "x_min": 165,
    "x_max": 235,
    "gap": 5
}

axes_y = {
    "y_min": 2500,
    "y_max": 6500,
    "gap": 500
}

peng_color = {
       "Adelie": "#F56C27",
       "Chinstrap": "#88219E",
       "Gentoo": "#685CE0"
}
# chart definition

chart = alt.Chart(data).mark_circle(
    opacity = 0.8
).encode(
    x=alt.X(
        "flipper_length_mm:Q",
        title = "Flipper Length (mm)",
        scale = alt.Scale(domain = [axes_x["x_min"], axes_x["x_max"]], zero=False),
        axis = alt.Axis(
            values = list(range(axes_x["x_min"] + axes_x["gap"], axes_x["x_max"], 10)),
            labelFontSize = 16,
            titleFontSize = 20,
            grid = True
        )
    ),

    y=alt.Y(
        "body_mass_g:Q",
        title = "Body Mass (g)",
        scale = alt.Scale(domain=[axes_y["y_min"], axes_y["y_max"]], zero=False),
        axis = alt.Axis(
            values = list(range(axes_y["y_min"] + axes_y["gap"], axes_y["y_max"], axes_y["gap"])),
            labelFontSize = 16,
            titleFontSize = 20,
            grid = True
        )
    ),

    color = alt.Color(
        "species:N",
        title = "Penguin Species",
        scale = alt.Scale(
            domain = ["Adelie", "Chinstrap","Gentoo"],
            range = ["#F56C27","#88219E","#685CE0"]
        ),
        legend = alt.Legend(
            labelFontSize = 16,
            titleFontSize = 20,
            orient = "right"
        )
    ),
    # size based on bill length
    size = alt.Size(
        "bill_length_mm:Q",
        title = "Bill Length (mm)",
        scale = alt.Scale(range=[20,500], zero = False),
    ),

    opacity=alt.condition(
        species_selection,
        alt.value(0.8),
        alt.value(0.05)
    ),
).add_params(
    species_selection
).properties(
    width = 800,
    height = 600,
    title = alt.Title(
        "Penguin Body Mass vs. Flipper Length",
        fontSize = 24
    )
).configure_axis(
    gridOpacity = 0.6,
    domainWidth = 1.5,
    tickWidth = 1.5
).configure_view(
    stroke = None
)

chart.save("penguin_scatterplot.html")


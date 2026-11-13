from pathlib import Path
import pandas as pd
import altair as alt

#Read CSV
penguinData = pd.read_csv(Path(__file__).resolve().parent.parent/"penglings.csv")

# Chart creation
altairChart = alt.Chart(penguinData).mark_circle(opacity = 0.8).encode(
    # X-axis
    x = alt.X(
        'flipper_length_mm:Q',
        title = 'Flipper Length in millimeters',
        scale = alt.Scale(zero = False)
    ),
    # Y-axis
    y = alt.Y(
        'body_mass_g:Q',
        title = 'Body Mass in grams',
        scale = alt.Scale(zero = False)
    ),

    # Color to speciess (Design Achievemebt)
    color = alt.Color(
        'species:N',
        title = 'Species',
        scale = alt.Scale(
            domain = ['Adelie', 'Chinstrap', 'Gentoo'],
            range = ['#FF7F7F', '#90EE90', '#ADD8E6']
        )
    ),
    
    # Size to bill length
    size = alt.Size(
        'bill_length_mm:Q',
        title = 'Bill Length in millimeters)',
        scale = alt.Scale(zero = False)
    ),
    # Technical Achievement: you can hover over each circle to get more details of that one circle
    tooltip = [
        alt.Tooltip('species:N', title = 'Species'),
        alt.Tooltip('island:N', title = 'Island Name'),
        alt.Tooltip('bill_length_mm:Q', title = 'Bill Length (mm)'),
        alt.Tooltip('flipper_length_mm:Q', title = 'Flipper Length (mm)'),
        alt.Tooltip('body_mass_g:Q', title = 'Body Mass (g)'),
        alt.Tooltip('sex:N', title = 'Sex'),
        alt.Tooltip('year:N', title = 'Year')
    ]
).interactive() #Design Achievement: you can interact with the generated graph
alt.themes.enable('dark') #Design Achievement: dark mode

altairChart.save(Path(__file__).resolve().parent / "scatter.html") # Creates the HTML 

# Chart starter code taken from: https://altair-viz.github.io/getting_started/overview.html#overview


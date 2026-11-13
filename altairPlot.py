import altair as alt
import pandas as pd

# Load the penguins dataset
df = pd.read_csv('penglings.csv')

# Create a scatter plot using Altair
species_colors = {
    'Adelie': '#0000ff',  # Blue
    'Chinstrap': '#ff0000',  # Red
    'Gentoo': '#00ff00'  # Green
}


df = df.dropna(subset=['flipper_length_mm', 'body_mass_g', 'species', 'bill_length_mm', 'bill_depth_mm', 'sex', 'island', 'year'])

scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('flipper_length_mm', scale=alt.Scale(zero=False)),
    y=alt.Y('body_mass_g', scale=alt.Scale(zero=False)),
    color=alt.Color('species', scale=alt.Scale(domain=list(species_colors.keys()), range=list(species_colors.values()))),
    tooltip=['species', 'flipper_length_mm', 'body_mass_g']   
)

# Save the chart as a PNG image
scatter_plot.save('Plots/Altair_Penguin_Plot.png', scale_factor=2.0)
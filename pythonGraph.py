import altair as alt
from altair.datasets import data
import pandas as pd

source = pd.read_csv('penglings.csv')
source = source.dropna(subset=['flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'species'])

domain = ["Adelie", "Gentoo", "Chinstrap" ]
range = [ "#01a2b0", "#c62423", "#ff818a"]

chart = alt.Chart(source).mark_circle(opacity=0.8).encode(
    alt.X('flipper_length_mm', title='Flipper Length (mm)').scale(zero=False),
    alt.Y('body_mass_g', title="Body Mass (g)").scale(zero=False, padding=1),
    alt.Size('bill_length_mm', title="Bill Length (mm)").scale(zero=False),
    alt.Color('species', title='Species').scale(domain=domain, range=range),
    tooltip=['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']
).interactive()

chart.save('chart.html')
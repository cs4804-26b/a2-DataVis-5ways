# used altair's reference docs 
import pandas as pd
import altair as alt

data = pd.read_csv("C:/Users/victo/OneDrive/Documents/GitHub/a2-DataVis-5ways/penglings.csv").dropna(
    subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

colors = {"Adelie": "orange", "Chinstrap": "purple", "Gentoo": "teal"}

chart = alt.Chart(data).mark_circle(opacity=0.8).encode(
    x = alt.X("flipper_length_mm:Q", scale = alt.Scale(domain=[170,235]), title="Flipper Length (mm)"),
    y = alt.Y("body_mass_g:Q", scale = alt.Scale(domain=[2500,6500]), title="Body Mass (g)"),
    color = alt.Color("species:N", title="Species", scale=alt.Scale(domain=list(colors.keys()), range=list(colors.values()))),
    size = alt.Size("bill_length_mm:Q", title="Bill Length (mm)")).properties(width=600, height=400)

# chart.show()
chart.save("altair.html")
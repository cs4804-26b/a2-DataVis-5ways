import altair as alt
import pandas as pd

# read csv and drop na
df = pd.read_csv("../penglings.csv")
penguins = df.dropna(subset = ["flipper_length_mm", "body_mass_g", "bill_length_mm"])

# tooltop allows to hover over each dot/penguin
# .interactive() allows for zooming in and out of visualiation
chart = alt.Chart(penguins).mark_circle(opacity = 0.8).encode(
    alt.X("flipper_length_mm", title = "Flipper Length (mm)").scale(zero=False),
    alt.Y("body_mass_g", title = "Body Mass (g)").scale(zero=False, padding=1),
    alt.Size("bill_length_mm", title = "Bill Length (mm)", legend=alt.Legend(values=[40, 50])).scale(zero=False),
    color= alt.Color("species", title = "Species", scale=alt.Scale(domain=["Adelie", "Chinstrap", "Gentoo"], range=["#F5A142", "#9B3FD4", "#4A9A98"])),
    tooltip=["species", "island", "flipper_length_mm", "body_mass_g", "bill_length_mm"]
).interactive()



# save to html file to view visualization
chart.save("penguins.html")


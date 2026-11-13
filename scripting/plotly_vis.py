import plotly.express as px
import pandas as pd

df = pd.read_csv("data/penglings.csv")
colors = {
    "Adelie":"#FF9633",
    "Gentoo":"#14978C",
    "Chinstrap":"#801BBA",
}
df = df.dropna(subset=['bill_length_mm'])
df["scaled_bill_length_mm"] = (df["bill_length_mm"]-25) * 4

# Simple scatter plot
fig = px.scatter(df, x="flipper_length_mm", y="body_mass_g", size="scaled_bill_length_mm",
                 color="species", color_discrete_sequence=list(colors.values()),
                 opacity=0.8)
fig.write_image("../img/plotly_vis.png")
import altair as alt
import pandas as pd

df = pd.read_csv("penglings.csv")

chart = (
    alt.Chart(df)
    .mark_circle(size=60)
    .encode(
        x="flipper_length_mm:Q",
        y="body_mass_g:Q",
        tooltip=["flipper_length_mm", "body_mass_g"],
    )
    .interactive()
)

chart.display()
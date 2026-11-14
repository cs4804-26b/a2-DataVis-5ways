from pathlib import Path 
import altair as alt 
import pandas as pd

def main():
    folder = Path(__file__).resolve().parent
    data = pd.read_csv(folder.parent / "penglings.csv")
    data = data.dropna(
        subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"]
    )
    chart = alt.Chart(data).mark_circle(opacity=0.8).encode(
        x=alt.X(
            "flipper_length_mm:Q", title="flipper length mm", scale=alt.Scale(zero=False)
        ), 
        y=alt.Y(
            "body_mass_g:Q", title="body mass g",scale=alt.Scale(zero=False)
        ), 
        color=alt.Color(
            "species:N", title="species", scale=alt.Scale(domain=["Adelie", "Chinstrap", "Gentoo"], range=["#e76f51", "#8b6bb1", "#2a9d87"])
        ), 
        size=alt.Size(
            "bill_length_mm:Q", title ="bill length mm", scale=alt.Scale(zero=True, range=[0, 250])
        ), 
        tooltip=[
            alt.Tooltip("species:N", title="Species"), 
            alt.Tooltip("flipper_length_mm:Q", title="flipper length mm"), 
            alt.Tooltip("body_mass_g:Q", title="body mass(g)"), 
            alt.Tooltip("bill_length_mm:Q", title="bill length mm")
        ]
    ).properties(
        width=700, height=450, title="penguin flipper length and mass"
    )
    chart.save(str(folder / "penguin_chart.html"))

if __name__=="__main__":
        main()

from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    ROOT / "penglings.csv",
    na_values=["NA"]
)

columns = [
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm"
]

for col in columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["species"] + columns)


colors = {
    "Adelie": "#F4A5DF",
    "Chinstrap": "#83E8A9",
    "Gentoo": "#91EAF2"
}


fig = px.scatter(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
    color="species",
    size="bill_length_mm",
    color_discrete_map=colors,
    category_orders={
        "species": ["Adelie", "Chinstrap", "Gentoo"]
    },
    opacity=0.8,
    size_max=18,
    title="Penguin Body Mass vs. Flipper Length",
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "bill_length_mm": "Bill Length (mm)",
        "species": "Species"
    },
    hover_data=[
        "species",
        "flipper_length_mm",
        "body_mass_g",
        "bill_length_mm"
    ]
)


max_bill = df["bill_length_mm"].max()
max_marker_size = 18

sizeref = 2.0 * max_bill / (max_marker_size ** 2)

fig.update_traces(
    marker=dict(
        sizeref=sizeref,
        sizemode="area",
        line=dict(width=0)
    ),
    selector=lambda trace: trace.legendgroup in colors
)


for bill_length in [40, 50]:
    fig.add_trace(
        go.Scatter(
            x=[None],
            y=[None],
            mode="markers",
            name=f"{bill_length} mm",
            legendgroup="bill_length",
            legendgrouptitle_text="Bill Length (mm)",
            marker=dict(
                size=bill_length,
                sizeref=sizeref,
                sizemode="area",
                color="#555555",
                opacity=0.8,
                line=dict(width=0)
            ),
            showlegend=True,
            hoverinfo="skip"
        )
    )


fig.update_layout(
    width=1050,
    height=700,
    template="plotly_white",

    title=dict(
        text="Penguin Body Mass vs. Flipper Length",
        font=dict(size=22),
        x=0.5,
        xanchor="center"
    ),

    font=dict(
        family="Arial",
        size=13
    ),

    legend=dict(
        orientation="v",
        x=1.02,
        y=1,
        xanchor="left",
        yanchor="top",
        tracegroupgap=20,
        groupclick="togglegroup"
    ),

    margin=dict(
        l=80,
        r=180,
        t=100,
        b=80
    ),

    plot_bgcolor="white",
    paper_bgcolor="white"
)

fig.update_xaxes(
    title_text="Flipper Length (mm)",
    range=[170, 240],
    tick0=170,
    dtick=10,
    showgrid=True,
    gridcolor="#E5E5E5",
    zeroline=False,
    showline=True,
    linecolor="#888888"
)

fig.update_yaxes(
    title_text="Body Mass (g)",
    range=[2500, 6500],
    tick0=2500,
    dtick=500,
    showgrid=True,
    gridcolor="#E5E5E5",
    zeroline=False,
    showline=True,
    linecolor="#888888"
)


output_dir = ROOT / "img"
output_dir.mkdir(parents=True, exist_ok=True)

html_path = ROOT / "plotly" / "chart.html"
png_path = output_dir / "plotly.png"

fig.write_html(
    str(html_path),
    auto_open=True
)

print(f"HTML chart saved to: {html_path}")

try:
    fig.write_image(
        str(png_path),
        scale=2
    )
    print(f"PNG chart saved to: {png_path}")

except Exception as e:
    print("PNG export failed:", e)
    print("Install Kaleido and Chrome if needed.")

print("Plotly visualization complete!")

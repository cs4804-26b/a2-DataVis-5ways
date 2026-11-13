from pathlib import Path

import altair as alt


OUTPUT_PATH = Path(__file__).resolve().parent / "index.html"

species_colors = {
    "Adelie": "#F28E2B",
    "Chinstrap": "#9B5DE5",
    "Gentoo": "#59A14F",
}

chart = (
    alt.Chart(
        alt.Data(
            url="../penglings.csv",
            format=alt.DataFormat(
                type="csv",
                parse={
                    "bill_length_mm": "number",
                    "flipper_length_mm": "number",
                    "body_mass_g": "number",
                },
            ),
        )
    )
    .mark_circle(opacity=0.8, stroke="#333333", strokeWidth=0.5)
    .encode(
        x=alt.X(
            "flipper_length_mm:Q",
            title="Flipper Length (mm)",
            scale=alt.Scale(domain=[170, 235]),
            axis=alt.Axis(tickCount=7),
        ),
        y=alt.Y(
            "body_mass_g:Q",
            title="Body Mass (g)",
            scale=alt.Scale(domain=[2500, 6500]),
            axis=alt.Axis(tickCount=6),
        ),
        color=alt.Color(
            "species:N",
            title="Species",
            scale=alt.Scale(
                domain=list(species_colors),
                range=list(species_colors.values()),
            ),
        ),
        size=alt.Size(
            "bill_length_mm:Q",
            title="Bill Length (mm)",
            scale=alt.Scale(range=[10, 500]),
        ),
        tooltip=[
            alt.Tooltip("species:N", title="Species"),
            alt.Tooltip("flipper_length_mm:Q", title="Flipper Length (mm)"),
            alt.Tooltip("body_mass_g:Q", title="Body Mass (g)"),
            alt.Tooltip("bill_length_mm:Q", title="Bill Length (mm)"),
        ],
    )
    .transform_filter(
        "isValid(datum.flipper_length_mm) && "
        "isValid(datum.body_mass_g) && "
        "isValid(datum.bill_length_mm)"
    )
    .properties(
        width=700,
        height=500,
        title="Penguin Body Mass vs. Flipper Length",
    )
    .configure_axis(
        grid=True,
        gridColor="#D8D8D8",
        gridDash=[3, 3],
        labelColor="#333333",
        titleColor="#1D1D1D",
    )
    .configure_legend(orient="right", titleColor="#1D1D1D", labelColor="#333333")
    .configure_view(stroke=None)
)

chart.save(OUTPUT_PATH)
print(f"Saved Altair chart to {OUTPUT_PATH}")

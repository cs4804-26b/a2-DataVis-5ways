import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")
data = data.dropna()

chart = alt.Chart(data).mark_point(filled=True, opacity=0.7).encode(
    x=alt.X('flipper_length_mm:Q', title='Flipper Length (mm)', scale=alt.Scale(zero=False), axis=alt.Axis(titleFontWeight='normal', grid=True, gridColor='white')),
    y=alt.Y('body_mass_g:Q', title='Body Mass (g)', scale=alt.Scale(zero=False), axis=alt.Axis(titleFontWeight='normal', grid=True, gridColor='white')),
    size=alt.Size(
        'bill_length_mm:Q',
        title='bill_length_mm',
        scale=alt.Scale(zero=False, range=[80,500]),
        legend=alt.Legend(values=[40, 50], orient='none', legendX=520, legendY=100, titleFontWeight='normal')
    ),
    color=alt.Color(
        'species:N',
        title='species',
        scale=alt.Scale(
            domain=['Adelie', 'Chinstrap', 'Gentoo'],
            range=['#ff941f', '#a83dcc', '#159995']
        ),
        legend=alt.Legend(orient='none', legendX=520, legendY=170, titleFontWeight='normal')
    )
).properties(
    width=500,
    height=350
).configure_view(
    fill='#E9E9E9'
).configure_axis(
    grid=True,
    gridColor='white',
    domainColor='white',
    tickColor='white'
).interactive()

chart.save("vega-altair/chart.html")
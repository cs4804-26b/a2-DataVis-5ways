from pathlib import Path
import pandas as pd
import datawrapper as dw
from dotenv import load_dotenv
import os

#I dont like datawrapper :(


#Data wrapper requires an api token to run so I stored it in my .env file and used dotenv to access it here
load_dotenv(
    Path(__file__).resolve().parent.parent / ".env"
)
token = os.environ["DATAWRAPPER_ACCESS_TOKEN"]


#Read CSV
penguinData = pd.read_csv(Path(__file__).resolve().parent.parent/"penglings.csv")

#To acutally make the circle size difference noticible in the graph I made the measurements
penguinData["bill_length_adjusted"] = penguinData["bill_length_mm"] - 30 

#Chart customization
chart = dw.ScatterPlot(
    title="Penguin Data using Datawrapper",
    data = penguinData,
    x_column = "flipper_length_mm",
    y_column = "body_mass_g",
    
    size="dynamic",
    size_column="bill_length_adjusted",
    max_size=14,
    
    size_legend_values_format="custom",
    size_legend_values=[5, 15, 25],
    size_legend_title_enabled=True,
    size_legend_title="Bill Length over 30mm",


    color_column="species",
    color_category={
        "Adelie": "#FF7F7F",
        "Chinstrap": "#90EE90",
        "Gentoo": "#ADD8E6"
    },
    
    #Technical advancement, tooltips/more data upon hovering over a circle
    tooltip_enabled = True,
    tooltip_sticky = False,
    tooltip_title="{{ species }} Penguin",
    tooltip_body="""
    <b>Island:</b> {{ island }}<br>
    <b>Bill Length:</b> {{ bill_length_mm }} mm<br>
    <b>Flipper Length:</b> {{ flipper_length_mm }} mm<br>
    <b>Body Mass:</b> {{ body_mass_g }} g<br>
    <b>Sex:</b> {{ sex }}<br>
    <b>Year:</b> {{ year }}
    """,

    opacity=0.8,
    show_color_key=True,
    show_size_legend=True,
    theme = 'pageflow' # I guess this is a minimal design advancement, just a darkmode theme!
)

chart.create()
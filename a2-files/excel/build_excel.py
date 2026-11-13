# Builds penguins.xlsx: a data sheet plus a native Excel bubble chart.
# The chart itself is a normal Excel chart, so you can open the file and edit it in Excel.
# Run from the repo root:  python excel/build_excel.py
import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BubbleChart, Reference, Series
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties

df = pd.read_csv("penglings.csv").dropna(
    subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])
df = df.sort_values("species")

wb = Workbook()
ws = wb.active
ws.title = "data"
cols = ["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"]
# Excel scales bubbles from 0, so a 35 mm and a 60 mm bill look almost the same.
# Hack: size the bubbles by (bill length - 30) so the differences actually show.
df["bubble_size"] = df.bill_length_mm - 30
ws.append(cols + ["bubble_size (bill - 30)"])
for row in df[cols + ["bubble_size"]].itertuples(index=False):
    ws.append(list(row))

chart = BubbleChart()
chart.style = 18
chart.title = None
chart.height, chart.width = 12, 20
chart.x_axis.title = "Flipper Length (mm)"
chart.y_axis.title = "Body Mass (g)"
chart.x_axis.scaling.min, chart.x_axis.scaling.max = 170, 235
chart.y_axis.scaling.min, chart.y_axis.scaling.max = 2500, 6500
chart.x_axis.majorUnit, chart.y_axis.majorUnit = 10, 1000
chart.x_axis.delete = chart.y_axis.delete = False
chart.legend.position = "r"

colors = {"Adelie": "FF8C00", "Chinstrap": "A034F0", "Gentoo": "159090"}

# Excel colors by series, so each species becomes its own series
start = 2
for name, group in df.groupby("species", sort=True):
    end = start + len(group) - 1
    x = Reference(ws, min_col=2, min_row=start, max_row=end)
    y = Reference(ws, min_col=3, min_row=start, max_row=end)
    size = Reference(ws, min_col=5, min_row=start, max_row=end)
    s = Series(values=y, xvalues=x, zvalues=size, title=name)
    s.graphicalProperties = GraphicalProperties(solidFill=colors[name])
    s.graphicalProperties.line = LineProperties(noFill=True)
    chart.series.append(s)
    start = end + 1

# Hack 2: Excel draws the biggest bubble at a fixed size and scales the rest to it,
# so every penguin ends up huge. An invisible "scale" bubble that is much bigger,
# parked off the chart at x = 100, makes all the real bubbles draw smaller.
ws["G1"], ws["H1"], ws["I1"] = "scale_x", "scale_y", "scale_size"
ws["G2"], ws["H2"], ws["I2"] = 100, 4000, 700
ghost = Series(values=Reference(ws, min_col=8, min_row=2), xvalues=Reference(ws, min_col=7, min_row=2),
               zvalues=Reference(ws, min_col=9, min_row=2), title="scale")
ghost.graphicalProperties = GraphicalProperties(noFill=True)
ghost.graphicalProperties.line = LineProperties(noFill=True)
chart.series.append(ghost)
from openpyxl.chart.legend import LegendEntry
chart.legend.legendEntry = [LegendEntry(idx=3, delete=True)]

ws2 = wb.create_sheet("chart", 0)
ws2.add_chart(chart, "B2")
ws2.page_setup.orientation = "landscape"
ws2.page_setup.fitToWidth = 1
ws2.sheet_properties.pageSetUpPr.fitToPage = True
wb.save("excel/penguins.xlsx")

# openpyxl has no setting for fill transparency, so patch the chart XML directly
# to give each bubble 80% opacity (alpha 80000 = 80%)
import zipfile, shutil, re, os
src, tmp = "excel/penguins.xlsx", "excel/_tmp.xlsx"
with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename.startswith("xl/charts/chart"):
            xml = data.decode()
            for hexcode in colors.values():
                xml = xml.replace(f'<a:srgbClr val="{hexcode}"/>',
                                  f'<a:srgbClr val="{hexcode}"><a:alpha val="80000"/></a:srgbClr>')
            data = xml.encode()
        zout.writestr(item, data)
shutil.move(tmp, src)

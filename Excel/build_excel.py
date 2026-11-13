"""Build the penguins scatterplot as a native Excel bubble chart

Excel cannot map a *numeric* variable to marker size in a normal scatterplot,
but a bubble chart maps x, y, and a third value (bill length) to bubble area, so
it can reproduce all three encodings from the assignment

Writes ../Excel/penguins.xlsx (or ./penguins.xlsx when run from this folder)
"""

from pathlib import Path
import re
import shutil
import tempfile
import zipfile

import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BubbleChart, Reference, Series
from openpyxl.drawing.fill import SolidColorFillProperties
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

HERE = Path(__file__).resolve().parent
CSV = HERE.parent / "penglings.csv"
OUT = HERE / "penguins.xlsx"

SPECIES = ["Adelie", "Chinstrap", "Gentoo"]
COLORS = {"Adelie": "F2A03D", "Chinstrap": "8E44AD", "Gentoo": "2A7F7F"}
OPACITY = 0.8


def load_data() -> pd.DataFrame:
    df = pd.read_csv(CSV)
    df = df.dropna(
        subset=["bill_length_mm", "flipper_length_mm", "body_mass_g"]
    ).copy()
    df["species"] = pd.Categorical(df["species"], categories=SPECIES, ordered=True)
    return df.sort_values(["species", "flipper_length_mm"]).reset_index(drop=True)


def style_header(ws, row=1, columns=None):
    for col in columns or range(1, ws.max_column + 1):
        cell = ws.cell(row=row, column=col)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="3B3B3B")
        cell.alignment = Alignment(horizontal="center")
    ws.freeze_panes = "A2"


def build_data_sheet(wb: Workbook, df: pd.DataFrame):
    """One clean table plus one contiguous x/y/size block per species."""
    ws = wb.active
    ws.title = "Data"

    columns = [
        ("species", "species"),
        ("island", "island"),
        ("bill_length_mm", "bill length (mm)"),
        ("flipper_length_mm", "flipper length (mm)"),
        ("body_mass_g", "body mass (g)"),
        ("sex", "sex"),
    ]
    ws.append([label for _, label in columns])
    for _, row in df.iterrows():
        ws.append([row[key] for key, _ in columns])
    style_header(ws)
    ws.column_dimensions["A"].width = 12
    ws.column_dimensions["B"].width = 12
    for col in "CDE":
        ws.column_dimensions[col].width = 18
    ws.column_dimensions["F"].width = 9

    # Each species gets its own x, y, size columns
    start = len(df) + 4
    ws.cell(row=start - 1, column=1, value="Bubble chart source data").font = Font(
        bold=True, size=12
    )

    blocks = {}
    col = 1
    for species in SPECIES:
        part = df[df["species"] == species]
        headers = [
            f"{species} flipper",
            f"{species} body mass",
            f"{species} bill",
        ]
        for offset, header in enumerate(headers):
            cell = ws.cell(row=start, column=col + offset, value=header)
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor=COLORS[species])
            cell.alignment = Alignment(horizontal="center")
            ws.column_dimensions[get_column_letter(col + offset)].width = max(
                ws.column_dimensions[get_column_letter(col + offset)].width or 0, 16
            )

        for i, (_, row) in enumerate(part.iterrows(), start=start + 1):
            ws.cell(row=i, column=col, value=float(row["flipper_length_mm"]))
            ws.cell(row=i, column=col + 1, value=float(row["body_mass_g"]))
            ws.cell(row=i, column=col + 2, value=float(row["bill_length_mm"]))

        blocks[species] = (
            col,
            start + 1,
            start + len(part),
        )
        col += 4

    return blocks


def build_chart(wb: Workbook, blocks):
    ws = wb.create_sheet("Chart")
    chart = BubbleChart()
    chart.title = "Penguin body mass vs. flipper length"
    chart.style = 2
    chart.bubbleScale = 15
    chart.sizeRepresents = "area"
    chart.showNegBubbles = False
    chart.width = 24.0
    chart.height = 14.5

    for species in SPECIES:
        col, first, last = blocks[species]
        data_ws = wb["Data"]
        xvalues = Reference(data_ws, min_col=col, min_row=first, max_row=last)
        yvalues = Reference(data_ws, min_col=col + 1, min_row=first, max_row=last)
        zvalues = Reference(data_ws, min_col=col + 2, min_row=first, max_row=last)

        series = Series(yvalues, xvalues, zvalues, title=species)
        series.graphicalProperties.solidFill = COLORS[species]
        series.graphicalProperties.line.solidFill = COLORS[species]
        chart.series.append(series)

    chart.x_axis.title = "Flipper Length (mm)"
    chart.y_axis.title = "Body Mass (g)"
    chart.title.overlay = False
    chart.x_axis.title.overlay = False
    chart.y_axis.title.overlay = False
    chart.x_axis.scaling.min = 170
    chart.x_axis.scaling.max = 234
    chart.x_axis.majorUnit = 10
    chart.x_axis.delete = False
    chart.y_axis.scaling.min = 2700
    # Headroom above the largest observation (6300 g)
    chart.y_axis.scaling.max = 6400
    chart.y_axis.majorUnit = 1000
    chart.y_axis.delete = False
    chart.legend.position = "r"
    chart.legend.overlay = False

    ws.add_chart(chart, "A1")
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 2
    ws.row_dimensions[1].height = 22

    # Make the chart fit on page when exported
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.print_options.horizontalCentered = True
    return ws


def apply_transparency(path: Path):
    """Add 20% transparency to every species-coloured fill in the chart XML.

    openpyxl's public API cannot write <a:alpha>, so patch the chart part after
    saving.  This is the Excel-specific hack mentioned in the README.
    """
    tmp_dir = Path(tempfile.mkdtemp())
    with zipfile.ZipFile(path) as zin:
        zin.extractall(tmp_dir)

    for chart_file in (tmp_dir / "xl" / "charts").glob("chart*.xml"):
        xml = chart_file.read_text(encoding="utf-8")
        for color in COLORS.values():
            xml = re.sub(
                rf'(<a:srgbClr val="{color}"\s*)/>',
                rf'\1><a:alpha val="{int(OPACITY * 100000)}"/></a:srgbClr>',
                xml,
            )
        chart_file.write_text(xml, encoding="utf-8")

    tmp_zip = path.with_suffix(".patched.xlsx")
    with zipfile.ZipFile(tmp_zip, "w", zipfile.ZIP_DEFLATED) as zout:
        for file in tmp_dir.rglob("*"):
            if file.is_file():
                zout.write(file, file.relative_to(tmp_dir))
    shutil.move(tmp_zip, path)
    shutil.rmtree(tmp_dir)


def main():
    df = load_data()
    wb = Workbook()
    blocks = build_data_sheet(wb, df)
    build_chart(wb, blocks)
    wb.save(OUT)
    apply_transparency(OUT)
    print(f"{len(df)} observations written to {OUT}")


if __name__ == "__main__":
    main()

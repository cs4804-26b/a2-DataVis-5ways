# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "altair>=6.3.0",
#     "polars>=2.1.0",
# ]
# ///
import http.server
import os
import socketserver

import altair as alt
import polars as pl

def main() -> None:
    script_dir = os.path.realpath(os.path.dirname(__file__))
    csv_path = os.path.join(os.path.dirname(script_dir), "penglings.csv")

    if not (os.path.exists(csv_path) and os.path.isfile(csv_path)):
        print("penglings.csv cannot be found in the directory above the one containing this script")
        return

    print("loading the following file", "\n", csv_path)
    df = pl.read_csv(
         csv_path,
         columns=["species", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
         schema_overrides={"bill_length_mm": pl.Float64,},
         null_values=["NA"],
     ).drop_nulls().drop_nans()
    print(df.schema)

    chart = alt.Chart(df).mark_point(
            filled=True,
            fillOpacity=0.75,
        ).encode(
            x=alt.X(
                "flipper_length_mm",
                title="Flipper Length (mm)",
                scale=alt.Scale(zero=False)
            ),
            y=alt.Y(
                "body_mass_g",
                title="Body Mass (g)",
                scale=alt.Scale(zero=False)
            ),
            color=alt.Color("species", legend=alt.Legend(title="Species")),
            size=alt.Size(
                "bill_length_mm",
                legend=alt.Legend(title="Bill Length (mm)"),
                scale=alt.Scale(zero=False, range=[20, 240]),
            ),
            tooltip=[
                alt.Tooltip("flipper_length_mm:Q", title="Flipper Length (mm)"),
                alt.Tooltip("body_mass_g:Q", title="Body Mass (g)"),
                alt.Tooltip("bill_length_mm:Q", title="Bill Length (mm)"),
                alt.Tooltip("species:N", title="Species"),
            ],
        )

    with open(os.path.join(script_dir, "index.html"), "w") as f:
        f.write(chart.to_html())

if __name__ == "__main__":
    main()

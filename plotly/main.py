# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy>=2.5.4",
#     "plotly>=7.1.0",
#     "polars>=2.1.0",
# ]
# ///
import os

import numpy as np
import polars as pl
import plotly.express as px

def main():
    script_dir = os.path.realpath(os.path.dirname(__file__))
    csv_path = os.path.join(os.path.dirname(script_dir), "penglings.csv")

    if not (os.path.exists(csv_path) and os.path.isfile(csv_path)):
        print("penglings.csv cannot be found in the directory above the one containing this script")
        return

    print("loading the following file", "\n", csv_path)
    df = pl.read_csv(
         csv_path,
         columns=["species", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
         schema_overrides={"species": pl.Categorical, "bill_length_mm": pl.Float64,},
         null_values=["NA"],
     ).drop_nulls().drop_nans()

    fig = px.scatter(
        df,
        x="flipper_length_mm",
        y="body_mass_g",
        color="species",
        size="bill_length_mm",
    )
    fig.update_traces(marker_sizemode="diameter", marker_sizeref=4)
    fig.write_html(os.path.join(script_dir, "index.html"))
    
if __name__ == '__main__':
    main()
    

    

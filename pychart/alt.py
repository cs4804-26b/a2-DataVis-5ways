import sys

import altair as alt
import pandas as pd


def main():
    if len(sys.argv) != 2:
        print("This program requires a path to the penglings data file.")
        sys.exit(1)

    df = pd.read_csv(sys.argv[1])
    chart = alt.Chart(df).mark_circle().encode( # type: ignore
        x=alt.X("flipper_length_mm:Q").scale(zero=False),
        y=alt.Y("body_mass_g:Q").scale(zero=False),
        size=alt.Size("bill_length_mm:Q").scale(zero=False, range=[10,300]),
        color=alt.Color("species:N").scale(range=["#ffaa66", "#aa66ff", "#66bbaa"])
    )
    chart.save("altair.html")


if __name__ == "__main__":
    main()

import pandas as pd
import altair as alt
data = pd.read_csv("penglings.csv", header=0)
chart = alt.Chart(data).mark_circle(opacity=.8).encode(alt.X("flipper_length_mm").title("Flipper Length (mm)").scale(zero=False), alt.Y("body_mass_g").title("Body Mass (g)").scale(zero=False), alt.Color("species").scale(domain=["Adelie", "Chinstrap", "Gentoo"], range=["#FF6E00", "#663399", "#00CED1"]), alt.Size("bill_length_mm").scale(zero=False), tooltip=["flipper_length_mm", "body_mass_g", "species", "bill_length_mm"]).properties(title="Penguin Flipper Length vs Body Mass").transform_filter('isValid(datum.flipper_length_mm) && isValid(datum.body_mass_g) && isValid(datum.bill_length_mm)').interactive()
chart.save("altairpenguin.html")
import matplotlib.pyplot as plt
import pandas as pd
import mplcursors
from mpl_interactions import panhandler, zoom_factory
data = pd.read_csv("penglings.csv")
data = data.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])
plt.subplots(layout="constrained")
plt.scatter(data["flipper_length_mm"], data["body_mass_g"], c=data["species"].map({"Adelie": "#FF6E00", "Chinstrap": "#663399", "Gentoo": "#00CED1"}), s=((data["bill_length_mm"] - data["bill_length_mm"].min()) + 5) * 10, alpha=.8)
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.title("Flipper Length (mm) vs Body Mass (g)")
color_legend = plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color,label=species, markersize=10) for color, species in zip(["#FF6E00", "#663399", "#00CED1"], ["Adelie", "Chinstrap", "Gentoo"])], title="Species", loc="upper right", bbox_to_anchor=(1.30, 1))
plt.gca().add_artist(color_legend)
plt.legend(handles=[plt.Line2D([0], [0],marker='o', color='w', markerfacecolor='black', label=f"{size} mm", markersize=size - data["bill_length_mm"].min() + 5) for size in [35, 40, 45, 50, 55]], title="Bill Length (mm)", loc="upper right", bbox_to_anchor=(1.32, 0.7), handleheight=3)
plt.grid(True)
cursor = mplcursors.cursor(hover=True)
@cursor.connect("add")
def on_add(sel):
    idx = sel.index
    row = data.iloc[idx]
    sel.annotation.set_text(f"Flipper Length: {row['flipper_length_mm']:.2f} mm\nBody Mass: {row['body_mass_g']:.2f} g")
ph = panhandler(plt.gcf(), button=1)
zf = zoom_factory(plt.gca())
plt.show()
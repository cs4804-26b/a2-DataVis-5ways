import pandas as pd
import matplotlib.pyplot as plt

# load and drop na rows
df = pd.read_csv("../penglings.csv")
df = df.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

colors = {"Adelie": "#ff8c00", "Chinstrap": "#a034f0", "Gentoo": "#159090"}

fig, ax = plt.subplots(figsize=(8, 6))

# one scatter per species so the legend works
for species, group in df.groupby("species"):
    # bill length is small so scale it up for the size
    sizes = (group["bill_length_mm"] - 30) * 6
    ax.scatter(group["flipper_length_mm"], group["body_mass_g"],
               s=sizes, c=colors[species], alpha=0.8, label=species)

ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.grid(True, color="#dddddd")
ax.set_axisbelow(True)
ax.legend(title="Species")

plt.savefig("../img/matplotlib.png", dpi=150)
plt.show()

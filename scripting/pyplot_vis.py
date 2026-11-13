import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/penglings.csv")
colors = {
    "Adelie":"#FF9633",
    "Chinstrap":"#801BBA",
    "Gentoo":"#14978C"
}

plt.clf()

for species in set(list(df["species"])):
    speciesData = df.loc[df["species"] == species]
    sizes = (speciesData["bill_length_mm"] - 25) * 4
    plt.scatter(speciesData["flipper_length_mm"], speciesData["body_mass_g"], s=sizes, label=species, alpha=0.8, color=colors[species])

plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.grid(ls="--")
plt.gca().set_axisbelow(True)
plt.legend()
plt.savefig("../img/pyplot_vis.png")
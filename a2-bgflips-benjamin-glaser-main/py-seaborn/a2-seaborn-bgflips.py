import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("penglings.csv")
dfclean = df.dropna(subset=["flipper_length_mm", "body_mass_g", "bill_length_mm", "species"])

plt.figure(figsize=(7, 4.5))
palette = {
    "Adelie": "darkorange",
    "Chinstrap": "darkorchid",
    "Gentoo": "darkcyan"
}

sns.scatterplot(
    data=dfclean,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    size="bill_length_mm",
    sizes=(50, 200),
    alpha=0.8,
    palette=palette
)

plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.xticks(range(170, 240, 10))
plt.yticks(range(3000, 7000, 1000))

plt.tight_layout()

plt.savefig("a2-seaborn-picture-bgflips.png")
plt.close()

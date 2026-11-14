import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Kamala's_files/penglings.csv")
penguin_size = data.bill_length_mm
data = data.drop(columns = ["island", "sex", "year", "bill_depth_mm"])
data = data.dropna()

fig, ax = plt.subplots(figsize=(8,5))

colorMap={'Adelie': '#f0a235b3',
          'Chinstrap':'#8535bab3',
          'Gentoo': '#27a9adb3'}


for species in colorMap:
    subset = data[data.species == species]
    ax.scatter(
        x=subset["flipper_length_mm"],
        y=subset["body_mass_g"],
        s=(2*(subset["bill_length_mm"])),
        c=colorMap[species],
        label=species
    )


ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.set_facecolor('#f0f0f0')
ax.grid(True)
##legend one
species_legend = plt.legend(title="Species", loc="upper left")
ax.add_artist(species_legend)
##legend two
size_values = [32.10, 40, 50, 59.60]
size_handles = [
    plt.scatter([],[],s=v, color="black")
    for v in size_values]
size_lables= [f"{v} mm" for v in size_values]
ax.legend(
    handles=np.array(size_handles),
    labels=size_lables,
    title="Bill Length",
    loc="upper left",
    bbox_to_anchor=(0.25, 1)
)
plt.savefig("img/pythonPlt.png",dpi=200)
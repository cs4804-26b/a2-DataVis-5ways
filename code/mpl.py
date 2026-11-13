import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/victo/OneDrive/Documents/GitHub/a2-DataVis-5ways/penglings.csv").dropna(
    subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

colors = {"Adelie": "orange", "Chinstrap": "purple", "Gentoo": "teal"}

fig, ax = plt.subplots()
scatter=None
for species, i in data.groupby("species"):
    scatter=ax.scatter(i["flipper_length_mm"], i["body_mass_g"], s=(i["bill_length_mm"]), 
               c=colors.get(species), alpha=0.8, label=species)
ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.grid(alpha=0.2)
spe = ax.legend(title="Species", loc="upper left")
ax.add_artist(spe)
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
sz = ax.legend(handles, labels, loc="lower right", title="Bill Length (mm)")
plt.tight_layout()

plt.show()
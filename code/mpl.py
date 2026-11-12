import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/victo/OneDrive/Documents/GitHub/a2-DataVis-5ways/penglings.csv").dropna(
    subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])

colors = {"Adelie": "orange", "Chinstrap": "purple", "Gentoo": "teal"}

fig, ax = plt.subplots()
for species, i in data.groupby("species"):
    ax.scatter(i["flipper_length_mm"], i["body_mass_g"], s=(i["bill_length_mm"]-25), 
               c=colors.get(species), alpha=0.8, label=species)
ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.legend(title="Species")
plt.tight_layout()

plt.show()
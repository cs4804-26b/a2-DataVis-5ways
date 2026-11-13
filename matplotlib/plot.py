import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the dataset
file_path = Path(__file__).resolve().parent.parent/"penglings.csv"
penguins = pd.read_csv(file_path, na_values=["NA"])

# Skip missing data 
penguins = penguins.dropna(subset=[
  "species", 
  "flipper_length_mm",
  "body_mass_g",
  "bill_length_mm"
])

# Pick colors for each species
species_colors = {
  "Adelie": "#E69F00",
  "Chinstrap": "#56B4E9",
  "Gentoo": "#009E73"
}

# Create the figure
fig, ax = plt.subplots(figsize=(9,6))

# Plot the penguins by species
for name, data in penguins.groupby("species"):
  ax.scatter(
    data["flipper_length_mm"],
    data["body_mass_g"],
    s=data["bill_length_mm"]*2,
    color=species_colors.get(name, "gray"),
    alpha=0.8,
    label=name
  )

# Add the labels
ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.set_title("Penguin Body Mass and Flipper Length")

# Adjust the axis limits
ax.set_xlim(165, 235)
ax.set_ylim(2500, 6500)

# Add grid and species legend
ax.grid(True, alpha=0.2)
species_legend = ax.legend(title="Species", loc = "upper left")
ax.add_artist(species_legend)

# Add bill Length Legend
bill_lengths = [35,45, 55]
size_handles = [
  ax.scatter([], [], s=length*2, color="gray", alpha=0.8)
  for length in bill_lengths
]
ax.legend(
  size_handles,
  [f"{length}" for length in bill_lengths],
  title="Bill Length (mm)",
  loc="lower right"
)

# Save and display the plot
plt.tight_layout()
plt.savefig(
  Path(__file__).resolve().parent/"matplotlib.png",
  dpi=300
)
plt.show

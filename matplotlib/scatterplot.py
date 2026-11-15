import csv 
from pathlib import Path

import matplotlib.pyplot as plt

csv_path = Path(__file__).resolve().parent.parent / "penglings.csv"

with csv_path.open(newline="") as file:
    penguins = [ row for row in csv.DictReader(file) if all(row[field] not in ("", "NA") for field in ("flipper_length_mm", "body_mass_g", "bill_length_mm"))]

flipper_lengths = [float(penguin["flipper_length_mm"]) for penguin in penguins]
body_masses = [float(penguin["body_mass_g"]) for penguin in penguins]

species_colors = {
    "Adelie": "#4b77a6",
    "Gentoo": "#f08a24",
    "Chinstrap": "#d95556",
}

colors = [species_colors[penguin["species"]] for penguin in penguins]

bill_lengths = [float(penguin["bill_length_mm"]) for penguin in penguins]
smallest_bill = min(bill_lengths)
largest_bill = max(bill_lengths)

def marker_area(bill):
    return 15 + 65 * (bill - smallest_bill) / (largest_bill - smallest_bill)

marker_areas = [marker_area(bill) for bill in bill_lengths]

plt.scatter(
    flipper_lengths,
    body_masses,
    c=colors,
    s=marker_areas,
    alpha=0.8,
    linewidths=0,
)

plt.xticks(range(170, 231, 10))
plt.yticks(range(3000, 6001, 1000))
plt.xlim(169, 234)
plt.ylim(2500, 6500)

plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body mass (g)")

plt.gca().set_axisbelow(True)
plt.grid(color="gray")

for species, color in species_colors.items():
    plt.scatter([], [], color=color, s=45, alpha=0.8, linewidths=0, label=species)

species_legend = plt.legend(title="Species", loc="upper left")
plt.gca().add_artist(species_legend)

size_samples = []
for bill in [40, 50]:
    sample = plt.scatter([], [], color="#555555", s=marker_area(bill), alpha=0.8, linewidths=0, label=str(bill))
    size_samples.append(sample)

plt.legend(handles=size_samples, title="Bill length (mm)", loc="lower right")

plt.show()

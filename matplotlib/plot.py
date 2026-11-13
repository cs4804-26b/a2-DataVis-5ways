
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "penglings.csv")

df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"\(.*?\)", "", regex=True)
    .str.strip("_")
)

required = [
    "species",
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm"
]


for col in required[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")


df = df.dropna(subset=required).copy()


colors = {
    "Adelie": "#F28E8E",
    "Chinstrap": "#65B8A6",
    "Gentoo": "#799CE8"
}


fig, ax = plt.subplots(figsize=(10, 6))

for species, group in df.groupby("species"):
    ax.scatter(
        group["flipper_length_mm"],
        group["body_mass_g"],
        s=group["bill_length_mm"] * 3,
        c=colors.get(species, "#999999"),
        alpha=0.8,
        label=species,
        edgecolors="white",
        linewidths=0.5
    )

ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
ax.set_title("Penguin Body Mass vs. Flipper Length")

ax.set_xlim(170, 240)
ax.set_ylim(2500, 6500)

ax.set_xticks(range(170, 241, 10))
ax.set_yticks(range(2500, 6501, 500))

ax.grid(alpha=0.2)
ax.set_axisbelow(True)


species_legend = ax.legend(
    title="Species",
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
    frameon=False
)


ax.add_artist(species_legend)


bill_lengths = [40, 50]

size_handles = [
    ax.scatter(
        [],
        [],
        s=length * 3,
        color="#555555",
        alpha=0.8,
        edgecolors="white",
        linewidths=0.5,
        label=f"{length} mm"
    )
    for length in bill_lengths
]

ax.legend(
    handles=size_handles,
    title="Bill Length (mm)",
    loc="upper left",
    bbox_to_anchor=(1.02, 0.65),
    frameon=False,
    labelspacing=1.5
)
fig.subplots_adjust(right=0.78)

output = ROOT / "img" / "matplotlib.png"
output.parent.mkdir(parents=True, exist_ok=True)

fig.savefig(
    output,
    dpi=200,
    bbox_inches="tight"
)

print(f"Matplotlib visualization saved to: {output}")

plt.show()

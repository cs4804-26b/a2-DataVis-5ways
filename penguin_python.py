import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load in the dataset
df = pd.read_csv("penglings.csv")
print(df.head())

# Define the species colors
palette = {
    "Adelie": "#FF8C00",
    "Chinstrap": "#A034F0",
    "Gentoo": "#159090"
}

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_facecolor("#E5E5E5")

# Draw the scatter plot
scatter = sns.scatterplot(
    data=df,
    x="flipper_length_mm", 
    y="body_mass_g",
    hue="species",
    size="bill_length_mm",
    sizes=(20, 200),
    palette=palette,
    alpha=0.7,
    edgecolor="none",
    ax=ax
)

# Apply the white lines drawn behind the points
ax.grid(True, color="white", linewidth=1.2)
ax.set_axisbelow(True)

# Remove the plot border
for spine in ax.spines.values():
    spine.set_visible(False)

# Labeling the axis
ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")

# move the legend outside the plot
sns.move_legend(ax, "upper left", bbox_to_anchor=(1.02, 1), frameon=False)

plt.tight_layout()
plt.show()
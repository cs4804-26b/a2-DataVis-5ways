library(ggplot2)
# Load dataset
penguins <- read.csv("penglings.csv")

# Remove the missing measurements
penguins <- penguins[
  complete.cases(
    penguins[, c("species", "bill_length_mm",
                 "flipper_length_mm", "body_mass_g")]
  ),
]

# Creates scatterplot
penguin_plot <- ggplot(
  penguins,
  aes(
    x = flipper_length_mm,
    y = body_mass_g,
    color = species,
    size = bill_length_mm
  )
) +
  # Add transparency to circles
  geom_point(alpha = 0.8) +

  # Set a different color for each species
  scale_color_manual(
    values = c(
      "Adelie" = "#E09719","Chinstrap" = "#B363C7","Gentoo" = "#27f5b4"
    )
  ) +

  # Change circles size
  scale_size_continuous(range = c(2, 8)) +

  # Set axis ranges
  coord_cartesian(
    xlim = c(170, 235),
    ylim = c(2500, 6500)
  ) +

  # Add labels/legend labels
  labs(
    title = "Penguin Flipper Length vs Body Mass",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  ) +

  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.title = element_text(size = 12),
    legend.position = "right"
  )
# Display plot
print(penguin_plot)

# Saves the visual
ggsave(
  "img/r-ggplot.png",
  plot = penguin_plot,
  width = 12,
  height = 7,
  dpi = 150
)
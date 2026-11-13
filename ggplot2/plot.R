# Load the library
library(ggplot2)

# Load the dataset
data <- read.csv("penglings.csv", na.strings = "NA")

# Remove missing values
data <- na.omit(data[, c(
  "species",
  "flipper_length_mm",
  "body_mass_g",
  "bill_length_mm"
  )])

# Pick colors for each species
colors <- c(
  "Adelie" = "#E69f00",
  "Chinstrap" = "#56B4E9",
  "Gentoo" = "#009E73"
)

# Create the scatterplot
plot <- ggplot(data, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  color = species,
  size = bill_length_mm
)) +
  geom_point(alpha = 0.8) + 
  scale_color_manual(values = colors) +
  scale_size_continuous(range = c(2,7)) +
  scale_x_continuous(limits = c(165, 235)) +
  scale_y_continuous(limits = c(2500, 6500)) +
  labs(
    title = "Penguin Body Mass and Flipper Length",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  ) +
 theme_minimal(base_size = 13) +
 theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    panel.grid.minor = element_blank(),
    legend.position = "right"
   )

# Display the chart
print(plot)

# Save the chart
ggsave(
  "ggplot2/ggplot2.png",
  plot = plot,
  width = 10,
  height = 6,
  dpi = 150
)
  



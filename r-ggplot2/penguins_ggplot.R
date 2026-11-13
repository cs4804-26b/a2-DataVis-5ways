
# Penguin scatterplot using ggplot2

library(ggplot2)

# Load  dataset
penguins <- read.csv("penglings.csv")

# Remove rows with missing measurements
penguins <- penguins[
  complete.cases(penguins[, c(
    "flipper_length_mm",
    "body_mass_g",
    "bill_length_mm",
    "species"
  )]),
]

# Create  scatterplot
chart <- ggplot(
  penguins,
  aes(
    x = flipper_length_mm,
    y = body_mass_g,
    color = species
  )
) +

  # Plot penguins, sized by bill length
  geom_point(
    aes(size = bill_length_mm),
    alpha = 0.8
  ) +

  # Adelie regression line - dark teal
  geom_smooth(
    data = subset(penguins, species == "Adelie"),
    aes(
      x = flipper_length_mm,
      y = body_mass_g,
      linetype = "Adelie"
    ),
    inherit.aes = FALSE,
    method = "lm",
    formula = y ~ x,
    se = FALSE,
    color = "#06454D",
    linewidth = 1.1
  ) +

  # Gentoo regression line - deep navy
  geom_smooth(
    data = subset(penguins, species == "Gentoo"),
    aes(
      x = flipper_length_mm,
      y = body_mass_g,
      linetype = "Gentoo"
    ),
    inherit.aes = FALSE,
    method = "lm",
    formula = y ~ x,
    se = FALSE,
    color = "#173B78",
    linewidth = 1.1
  ) +

  # Chinstrap regression line - dark orange
  geom_smooth(
    data = subset(penguins, species == "Chinstrap"),
    aes(
      x = flipper_length_mm,
      y = body_mass_g,
      linetype = "Chinstrap"
    ),
    inherit.aes = FALSE,
    method = "lm",
    formula = y ~ x,
    se = FALSE,
    color = "#984600",
    linewidth = 1.1
  ) +

  # Species colors
  scale_color_manual(
    values = c(
      "Adelie" = "#177E89",
      "Gentoo" = "#59A5D8",
      "Chinstrap" = "#E8A44D"
    ),
    breaks = c("Adelie", "Gentoo", "Chinstrap")
  ) +

  # Bill length legend
  scale_size_continuous(
    breaks = c(35, 40, 45, 50, 55),
    range = c(1.5, 4.5)
  ) +

  # Trendline legend
  scale_linetype_manual(
    name = "Trendlines",
    values = c(
      "Adelie" = "dashed",
      "Gentoo" = "dashed",
      "Chinstrap" = "dashed"
    ),
    breaks = c("Adelie", "Gentoo", "Chinstrap"),
    guide = guide_legend(
      order = 2,
      override.aes = list(
        color = c("#06454D", "#173B78", "#984600"),
        linewidth = 1.1
      )
    )
  ) +

  # Axis ranges and ticks
  scale_x_continuous(
    breaks = seq(170, 230, 10)
  ) +

  scale_y_continuous(
    breaks = seq(2500, 6500, 500),
    labels = scales::comma
  ) +

  coord_cartesian(
    xlim = c(170, 235),
    ylim = c(2500, 6500)
  ) +

  # Titles and labels
  labs(
    title = "Penguin Body Mass vs. Flipper Length",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  ) +

  # Organize legend order
  guides(
    color = guide_legend(order = 1),
    size = guide_legend(order = 3)
  ) +

  # Chart styling
  theme_minimal(base_size = 13) +

  theme(
    plot.background = element_rect(
      fill = "white", color = NA
    ),
    panel.background = element_rect(
      fill = "white", color = NA
    ),
    legend.background = element_rect(
      fill = "white", color = NA
    ),

    # Subtle gridlines
    panel.grid.major = element_line(
      color = "#E5E7EB",
      linewidth = 0.4
    ),
    panel.grid.minor = element_blank(),

    # Centered title
    plot.title = element_text(
      hjust = 0.5,
      face = "bold",
      size = 16,
      color = "#263238"
    ),

    axis.title = element_text(
      color = "#263238"
    ),
    axis.text = element_text(
      color = "#475569"
    ),

    legend.title = element_text(
      face = "bold",
      color = "#263238"
    ),
    legend.text = element_text(
      color = "#475569"
    ),

    plot.margin = margin(20, 20, 20, 20)
  )

ggsave(
  "img/ggplot2.png",
  plot = chart,
  width = 10,
  height = 6,
  dpi = 150,
  bg = "white"
)

print("ggplot2 chart created!")

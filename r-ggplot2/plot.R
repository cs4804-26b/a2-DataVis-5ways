library(ggplot2)
library(plotly)
library(htmlwidgets)


# Load the penguin dataset
penguins <- read.csv("../penglings.csv", na.strings = "NA")

# Remove rows missing measurements needed for the chart
needed <- c("flipper_length_mm", "body_mass_g", "bill_length_mm")
penguins <- penguins[complete.cases(penguins[, needed]), ]

# Keep the species in a consistent order
penguins$species <- factor(
  penguins$species,
  levels = c("Adelie", "Chinstrap", "Gentoo")
)

# Check the data
print(nrow(penguins))
print(table(penguins$species))



# Create the scatterplot
p <- ggplot(penguins, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  color = species,
  size = bill_length_mm
)) +
  geom_point(alpha = 0.8
             ) +
  
  # Use same species colors
  scale_color_manual(values = c(
    "Adelie" = "#FF8C00",
    "Chinstrap" = "#A536D2",
    "Gentoo" = "#008B8B"
  )) +
  
  # Set how bill length controls circle size
  scale_size_continuous(
    range = c(1.5, 6),
    breaks = c(40, 50)
  ) +
  
  # Configure the axis ticks
  scale_x_continuous(
    breaks = seq(170, 230, 10)
  ) +
  
  scale_y_continuous(
    breaks = seq(3000, 6000, 1000)
  ) +
  
  # Match the original visible axis ranges
  coord_cartesian(
    xlim = c(169, 234),
    ylim = c(2500, 6500),
    expand = FALSE
  ) +
  
  # Add readable axis and legend labels
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    color = "Species",
    size = "Bill Length (mm)"
  ) +
  
  # Use a gray theme like the reference
  theme_gray(base_size = 13, base_family = "sans") +
  
  # Improve font and background styling
  theme(
    panel.background = element_rect(
      fill = "#EBEBEB",
      color = NA
    ),
    
    panel.grid.major = element_line(
      color = "white",
      linewidth = 0.7
    ),
    
    panel.grid.minor = element_line(
      color = "white",
      linewidth = 0.3
    ),
    
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 11),
    
    legend.title = element_text(size = 12),
    legend.text = element_text(size = 11),
    legend.position = "right"
  )

# Display the finished chart
print(p)

# Save the main visualization
ggsave(
  "../img/r.png",
  plot = p,
  width = 10,
  height = 6.2,
  dpi = 160,
  bg = "white"
)

print("Saved r.png")


# Add detailed information for the interactive version
interactive_source <- p + aes(
  text = paste0(
    "Species: ", species,
    "<br>Flipper Length: ", flipper_length_mm, " mm",
    "<br>Body Mass: ", body_mass_g, " g",
    "<br>Bill Length: ", bill_length_mm, " mm",
    "<br>Island: ", island,
    "<br>Year: ", year
  )
)

# Convert the ggplot into an interactive Plotly chart
interactive_plot <- ggplotly(
  interactive_source,
  tooltip = "text"
)

# Display it
print(interactive_plot)


# Save the interactive visualization as an HTML page
saveWidget(
  interactive_plot,
  file = "penguins-interactive.html",
  selfcontained = FALSE
)

print("Saved interactive HTML")


# Make a second plot with trend lines for each species
trend_plot <- p +
  geom_smooth(
    data = penguins,
    aes(
      x = flipper_length_mm,
      y = body_mass_g,
      color = species
    ),
    inherit.aes = FALSE,
    method = "lm",
    se = FALSE,
    linewidth = 0.8,
    show.legend = FALSE
  ) +
  labs(
    title = "Penguin Measurements by Species",
    subtitle = "Lines show the fitted trend for each species",
    caption = paste(nrow(penguins), "penguins with complete measurements")
  ) +
  theme(
    plot.title = element_text(size = 17, face = "bold"),
    plot.subtitle = element_text(size = 11),
    plot.caption = element_text(size = 10)
  )

# Display the enhanced plot
print(trend_plot)

# Save it as a second image
ggsave(
  "../img/r-trends.png",
  plot = trend_plot,
  width = 10,
  height = 6.2,
  dpi = 160,
  bg = "white"
)



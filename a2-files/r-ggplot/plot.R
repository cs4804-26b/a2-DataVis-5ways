# Penguin scatterplot in R + ggplot2
# Run from the repo root:  Rscript r-ggplot/plot.R
library(ggplot2)

penguins <- read.csv("penglings.csv", na.strings = "NA")

# Drop rows missing any of the values we plot
penguins <- subset(penguins,
  !is.na(flipper_length_mm) & !is.na(body_mass_g) & !is.na(bill_length_mm))

species_colors <- c(Adelie = "#FF8C00", Chinstrap = "#A034F0", Gentoo = "#159090")

p <- ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g,
                          color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = species_colors) +
  scale_size(range = c(1, 6), breaks = c(40, 50)) +
  scale_x_continuous(breaks = seq(170, 230, 10)) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)",
       color = "species", size = "bill_length_mm") +
  guides(color = guide_legend(order = 2, override.aes = list(size = 3)),
         size = guide_legend(order = 1))

ggsave("img/ggplot2.png", p, width = 8, height = 5, dpi = 150)

#install.packages("ggplot2")

library("ggplot2")

pengling <- read.csv("penglings.csv", na.strings = c("NA", ""))

pengling <- pengling[complete.cases(pengling[c(
  "flipper_length_mm", "body_mass_g", "bill_length_mm", "species"
)]), ]

ggplot(pengling, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
    geom_point(alpha = 0.8) +
    scale_color_manual(values = c("Adelie" = "#ff8c00", "Chinstrap" = "#a52bd4", "Gentoo" = "#008b8b")) +
    scale_size_continuous(range = c(2, 6)) +
    scale_x_continuous(breaks = seq(170, 230, 10)) +
    scale_y_continuous(breaks = seq(3000, 6000, 1000)) +
    coord_cartesian(
        xlim = c(169, 234),
        ylim = c(2500, 6500),
        expand = FALSE
    ) +
    labs(
        x = "Flipper Length (mm)",
        y = "Body Mass (g)",
        color = "Species",
        size = "Bill Length (mm)"
    ) +
    theme_gray(base_size = 14)


    ggsave("ggplot-penguins.png", width = 9, height = 6, dpi = 300)
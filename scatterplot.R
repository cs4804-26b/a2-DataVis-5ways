library(ggplot2) #ggplot2

#import data from csv file
penglingData <- read.csv("penglings.csv")

#custom colors
custom_colors <- c("Adelie" = "#fa9037", "Chinstrap" = "#9a3dca", "Gentoo" = "#378e8d")

#make scatterplot
plot <- ggplot(penglingData, aes(x= flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
    geom_point(alpha= 0.8) + scale_color_manual(values = custom_colors)
    labs (
        x = "Flipper Length (mm)",
        y = "Body Mass (g)"
    ) +
    theme_minimal()

print(plot)


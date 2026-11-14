library(ggplot2)

# read data
data <- read.csv("penglings.csv")

# plot
plot <- ggplot(data, aes(x = flipper_length_mm, y = body_mass_g, size = bill_length_mm, color = species)) +
          geom_point(alpha = 0.8) +
          scale_color_manual(values = c(Adelie = "#fa9037", Chinstrap = "#9a3dca", Gentoo = "#3c9190")) +
          labs(x = "Flipper Length (mm)", y = "Body Mass (g)") +
          guides(size = guide_legend(order = 1), color = guide_legend(order = 2))

ggsave("img/r-ggplot2.png", plot, width = 7, height = 4.5, dpi = 200)



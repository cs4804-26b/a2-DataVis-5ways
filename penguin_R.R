library(ggplot2)

df <- read.csv("penglings.csv")
print(head(df))

ggplot(df, aes(x = flipper_length_mm, y = body_mass_g,
               color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = c("Adelie"    = "darkorange",
                                "Chinstrap" = "darkorchid",
                                "Gentoo"    = "#008080")) +
  scale_size_continuous(range = c(1, 6), breaks = c(40, 50)) +
  guides(size  = guide_legend(order = 1),
         color = guide_legend(order = 2)) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)") +
  theme_gray()
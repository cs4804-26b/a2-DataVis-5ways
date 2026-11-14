library(ggplot2)
library(readr)
pengdata <- read_csv("Kamala's_files/penglings.csv")
ggplot(data = pengdata, aes(x = flipper_length_mm, y = body_mass_g, size = bill_length_mm, col = species)) +
  scale_color_manual(values = c("orange", "purple", "darkcyan")) +
  geom_point(alpha= 0.8) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)")






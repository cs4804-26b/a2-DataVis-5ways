library(ggplot2)

dataframe <- read.csv("../penglings.csv")

ggplot(dataframe, aes(
  x = flipper_length_mm,
  y = body_mass_g,
  size = bill_length_mm,
  color = species
)) +
  geom_point(alpha = 0.7) +
  labs(
    title = "Penglings",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    size = "Bill Length (mm)",
    color = "Species"
  )



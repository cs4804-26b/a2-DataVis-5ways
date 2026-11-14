library(ggplot2)
data <- read.csv(file.choose(), na.strings = c("NA", ""))
data -> data[complete.cases(data[, c(
  "flipper_length_mm", "body_mass_g", "bill_length_mm"
)]), ]
chart <- ggplot(data, aes(
  x = flipper_length_mm, 
  y = body_mass_g, 
  color = species, 
  size = bill_length_mm
)) +
  geom_point(alpha = 0.8) +
  scale_color_manual(values = c(
    "Adelie" = "#e76f51", "Chinstrap" ="#8b6bb1", "Gentoo" ="#2a9d87"
  )) +
  scale_size_area(max_size = 10) +
  labs(
    title = "penguin flipper length and mass", 
    x= "flipper length mm",
    y ="body mass g", 
    color ="species", 
    size = "bill length mm"
  ) +
  theme_minimal(base_size = 13)
print(chart)
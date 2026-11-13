library(ggplot2)
library(hrbrthemes)


df <- read.csv("penglings.csv")
df_clean <- na.omit(df) # to remove null values

# Transparency
ggplot(df_clean, aes(x=flipper_length_mm, y=body_mass_g)) +
  geom_point(aes(size=bill_length_mm, color=species), alpha = 0.8) +
  scale_color_manual(values = c(
    "Adelie"    = "#01a2b0",
    "Gentoo"    = "#c62423",
    "Chinstrap" = "#ff818a"
  )) +
  labs(
    x = "Flipper Length (mm)",
    y = "Body Mass (g)",
    title = "Flipper Length vs. Body Mass",
    size = "Bill Length (mm)",
    color = "Species",
  )
  theme_ipsum()
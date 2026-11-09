#load ggplot2
if (!require(ggplot2)) {
  install.packages("ggplot2")
}

#load libraries
if (!require (dplyr)) install.packages("dplyr")
if (!require (tidyr)) install.packages("tidyr")

library(ggplot2)
library(dplyr)
library(tidyr)

#loading and cleaning data
data <- read.csv("C:/Users/madis/Data Vis/a2-DataVis-5ways/penglings.csv", stringsAsFactors = FALSE, header=TRUE)
data <- data %>% drop_na()

ggplot(data = data)
ggplot(data, mapping = aes(x=flipper_length_mm, y=body_mass_g))

#color mapping
ggplot(data, aes(flipper_length_mm, body_mass_g, size = bill_length_mm, color = species)) +
  geom_point(alpha = 0.7) +
  scale_color_manual(values = c("Adelie"= "#ff941f",
                                "Chinstrap"= "#a83dcc",
                                "Gentoo"= "#159995")) +
  scale_size_continuous(breaks = c(40,50), range = c(1, 6)) +
  guides( #ordering size/species in legend
    size = guide_legend(order =1),
    color = guide_legend(order = 2)
  ) +
  labs ( #renaming axes
    x = "Flipper Length (mm)",
    y = "Body Mass (g)"
  )+
  theme_gray() + #setting background to gray
  theme(
    legend.position = "right"
  )


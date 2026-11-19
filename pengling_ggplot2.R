library(ggplot2)
library(dplyr)

data <- read.csv(file = "C:\\Users\\allys\\Documents\\Pengling project\\penglings.csv")

data %>%
  arrange(desc(bill_length_mm)) %>%
  ggplot(aes(x=flipper_length_mm, y=body_mass_g, size=bill_length_mm, color=species)) +
    geom_point(alpha=0.8) +
    scale_color_manual(values=c("#ff8e08","#9933cc","#158f8f")) +
    scale_size(range = c(1, 10), name="bill_length_mm") +
    labs(x = "Flipper Length (mm)") +
    labs(y = "Body Mass (g)")

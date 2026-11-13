# used ggplot2 v4.0.3's reference docs 
install.packages("ggplot2")
install.packages("dplyr")

library(ggplot2)
library(dplyr)

data <- read.csv("C:/Users/victo/OneDrive/Documents/GitHub/a2-DataVis-5ways/penglings.csv") %>% 
    filter(!is.na(flipper_length_mm), !is.na(body_mass_g), !is.na(bill_length_mm))

chart <- ggplot(data, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
    geom_point(alpha = 0.8) +
    scale_color_manual(values = c("Adelie"="orange", "Chinstrap"="purple", "Gentoo"="cyan4")) + 
    labs(x = "Flipper Length (mm)", y = "Body Mass (g)", color = "Species", size = "Bill Length (mm)")

print(chart)
ggsave("R_ggplot2-vis.png", chart, width=9, height=6)
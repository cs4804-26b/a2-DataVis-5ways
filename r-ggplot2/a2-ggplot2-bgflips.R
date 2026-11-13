#install.packages("ggplot2")
#setwd("C:/WPI Stuff/courses/2026-2027/B26/CS 4804 Data Visualization/a2 cs4804/a2-bgflips-benjamin-glaser-main")

library(ggplot2)
peng <- read.csv("penglings.csv", na.strings = "NA")

peng.clean <- subset(peng,!is.na(bill_length_mm)	&	
                       !is.na(bill_depth_mm)	&	
                       !is.na(flipper_length_mm)	& 
                       !is.na(body_mass_g))


p <- ggplot(data = peng.clean,
            aes(
              x = flipper_length_mm,
              y = body_mass_g,
              color = species,
              size = bill_length_mm
            )) +
  geom_point(alpha = 0.8) +
  scale_colour_manual(
    values = c(
      "Adelie" = "darkorange",
      "Chinstrap" = "darkorchid",
      "Gentoo" = "cyan4"
  )) +
  guides(
    size = guide_legend(order = 1),
    color = guide_legend(order = 2)
  )

print(p)

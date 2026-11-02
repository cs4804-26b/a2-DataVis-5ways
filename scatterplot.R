library(ggplot2) #ggplot2

#import data from csv file
penglingData <- read.csv("penglings.csv")

#make scatterplot
plot <- ggplot(penglingData, aes(x= flipper_length_mm, y = body_mass_g)) +
    geom_point(size=3,color="blue",alpha= 0.8) +
    labs (
        x = "Flipper Length (mm)",
        y = "Body Mass (g)"
    ) +
    theme_minimal()

print(plot)


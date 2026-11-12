#file to be run from main a2-kjhitt-keagan-hitt directory, not R directory

packages <- c("ggplot2", "svglite")

for (package in packages) { #install dependencies if not installed
    if (!requireNamespace(package, quietly = TRUE)) {
        install.packages(package, repos = "https://cloud.r-project.org")
    }
}

library(ggplot2)
library(svglite)

penglings <- read.csv("penglings.csv")

ggplot(penglings, aes(x=flipper_length_mm, y=body_mass_g, size=bill_length_mm, color=species)) +
    geom_point(alpha = 0.8) + #opacity
    #annoying linear scaling of radius
    scale_radius(range = c(min(penglings$bill_length_mm, na.rm = TRUE) * 0.083, max(penglings$bill_length_mm, na.rm = TRUE) * 0.083)) +
    scale_color_manual( #colors!
        values = c("Adelie" = "#fc992f", "Chinstrap" = "#9f3fce", "Gentoo" = "#219292")
    ) + 
    labs(x = "Flipper Length (mm)", y = "Body Mass (g)") +  # axis labels
    theme( #text size was too big
        axis.title = element_text(size = 8),
        axis.text = element_text(size = 6),
        legend.title = element_text(size = 8),
        legend.text = element_text(size = 7)
    ) + 
    guides( #swapping the order in the legend
        size = guide_legend(order = 1),
        color = guide_legend(order = 2)
    ) 


ggsave("img/r.png", width=1700, height=1050, units="px")
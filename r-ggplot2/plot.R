library(ggplot2)

data <- read.csv(
    "../penglings.csv",
    na.strings = c("NA", "")
)

data <- data[
    complete.cases(data[, c(
        "species",
        "bill_length_mm",
        "flipper_length_mm",
        "body_mass_g"
    )]),
]

chart <- ggplot(
    data,
    aes(
        x = flipper_length_mm,
        y = body_mass_g,
        color = species,
        size = bill_length_mm
    )
) +
    geom_point(alpha = 0.8) +
    scale_color_manual(
        values = c(
            Adelie = "#F28E2B",
            Chinstrap = "#9B5DE5",
            Gentoo = "#59A14F"
        )
    ) +
    scale_size_continuous(
        name = "Bill Length (mm)",
        range = c(2, 7)
    ) +
    coord_cartesian(
        xlim = c(170, 235),
        ylim = c(2500, 6500)
    ) +
    labs(
        title = "Penguin Body Mass vs. Flipper Length",
        x = "Flipper Length (mm)",
        y = "Body Mass (g)",
        color = "Species"
    ) +
    theme_minimal()

ggsave(
    "r-ggplot2_screenshot.png",
    plot = chart,
    width = 9,
    height = 6,
    dpi = 150
)

print(chart)

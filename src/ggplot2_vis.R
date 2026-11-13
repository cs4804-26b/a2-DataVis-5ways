
library(ggplot2)

penguin_data <- read.csv("./penglings.csv")

# Remove rows with missing values
penguin_data <- penguin_data[complete.cases(
    penguin_data[, c("flipper_length_mm", "body_mass_g", "bill_length_mm", "species")]
), ]

species_colors <- c(
    "Adelie" = "#e11d48",
    "Chinstrap" = "#ecb425",
    "Gentoo" = "#2563EB"
)

p <- ggplot(
    penguin_data,
    aes(
        x = flipper_length_mm,
        y = body_mass_g,
        size = bill_length_mm,
        fill = species
    )
) +
    # Filled density regions
    geom_density_2d_filled(
        data = subset(penguin_data, species == "Adelie"),
        aes(x = flipper_length_mm, y = body_mass_g),
        fill = "#e11d48",
        alpha = 0.12,
        contour_var = "ndensity",
        breaks = c(0.15, 0.3, 0.5, 0.7, 0.85, 1.01),
        show.legend = FALSE,
        inherit.aes = FALSE
    ) +
    geom_density_2d_filled(
        data = subset(penguin_data, species == "Chinstrap"),
        aes(x = flipper_length_mm, y = body_mass_g),
        fill = "#ecb425",
        alpha = 0.12,
        contour_var = "ndensity",
        breaks = c(0.15, 0.3, 0.5, 0.7, 0.85, 1.01),
        show.legend = FALSE,
        inherit.aes = FALSE
    ) +
    geom_density_2d_filled(
        data = subset(penguin_data, species == "Gentoo"),
        aes(x = flipper_length_mm, y = body_mass_g),
        fill = "#2563EB",
        alpha = 0.12,
        contour_var = "ndensity",
        breaks = c(0.15, 0.3, 0.5, 0.7, 0.85, 1.01),
        show.legend = FALSE,
        inherit.aes = FALSE
    ) +
    # Subtle outlines around density regions
    geom_density_2d(
        data = penguin_data,
        aes(
            x = flipper_length_mm,
            y = body_mass_g,
            color = species
        ),
        contour_var = "ndensity",
        breaks = c(0.15, 0.3, 0.5, 0.7),
        linewidth = 0.35,
        alpha = 0.35,
        show.legend = FALSE,
        inherit.aes = FALSE
    ) +
    # Individual penguin observations
    geom_point(
        aes(fill = species),
        shape = 21,
        color = "#333333",
        stroke = 0.5,
        alpha = 0.8
    ) +
        scale_fill_manual(
        values = species_colors,
        name = "Species",
        guide = guide_legend(
            order = 1,
            override.aes = list(
                shape = 21,
                color = "#333333",
                size = 5,
                alpha = 1,
                stroke = 0.5
            )
        )
    ) +
    scale_color_manual(
        values = species_colors,
        guide = "none"
    ) +
    scale_size_continuous(
        name = "Bill Length (mm)",
        range = c(2.5, 7),
        breaks = c(30, 35, 40, 45, 50, 55, 60),
        guide = guide_legend(
            order = 2,
            override.aes = list(
                shape = 21,
                fill = "#888888",
                color = "#333333",
                alpha = 0.8,
                stroke = 0.5
            )
        )
    ) +
    labs(
        title = "Penguin Measurements",
        subtitle = "Density regions highlight areas of concentration across three penguin species.",
        x = "Flipper Length (mm)",
        y = "Body Mass (g)"
    ) +
    theme_minimal(base_family = "sans") +
    theme(
        aspect.ratio = 1 / 1.5,
        plot.background = element_rect(
            fill = "#F7F7F2",
            color = NA
        ),
        panel.background = element_rect(
            fill = "#F7F7F2",
            color = NA
        ),
        panel.grid.major = element_line(
            color = "#DDDDDD",
            linewidth = 0.4
        ),
        panel.grid.minor = element_blank(),
        plot.title = element_text(
            size = 20,
            face = "bold",
            color = "#222222",
            hjust = 0.5
        ),
        plot.subtitle = element_text(
            size = 13,
            color = "#555555",
            hjust = 0.5
        ),
        axis.title = element_text(
            size = 13,
            color = "#222222"
        ),
        axis.text = element_text(
            size = 11,
            color = "#222222"
        ),
        legend.title = element_text(
            size = 12,
            face = "bold",
            color = "#222222"
        ),
        legend.text = element_text(
            size = 11,
            color = "#222222"
        ),
        legend.key.size = unit(0.8, "cm"),
        legend.spacing.y = unit(0.2, "cm"),
        legend.position = "right"
    )

print(p)

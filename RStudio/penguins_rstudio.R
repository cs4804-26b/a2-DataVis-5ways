# Recreate the penguins scatterplot in R with ggplot2
script_path <- function() {
  file_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
  if (length(file_arg) > 0) {
    return(normalizePath(sub("^--file=", "", file_arg[[1]])))
  }
  ofile <- tryCatch(sys.frame(1)$ofile, error = function(e) NULL)
  if (!is.null(ofile)) {
    return(normalizePath(ofile))
  }
  file.path(getwd(), "penguins_rstudio.R")
}

HERE <- dirname(script_path())
CSV <- file.path(HERE, "..", "penglings.csv")
PNG <- file.path(HERE, "penguins_rstudio.png")
README_PNG <- file.path(HERE, "..", "img", "rstudio.png")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("ggplot2 is required. Run install.packages('ggplot2') first.")
}

SPECIES <- c("Adelie", "Chinstrap", "Gentoo")
SPECIES_COLORS <- c(
  "Adelie" = "#F2A03D",
  "Chinstrap" = "#8E44AD",
  "Gentoo" = "#2A7F7F"
)

# Load and clean observations
penguins <- read.csv(CSV, na.strings = c("NA", ""), check.names = FALSE)
penguins <- penguins[complete.cases(
  penguins[, c("bill_length_mm", "flipper_length_mm", "body_mass_g")]
), ]
penguins$species <- factor(penguins$species, levels = SPECIES)

chart <- ggplot2::ggplot(
  penguins,
  ggplot2::aes(
    x = flipper_length_mm,
    y = body_mass_g,
    colour = species,
    size = bill_length_mm
  )
) +
  ggplot2::geom_point(alpha = 0.8, stroke = 0) +
  ggplot2::scale_colour_manual(
    name = "species",
    values = SPECIES_COLORS,
    limits = SPECIES,
    drop = FALSE
  ) +
  ggplot2::scale_size_continuous(
    name = "bill_length_mm",
    range = c(1.5, 8),
    breaks = c(40, 50)
  ) +
  ggplot2::scale_x_continuous(
    name = "Flipper Length (mm)",
    limits = c(168, 234),
    breaks = seq(170, 230, by = 10),
    expand = c(0, 0)
  ) +
  ggplot2::scale_y_continuous(
    name = "Body Mass (g)",
    limits = c(2700, 6300),
    breaks = seq(3000, 6000, by = 1000),
    # Keeps the largest and smallest circles from being clipped by edge
    expand = ggplot2::expansion(mult = 0.02)
  ) +
  ggplot2::labs(
    title = "Penguin body mass vs. flipper length",
    subtitle = sprintf(
      "Colour = species, size = bill length; %d complete observations",
      nrow(penguins)
    )
  ) +
  ggplot2::guides(
    size = ggplot2::guide_legend(order = 1),
    colour = ggplot2::guide_legend(order = 2, override.aes = list(size = 3))
  ) +
  ggplot2::theme_minimal(base_size = 13) +
  ggplot2::theme(
    plot.background = ggplot2::element_rect(fill = "white", colour = NA),
    panel.background = ggplot2::element_rect(fill = "#F5F5F5", colour = NA),
    panel.grid.major = ggplot2::element_line(colour = "white", linewidth = 0.9),
    panel.grid.minor = ggplot2::element_blank(),
    axis.text = ggplot2::element_text(colour = "#333333", size = 11),
    axis.title = ggplot2::element_text(colour = "#111111", face = "bold",
                                       size = 13),
    axis.title.x = ggplot2::element_text(margin = ggplot2::margin(t = 8)),
    axis.title.y = ggplot2::element_text(margin = ggplot2::margin(r = 8)),
    plot.title = ggplot2::element_text(colour = "#111111", face = "bold",
                                       size = 15, hjust = 0),
    plot.subtitle = ggplot2::element_text(colour = "#555555", size = 10,
                                          hjust = 0, margin =
                                            ggplot2::margin(b = 10)),
    legend.position = "right",
    legend.title = ggplot2::element_text(colour = "#111111", size = 11),
    legend.text = ggplot2::element_text(colour = "#333333", size = 10),
    legend.key = ggplot2::element_rect(fill = "#F5F5F5", colour = NA),
    legend.background = ggplot2::element_rect(fill = "white", colour = NA),
    legend.margin = ggplot2::margin(l = 12),
    plot.margin = ggplot2::margin(16, 20, 12, 12)
  )

# Keep text sharp and produce a high-resolution PNG
png_device <- if (requireNamespace("ragg", quietly = TRUE)) ragg::agg_png else "png"

ggplot2::ggsave(
  PNG,
  plot = chart,
  width = 8.5,
  height = 5.5,
  dpi = 200,
  units = "in",
  bg = "white",
  device = png_device
)
invisible(file.copy(PNG, README_PNG, overwrite = TRUE))

cat(nrow(penguins), "observations plotted\n")
cat("wrote", normalizePath(PNG), "\n")
cat("wrote", normalizePath(README_PNG), "\n")


library(ggplot2)
library(plotly)
library(dplyr)
library(htmlwidgets)

data <- read.csv("penglings.csv")

# Convert columns to numeric
numeric_columns <- c(
  "bill_length_mm",
  "flipper_length_mm",
  "body_mass_g"
)

data[numeric_columns] <- lapply(
  data[numeric_columns],
  as.numeric
)
# build the hoverable interaction 
chart <- ggplot(
  data,
  aes(
    x = flipper_length_mm,
    y = body_mass_g,
    color = species,
    size = bill_length_mm,
    text = paste0(
      "Species: ", species,
      "<br>Island: ", island,
      "<br>Flipper Length: ", flipper_length_mm, " mm",
      "<br>Body Mass: ", body_mass_g, " g",
      "<br>Bill Length: ", bill_length_mm, " mm"
    )
  )
) +

  geom_point(alpha = 0.6) +

  scale_color_manual(
    name = "Penguin Species",
    values = c(
      "Adelie" = "#F56C27",
      "Chinstrap" = "#88219E",
      "Gentoo" = "#685CE0"
    ),
    drop = FALSE
  ) +

  scale_size_continuous(
    name = "Bill Length (mm)",
    range = c(2, 15)
  ) +

  scale_x_continuous(
    name = "Flipper Length (mm)",
    limits = c(160, 240),
    breaks = seq(170, 230, 10),
    expand = expansion(mult = 0)
  ) +

  scale_y_continuous(
    name = "Body Mass (g)",
    limits = c(2500, 6500),
    breaks = seq(3000, 6000, 500),
    expand = expansion(mult = 0)
  ) +

  labs(
    title = "Penguin Body Mass vs. Flipper Length"
  ) +

  theme_minimal() +

  theme(
    plot.title = element_text(size = 24, hjust = 0.5),
    axis.title = element_text(size = 20),
    axis.text = element_text(size = 16),
    legend.title = element_text(size = 20),
    legend.text = element_text(size = 16),
    legend.position = "right",
    panel.grid.major = element_line(),
    panel.border = element_blank()
  )

interactive_chart <- ggplotly(
  chart,
  tooltip = "text",
  width = 1200,
  height = 800
) %>% # pipe in the interactive legend
  layout(
    legend = list(
      title = list(text = "Penguin Species"),
      font = list(size = 16),
      itemclick = "toggle",
      itemdoubleclick = "toggleothers"
    )
  )

saveWidget(
  interactive_chart,
  "penguin_scatterplot_R.html",
  selfcontained = FALSE
)

interactive_chart
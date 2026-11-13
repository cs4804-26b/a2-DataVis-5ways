options(repos = c(CRAN = "https://cran.rstudio.com"))

# Install and load packages
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)

# Read the penglings dataset into a data frame
dataframe <- read.csv("penglings.csv")
df <- na.omit(dataframe)  # Remove rows with missing values
str(df)

p <-ggplot(df, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.7) +
  scale_color_manual(values = c("Adelie" = "blue", "Chinstrap" = "red", "Gentoo" = "green")) +
  labs(title = "Penguin Flipper Length vs Body Mass",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)")

ggsave("ggplot2_Penguin_Plot.png", plot = p, path = "./Plots", width = 8, height = 6, dpi = 300)
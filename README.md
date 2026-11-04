Assignment 2 - Data Visualization, 5 Ways  
===

# d3

This was on the more difficult side just because I'm not experienced with d3.js and Javascript as a whole, and I had to look up a lot of examples.
The main requirements of the scatterplot were met.

![Scatterplot made with d3.js](img/d3.js_plot.png)

To visualize the penguins dataset, I had to extract each needed element from the .csv file with the d3.csv function, and create a conditional statement for rows that return null. I then had to specify elements such as margins, dimensions, the radius scale, the color scale. I also appended SVGs for the axes, data points, and labels.

Generally I found the process of working with d3.js tedious. While it seems to provide more freedom in how to display the scatterplot, I felt a lot of things had to be done manually. 

# R + ggplot2

![Scatterplot made with ggplot2](img/ggplot2.png)
With R and ggplot2, I used geom_point to create visualize the data with a scatterplot, and aes() to map visual properties to the points. I also created a vector with custom colors that correspond to each species.

Personally, I found R and ggplot2 the most convenient method so far.


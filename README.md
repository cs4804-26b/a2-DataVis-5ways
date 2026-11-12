# d3 + JavaScript
d3 is a free JavaScript library used to create data visualizations in web browsers. To create the penguin visualization, I created a plot svg and added the necessary elements, such as axes titles/labels, legends, color mapping, size mapping, to it. 

While d3.js gives you a lot of control over individual elements of the graph, it requires many lines of code and location specifications.  

For this graph, the font differs from the reference graph.

<img src="img/d3_plot.png" alt="D3 plot" width="600">  

<br>

# R + ggplot2
ggplot2 is a free R package used to create visualizations that allows you to build graphs step-by-step using data, aesthetic mappings (aes), and geoms (geometric objects). 

I found that this library was much easier to use than d3.js because the ggplot function allows you to add chart elements all at once, instead of building upon an svg. This software was also the same one used to create the reference plot given, which is why it was easy to match the required elements. Specifically, adding the gray background to the chart and legend was simpler than other software because it was a built-in theme that could be set, whereas in other software it had to be manually built by creating rectangles. 

I also used R packages (tidyr and dplyr) to clean the csv data and remove NA values. 

<img src="img/r_ggplot.png" alt="R + ggplot2 plot" width="600">

<br>

# Vega-Lite

Vega-Lite uses JSON specifications to create data visualizations. It is similar to R's ggplot2 because both are declarative and based on the grammar of graphics. Data fields are mapped to physical properties. The code is created in an .html file and rendered as a webpage. 

I thought that writing this code was much easier than d3.js and on a comparable level to ggplot2. I liked how each attribute of the graph, such as x-axis, y-axis, size, and color was a separate entity that could be altered. Even though I had to specific the x and y location of the bill length and species legend, it was easier to do so in Vega-lite than d3 because only an extra line needed to be added to the size and color fields.

Vega-lite also automatically disregards NA values, so the csv did not have to be cleaned. 

This graph differs because the x-axis shows increments of 5 instead of 10. The x and y axis titles are also smaller.

<img src="img/vegalite.png" alt="Vega-Lite plot" width="600">

<br>

# Python + Vega-Altair
 Vega-Altair is a Python visualization library that is built on Vega-Lite. Similar to Vega-Lite, each attribute of the graph is controlled by assigning it equal to data. 
 
 The graph is rendered as an .html file and displayed on a webpage. The program has to be run after every 
 have to run the program every time to update html

<img src="img/vegaaltair.png" alt="Vega-Altair Plot" width="600">

<br>

# Tableau
njsnj

## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Added Graph Title**:
- **Interactive Element**: 

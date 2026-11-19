Assignment 2 - Data Visualization, 5 Ways  

# Tableau

<img width="1983" height="1094" alt="pengling tableau" src="https://github.com/user-attachments/assets/b484b27b-9736-4cd9-a63c-8c9a6958a8c0" />
Tableau generated graphic
<img width="2700" height="1303" alt="image" src="https://github.com/user-attachments/assets/ec94d424-b2b4-444b-b82f-bc2b6d707788" />
Tableau set up 
https://public.tableau.com:9443/views/Assignment2Pengling/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Tableau is a tool that allows users to import a dataset and drag data columns to specific elements of a visualization. I used the opacity slider found after clicking on color to change the opacity from 100% to 80% and changed mark size from 25% to 30% using the slider in size. I changed the mark changed from automatic to circle to better fit the bubble. I decided to use color palette Tableau 10 with colors orange, purple, and teal. This allowed me to find the general colors but not as much specificity as preferred. I set the ticks for y starting at 2000 with tick intervals at 1000 with minor ticks at 500. The x axis starts at 170 uses interval of 10 for the ticks with minor ticks at 5 intervals. Generally this tool is very easy to use, but make customization difficult and it was hard to find the customization tools it did have.

# Python + Altair

<img width="883" height="624" alt="image" src="https://github.com/user-attachments/assets/929cf8eb-850d-4918-bfff-56e9f36a920f" />

Altair is a commonly used Python library based on Vega-Lite visualization tool with the main purpose being to statistical visualization. Altair does not have built in csv usage, so I specified the data using the pandas `read_csv` function. I used `scale(domain=domain,range=colors)` to set `colors=["#ff8e08","#9933cc","#158f8f"]` at specific values as opposed to preset schemes. The scale was set to start at 170 for x axis and 2500 for y axis because including `.scale(zero=False)` allowed for autoscaling instead of having to include zero. I also changed background colors by configuring background and axis grid color. This was a very strightforward language that allowed for decent customization very efficiently.

# R + ggplot2

<img width="1639" height="1435" alt="image" src="https://github.com/user-attachments/assets/cfa81c1e-a644-4dd3-8159-e3cb4071edd7" />

ggplot2 is a an R package  typically used for general data visualization. As R is already a statistical language, ggplot2 integrates smoothly with the language. I used `geom_point`'s alpha feature to set opacity to 80%, `scale_color_manual()` to set colors to orange:#ff8e08, purple: #9933cc, and teal: #158f8f, and `labs()` to set x and y labels. I scaled points size to a range from 1 to 10 to improve readability of the chart. ggplot2 was fairly useable with somewhat difficulty finding customization features, but all ultimately possible.

# MATLAB

<img width="1099" height="1064" alt="image" src="https://github.com/user-attachments/assets/9babe347-28ab-4625-8095-45398c817c41" />

MATLAB is primarily a computing environment that also supports visualization techniques. To be able to show plit species into separate datasets to overlay on the same graph. Used `tiledlayout("flow")` to put all species on same chart by keeping them on one tile. Set bubble size to low of 5, high of 20. Used `MarkerFaceColor` and `MarkerEdgeColor` for each separate species graph with the associated colors orange:#ff8e08, purple: #9933cc, and teal: #158f8f, along with `MarkerFaceOpacity` set to 0.8. I then turned on the grid, and set the color, grid color, and grid line width. I used the `bubblelegend` and `legend` functions to create the two legends with both positioned to the right of the chart using `.Layout.Tile = "east"` and the bubble size order switched to ascending. This language was not the easiest for visualization and had interesting customization options, such as position being dictated by cardinal direction.

# d3

<img width="946" height="719" alt="image" src="https://github.com/user-attachments/assets/798f0226-371e-4e9c-9336-f4764fd38903" />

<img width="974" height="897" alt="image" src="https://github.com/user-attachments/assets/d028d833-ea35-475d-b4b2-283f29de1375" />


d3 is a common library for JavaScript data visualizations that can be incorporated directly into an html file. I used `scaleOrdinal` with the species defined for the domain and the colors orange:#ff8e08, purple: #9933cc, and teal: #158f8f for the range. Style was used to set both the previously defined colors and set the opacity to 0.8. d3 does not automatically have a background, so I appended a rectangle as a background to add background color and when defining the scale using `scaleLinear` going from 170 to 235 on x and 2500 to 6500 on y, added ticks of a noticeable size and similar color to the original. When adding labels to the y-axis, I had to rotate it -90 degrees to sit properly on the axis instead of having a built in feature. For the legends, I was able to specifically identify which sizes I wanted the size legend to present (40, 50) and place them based on the size times a multiplier to make them not overlaid. The color legend I was able to control the size of the circles for the color. I also integrated a tool tip feature that is hidden when first opened, but when a data point is hovered over, highlights the border of the point and displays flipper length, body mass, and bill length below the visualization. d3 had many more steps to reach the result, however, each of those steps added many additional customization options to the process. It also had easily integrateble customizability.

## Technical Achievements
- **d3 Tooltip**: I added intractability with my d3 visualization by allowing the user to hover over a given penguin data point and see a bar at the bottom with the exact flipper length, body mass, and bill length. I also made the selected penguin point turn white on the outside edge to show which one is selected.
- **MATLAB Multicolor**: MATLAB did not have the feature all the other languages had for a nominal category to be automatically given different colors. However, I was able to work around this issue by splitting the graph into three different overlaid graphs, making use of tildelayout, nexttile, and hold.

### Design Achievements
- **Color Consistency**: I used a color picker on the original plot to determine the closest hex code for the three colors used to indicate species as well as for the background and grid color.
- **Size Consistency**: I frequently changed the size scales of the marks, seen in Tableau, ggplot2, MATLAB, and d3, to better fit the visualization and more easily interpret the data.

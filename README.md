# Excel

Excel is a spreadsheet and data analysis tool that is part of Microsoft Office. 
It has a relatively low barrier to entry compared to other more code-heavy options which can be good for people with less coding experience. 
However, it can become clunky to manipulate data, especially since every array of data needs to be shown in data cells in the software.
Additionally, finding everything within the Excel UI can become a pain.
Sometimes even when I knew what I needed to do, it was hard to find the menu to actually do it.  
To make the chart, I used a bubble chart since it allows for changing bubble size based on a "z" value. 
To organize the data for the chart, I made a new sheet with the 3 data columns for each type of penguin using the Filter function to filter for the correct penguin type and to get rid of NA values. 

![excel](img/excel.png)

# Python
Python is a coding language that is easy to begin development in and contains many useful libraries. 
Many of these libraries are useful for processing and visualizing data. 
Because of that, creating a basic chart only takes a few lines of code when using these libraries, creating a low barrier to entry. 
I also know that if I wanted to expand the visualization further or use it within a website in the future, I would be able to due to Python and its libraries' great flexibility and wide range of features.  
For my chart, I used Pandas to convert the CSV to a dataframe. 
Then, I used Matplotlib's scatter function to create the graph, and used its built in show function to display the graph in a new window after running the program. Since the scatter function uses area for circle size which is difficult to see small differences in size for, I created a new equation to make the size differences for the circles easier to see.

![python](img/python.png)

# R
R is another coding language, although it is less flexible than Python being focused mainly on data and statistics. 
I used a regular R file in RStudio with the output going directly to the "plots" tab in RStudio.   
I used R's built-in read.csv function to convert the CSV to a dataframe, then I used ggplot's geom_point function to create the scatterplot. 
One thing I especially appreciate about this was that a legend was automatically created, including automatic size scaling for the dots and dot size being included in the legend. 

![R](img/r.png)

## Technical Achievements
- **Excel**: Used Filter functions to manually created seperate columns of data for each penguin species with NA values filtered out so that those columns could be used as different groups within a Bubble Plot.
- **Python**: Used Pandas to convert the CSV into data for Matplotlib to visualize.
- **R**: Used built-in R functionality to convert the CSV into data for ggplot to visualize.

### Design Achievements
- **Excel**: Manually set X and Y range and scale so as to not start each axis at 0. Changed bubble size from area to radius to diameter to make size differences more visible.
- **Python**: Created custom dot size function to make the differences in dot size more visible, changed alpha value of dots to make them semitransparent.
- **R**: Changed alpha value of dots to make them semitransparent.

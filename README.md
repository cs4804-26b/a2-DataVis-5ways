Assignment 2 - Data Visualization, 5 Ways  
===
# Introduction

For this assignment, I used five different visualization tools to create scatterplots using the penguin dataset. I also explored one additional tool to gain more experience with different ways of creating visualizations

The five main tools I used were Matplotlib, Altair, D3.js, ggplot2, and Flourish. Tableau was my additional tool

Each visualization shows flipper length on the X-axis and body mass on the Y-axis. The colors represent penguin species, while circle sizes represent bill length. I tried to keep the visualizations consistent while learning about the features and limitations of each tool.

---
# Matplotlib (Python)
Code: https://github.com/AmieHuynh2101/a2-DataVis-5ways/blob/main/matplotlib/plot.py
<img width="2700" height="1800" alt="image" src="https://github.com/user-attachments/assets/8ecdc3b4-d774-4f33-bd2c-c1e584a87472" />


Matplotlib was one of the more straightforward tools because I could control the chart using Python code. It was easy to set the axis ranges, colors, and labels. However, I had to manually configure the legend and circle sizes. I think Matplotlib would be useful for data analysis and projects where I need more control over how a chart looks

---
# Altair (Python)
Code: https://github.com/AmieHuynh2101/a2-DataVis-5ways/blob/main/altair/plot.py
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/d9ce3ccc-9abc-400e-b60c-7dd92bb8e572" />


I found Altair easier to work with than Matplotlib in some ways because I could directly choose which data columns controlled the position, color, and size of the points. Adding tooltips was also simple, which made the chart more interactive. The harder part was figuring out how to change the axis scales and customize the design. I think Altair would be a good choice for exploring data and making interactive charts without needing too much code.

---
# D3.js (JavaScript)
Code: https://github.com/AmieHuynh2101/a2-DataVis-5ways/blob/main/d3/index.html
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b34a5315-2803-47dd-a0d5-3229e158e37d" />


D3.js took more time because I had to build most parts of the chart myself, including the axes, scales, circles, and legends. I also needed to figure out how to load the csv file and remove missing values so the chart would display correctly. Even though it was more difficult. I like having the freedom to change almost every part of the visualization. I added tooltips to show information about each penguin and a dropdown menu to filter different species. I think D3.js would be useful for building interactive charts on websites where I want more control over the design.

---
# ggplot2 (R)
Code: https://github.com/AmieHuynh2101/a2-DataVis-5ways/blob/main/ggplot2/plot.R
<img width="1500" height="900" alt="image" src="https://github.com/user-attachments/assets/1b814d99-306c-4364-ba51-23b0799c579c" />


I like how ggplot2 allowed me to create the chart by adding different layers. Once I understood how to connect the dataset columns to the axes, colors, and circle sizes, the visualization was not too difficult to make. The biggest challenge was getting R to work in VS Code and installing the package correctly. After solving those, the rest of the process was much easier. I think ggplot2 would be helpful for research, statistical analysis, and making charts for reports.

---
# Flourish
Visualization link: https://public.flourish.studio/visualisation/30886275/
<img width="794" height="545" alt="image" src="https://github.com/user-attachments/assets/03768b5c-7923-4d2e-be0a-162c78e66c02" />

Flourish was different from the previous tools because I could make the visualization without writing any code. I uploaded the penguin dataset and selected the columns for the axes, colors, and circle sizes. I like being able to see the chart update as I changed the settings. However, it took some time to find options for changing the colors, axis ranges, and other details. I think Flourish would be useful when I need to make an interactive chart quickly, especially for presentations or websites.

---
# Tableau
Tableau workbook: https://github.com/AmieHuynh2101/a2-DataVis-5ways/blob/main/tableau/tableau.twb
<img width="962" height="529" alt="image" src="https://github.com/user-attachments/assets/5daaf4a2-13f9-48c6-9884-155747325585" />

I also tried Tableau as an extra tool beyond the five required visualizations. Instead of writing code, I could drag the data columns into different areas to build the scatterplot. I used flipper length and body mass for the axes, species for the colors, and bill length for the circle sizes. Creating the basic chart was easy, but finding the settings for the axis ranges, colors, and opacity took more time. I think Tableau would be helpful for exploring large datasets and creating dashboards without having to write much code. 

---
# Technical Achievements

+ Five required tools and one additional tool: I created visualizations using Matplotlib, Altair, D3.js, ggplot2, and Flourish. I also explored Tableau to learn another way of making charts
+ D3.js interactions: I added hover tooltips that show penguin measurements and a dropdown menu that allows users to focus on different species.
+ Altair tooltips: I made the Altair chart interactive so users can hover over points to see more information
+ Handling missing data: I removed rows with missing measurements to prevent errors and make sure the points were displayed correctly
+ Different programming languages: I worked with Python, JavaScript, and R, Flourish, and Tableau
---
# Design Achievements

+ Consistent chart design: I kept flipper length on the X-axis and body mass on the Y-axis for all six visualizations. I also used colors to represent species and circle sizes to represent bill length.
+ Clear species colors: I chose different colors for each penguin species so they would be easy to tell apart.
+ Adjusted axis ranges: I made the axes start above zero to focus more on the actual measurements and make the differences easier to see
+ Circle transparency: I used around 80% opacity to help show points that overlap
+ Clear Charts: I added clear axis labels, tick marks, and legend where possible so the reader could understand the visualization more easily
---
# Conclusion

Through this assignment, I learned that different visualization tools have their own strengths and challenges. Matplotlib and ggplot2 were useful for making charts with code, while Altair made it easier to add interactive features. D3.js was more challenging because I had to build many parts myself, but it gave me more freedom to customize the chart. Flourish and Tableau were easier to use because I could create visualizations through their interfaces. Overall, trying these tools helped me understand which tool might be more useful for different projects.


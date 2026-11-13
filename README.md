# Assignment 2 of CS4804 B26
### Param Amre

## View Files
For all library based visualizations, please run an http server at the root of the project. Run anything needed to generate the html file (see relevant section for directions), and navigate to localhost:8000/folder-name/ to see and interact with the graph.

## Javascript + d3
Navigate to [server-url]/d3/.

![d3-based visualization](./img/d3.png)

Javascript is a scripting language primarily developed for the web. d3 is an data science industry standard that provides abstractions for creating visualizations.
I started with the code from the [basic d3 scatter plot ecample](https://observablehq.com/@d3/scatterplot/2), and adjusted it for the dataset we were given.
Using d3's documentation, I was also able to find the d3 way of adding hoverable interactivity, similar to my submission for assignment 1.

### Technical Achievements
- Hoverable interactivity: when a user hovers over a given point, then can look at the popup in the lower right of the graph to see the exact values that points represents
- All points are generated with a join that applies every piece of formatting needed, including the interactivity

### Design Achievements
- Legend: I manually created a legend in d3, using basic svg tag types. I wasn't able to find any automatic legend creation values in the docs, so I manually drew one out myself.

## Python + Altair
To view the page, run altair/main.py with any [PEP 723](https://peps.python.org/pep-0723/) compatible tool (uv, hatch, poetry, pipx, etc), and navigate to [server-url]/altair/

![altair-based visualization](./img/altair.png)

Python is a general purpose high level programming language that has a variety of different applications, including in data science. Altair is a python package that is based on, and generates Vega-Lite definitions. Vega-lite itself a formal schema for defining visualizations (see below). Because of this, the altair packages is relatively low level in that it only provides several generic chart types to the user, where objects corresponding to Vega-Lite definitions are expted to be passed in to create the visualization.

### Technical Achievements
- The graph is interactive, and a user can over over each point to see a popup of the 4 values visible in the graph.
- Visualization is rendered to html, making the visualization's generation independent of its display

### Design Achievements
By rendering to html, instead of directly displaying the visualization from the script, I was able to seperate the visualization's generation from it's display, which would allow me to modify it further, or embed it within something else as I wanted.

## Excel
Open the file in ./excel/a2-excel-Param-Amre.xlsx in Excel to see the graph.

![excel-based visualization](./img/excel.png)

Excel is a spreadsheet tool created by Microsoft. It is arguably the best tool for sharing data that people with many different skill sets need to work with, as it's very well known,
and many non-technical people are much more likely to be famailar with it. Essentially, Excel is a established standard solution.
To work with the data, I loaded it into a spreadsheet ([link to actual spreadsheet here](https://wpi0-my.sharepoint.com/:x:/g/personal/puamre_wpi_edu/IQAT3dWOI7AWRoLzHMaFFJQ5AfDUq31plc2k-7eGoXRrVoA?e=vuc8Bq))
and formatted it into a table. This let me sort the columns, which let me easily delete rows with null values. I then used the sorting features to sort the data by species, which let me
create a data series for each one. Excel doesn't natively let you color or size values by another value in a scatter chart, so I create 3 sets of data on the same graph to work around the
color issues. I think this is reasonable because Excel is not primarily focused on creating visualizations, it's aimed at a non Computer/Data Science audience.

### Technical Achievements
- The workaround for displaying colors of multiple types on mentioned above

## Python + Plotly
To view the page, run altair/main.py with any [PEP 723](https://peps.python.org/pep-0723/) compatible tool, and navigate to [server-url]/altair/

Plotly is a python package written for creating interactive visualizations. I specificaly used the express subpackage, which is a very high level way of creating graphs. In writing the graph this way,
I was able to get several features, such as graph interactvitiy (zooming in and out, hovering over data points for popups with information, export) without having to write any code. However, to do things outside the scope of the high level API, workarounds have to be used, or you have the use the alternate lower level API. For example, the API doesn't let the user seperate the scale from values plotted, so I
had to manually set the size mode (area to diamter) of the size markers. Even then, the engine resizes the points if they get too large, so I couldn't the get the points to look as large as I wanted them to.

### Technical Achievements
- Working around high level API to provie more a visual difference between marker sizes

### Design Achievments
- None, as all graph design features were provided by the library

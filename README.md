# Assignment 2 - Data Visualization, 5 Ways

Russell Hertel (hert22)

For this assignment I made the same penguin scatterplot with 5 different tools. Flipper length is on the x axis and body mass is on the y axis. Color is species and size is bill length. I used 3 libraries (d3, Altair, matplotlib) and 2 tools (Excel, Datawrapper).

In every version I removed the rows with NA values first. I also used the same 3 colors for the species every time.

# d3

Code is in the `d3` folder. To run it, start a server in the repo folder with `python3 -m http.server` and go to http://localhost:8000/d3/.

![d3](img/d3.png)

d3 took the most work out of all of them. You have to build everything yourself, like the axes, the labels, the grid and the legend. Loading the csv is async, so all the drawing has to go inside the `.then()`. I had to filter out the "NA" rows or the circles would break. I used `scaleSqrt` for the size so bigger bills don't look way too big. The good part is you can control everything. I would use d3 for a custom chart on a website.

# Altair

Code is in the `altair` folder. Run `python3 penguins_altair.py` from inside that folder. It saves an html file and a png.

![altair](img/altair.png)

Altair was the easiest one. You just say which column goes to x, y, color and size, and it makes the legends for you. The only thing I had to change was `zero=False` on the scales because Altair starts at 0 by default. Adding a tooltip and zoom only took one line each. I would use this for quick charts in python.

# matplotlib

Code is in the `matplotlib` folder. Run `python3 penguins_matplotlib.py` from inside that folder.

![matplotlib](img/matplotlib.png)

matplotlib was pretty easy too, but it is more manual than Altair. It doesn't do color by a category on its own, so I looped over each species and plotted them one at a time. The size also had to be scaled by hand. I did `(bill length - 30) * 6` so the dots were a good size. The legend only shows species, not bill length. It does start the axes at the data and not at 0, which was nice. I would use it for static charts for a report or paper.

# Excel

The file is `excel/penguins_excel.xlsx`.

![excel](img/excel.png)

I used a bubble chart in Excel since a normal scatter can't change the dot size. I had to split the data into 3 sets of columns, one for each species, so each species could be its own series with its own color. Then the bill length column is the bubble size. I set the axis min and max by hand so they don't start at 0. I set the fill transparency to 20% to get the 0.8 opacity. There is no legend for the bubble size. Excel is good if you just want a fast chart and don't want to code.

# Datawrapper

The cleaned data I uploaded is `datawrapper/penglings_clean.csv`.

![datawrapper](img/datawrapper.png)

Datawrapper is a website where you upload a csv and pick a chart type. I picked scatter plot and set x to flipper length, y to body mass, color to species and size to bill length. It was very fast and it adds hover tooltips by default. I did have to upload a csv with the NA rows taken out. You can't control things as much as with code. It would be good for making a quick chart for a news article or a blog.

# Technical Achievements

- **Tooltips in d3:** If you hover over a dot it shows the species, flipper length, body mass and bill length. The dot also gets a black outline.
- **Tooltips and zoom in Altair:** The Altair html has tooltips. You can also zoom and pan with `.interactive()`.
- **Size legend in d3:** I made a legend for bill length by hand with 3 example circles.
- **Data cleaning:** Every version removes the rows with NA before plotting.
- **Tooltips in Datawrapper:** Datawrapper has hover info built in.

# Design Achievements

- **Same colors everywhere:** All 5 charts use orange for Adelie, purple for Chinstrap and teal for Gentoo. This makes them easy to compare.
- **Light grid:** I made the grid lines light gray so they don't get in the way of the dots.
- **Square root size scale:** In d3 I used `scaleSqrt` so the area of a circle matches the bill length better.
- **Clear labels:** All the axes have labels with units.

## Tools summary

| tool | type | easy? | notes |
|---|---|---|---|
| d3 | javascript library | hard | full control but a lot of code |
| Altair | python library | easy | legends and tooltips for free |
| matplotlib | python library | medium | had to loop for colors |
| Excel | tool | medium | needed bubble chart and split columns |
| Datawrapper | tool | easy | fast but less control |

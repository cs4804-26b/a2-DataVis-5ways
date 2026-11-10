Assignment 2 - Data Visualization, 5 Ways  
===
# d3

Description of d3

I think the easiest part of this was just modifying to get the right properties after adding all of the elements. Once the data points were on the screen, it was pretty easy to change their sizes & opacity. I'd say the most difficult part was just learning how to add axes + gridlines. Also, I forgot about that d3 needs to wait for data to load, so I got confused for a while about why there weren't data points on my screen. I didn't really add the legend through any sort of legend tool, just added shapes to make up the legend - same with the background color. I could see using this tool in the future, potentially for my MQP as I will be making a data visualization tool.

![d3](img/d3.png)

# R + ggplot2

Description of R + ggplot2

This tool was by far the easiest, although the syntax was quite confusing as I'd never used R before. However, once I made the plot, it was pretty much the same as the original example image since that was made in R + ggplot2. The main difficulty came from adding linear scaling to the plot by diameter instead of the default of scaling by area, as I had to figure out how to create custom scaling. It would've been easiest if I had kept the original scaling, but that would make it much harder to apply to other tools.

There's a good chance I'll use R in the future as it's common in computational biology, but I can't say I liked the format. It felt weird just building from a base plot and adding things to it. I didn't really have to use any hacks to get the right chart since the original chart was already made using R + ggplot2.

![r](img/r.png)

# Python + Jupyter + Matplotlib

Description of Python + Matplotlib

This one was probably easier than d3, mainly because it followed a very similar format and I could copy many of the variables used there, but it was certainly not as easy as using R. I've had the most experience doing data visualization using Matplotlib, so I thought this would be simple, but I had to use many different tools than I've been used to. It felt like each time I wanted to make a simple change I'd have to look up the syntax to do so with Matplotlib. However, I'm overall quite happy with how it turned out in the end, as it ended up closest to the original image.

I definitely would use this tool in the future, as it's pretty versatile and I have experience with using it. I'd say I had to use hacks to implement the legend, because although I was originally going to try using the built in Matplotlib legend, I wasn't sure if I would be able to replicate the same grey background squares with the correctly sized circles in the middle. So, I just manually added a bunch of shapes and text.

![python](img/python.png)

# Python + Jupyter + Altair

Description of Tool/Library 4

I was somewhat expecting Altair to be easier, primarily because it's also Python, but it was probably the most difficult tool overall. Altair is very simple if I just want a nice, easy chart, but to get it to meet the design achievements I was going for took a ton of effort. The worst part by far was trying to do the scaling properly, as looking for resources on this ended up suggesting a transformation on the data, but in Altair the legend is directly connected to the data so it would display inaccurately. I ended up figuring out how to use the scale to properly match the data to a quadratic area scaling, but I almost just gave up. I think another of the most annoying parts was when I realized there were no minor gridlines available in Altair, so I ended up just making two separate charts for x-axis and y-axis minor gridlines.  Padding the edges to create the correct image size was also annoying, but didn't take too long. I unfortunately was not able to preserve the nice gray background behind the circles in the legend, since Altair does not support drawing outside of the main chart. All things considered, I am pretty happy with what I was able to do in regards to the design achievements, as I was able to preserve nearly everything. 

I could see this tool being useful in the future if you just wanted to make a simple chart and not attempt to design it to perfectly match another chart. If you're trying to do the latter like I was, avoid Altair. 

![Altair](img/altair.png)

# Excel

Description of Tool/Library 5

I was in the mood for something significantly easier after Altair, so I chose Excel as my fifth tool. I'm not entirely sure why I thought it would be that easy, as although Excel is pretty easy to use for simple plots, it definitely wasn't made to copy specific styles. Luckily, it wasn't that hard either, just probably ranked close to d3 in difficulty making the plot. There's a handy bubble chart made for making different dots of different sizes, and I could just make a new series for each color, so those parts were pretty easy. I think some of the most difficult parts were just figuring out that I could do these things in Excel, as there isn't any sort of code and instead it just involved me searching through dropdown menus. I ended up doing a simple trick for the y-axis, as Excel doesn't allow for custom y-axis labels, so I just made a new series at the y-axis and put data labels to the left of it. Excel's axis limits do also mean that I couldn't place the major and minor y-axis where I wanted to, so instead every line is a major line, which does go against my design unfortunately. Excel also doesn't allow custom tick marks, so I put short lines at each tick manually. Finally, the legend is also something Excel doesn't really style all that well, so I just made the legend out of various Excel shapes. I would absolutely use Excel again as it is useful for editing CSVs and making simple charts while working directly with the data, but if I had a very specific visualizaiton in mind, I wouldn't use Excel. 

![Excel](img/excel.png)


## Technical Achievements
List of potential tech achievement I could do:
- **Interactivity**: Might only do that in d3 or if it's easy elsewhere
- **Extra tools/libraries**: Could go above the 5 requested, also could maybe do something like three.js which would be really weird
- **API Usage???**: idk how i would do this but it'd be an achievement!
- **Fun Stuff in each tool**: some tools might have additional functionality that I could mess with
- **Filters**: could make axes + sizing + coloring customizable - potentially very hard to do

### Design Achievements
- **Consistent color choice**: Consistently used the same colors (purple #9f3fce = Chinstrap, orange #fc992f = Adelie, cyan #219292 = Gentoo), as picked from the original image in the assignment:
![color picked](img/colorpicker.png)
- **Consistent element size, font choice**: Element size also measured directly from the original image - 50mm is a 41px diameter circle, 40mm is a 32px diameter circle, so the ratio is about 0.8px/mm. There seems to be some sort of non-linear scaling, because the point at (188, 3050) in the example is far smaller than it should be, but I chose to do linear scaling for each point by diameter. Font identified as Arial, 26px tall for axes & 21px tall for axis labels. I've attached images to show where I got my measurements from, but a summary of all measurements that I kept consistent:
    - Size Mapping: 0.8px diameter circle per 1mm bill length
        - 2px outline for each circle
    - Font: Arial, 26px for legend & axis labels, 21px for smaller axis labels & legend labels
        - Axis label font color: #707070
    - Image size: 1700x1050
    - Chart size: 1200x900
        - Chart margins: 150px left, 350px right, 50px top, 100px bottom
    - Legend Placement 
        - bill_length_mm is at (1400, 250) and species is at (1400, 490)
        - each gray square behind the dots in the legend are 56px by 56px
        - the dots for species each have a 8px diameter
Overall, this design achievement was by far the hardest part of this assignment, and I likely should have done something much easier. At least it worked!
50mm circle:
![41x41 circle](img/41x41.png)
Overall measurements:
![Annotated Measurements](img/measurements.png)
- **Background Grid + Legends**: Not part of the assignment requirements, but I kept them for each library/tool. Background color is #ebebeb, grid lines are white (2px for major gridlines and 1px for minor).
- **Second Chart Type**: could also try to make histograms as a second comparison method